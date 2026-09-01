#!/usr/bin/env python3
"""Mike: a local voice assistant with wake-word and basic OS control.

Notes:
- This is a starter implementation. You can expand `COMMAND_PATTERNS` and `APPS`.
- Uses speech_recognition + pyttsx3. Optional: pyautogui for keyboard/mouse control.
- Offline wake-word detection uses Vosk (optional).
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import platform
import queue
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
import urllib.parse as _url

try:
    import speech_recognition as sr
except Exception as exc:  # pragma: no cover
    print("Missing dependency: speech_recognition. Install with `pip install SpeechRecognition`.")
    raise

try:
    import pyttsx3
except Exception as exc:  # pragma: no cover
    print("Missing dependency: pyttsx3. Install with `pip install pyttsx3`.")
    raise

# Optional offline wake-word / offline STT
try:
    import vosk
except Exception:
    vosk = None

# Optional dependency for keyboard/mouse control
try:
    import pyautogui
except Exception:
    pyautogui = None


WAKE_WORD = "mike"
WAKE_WORDS = {"mike", "maik", "মাইক"}
WAKE_COOLDOWN_SECONDS = 1.2

MIC_SAMPLE_RATE = 16000
LANG_PRIMARY = "en-GB"
LANG_SECONDARY = "bn-BD"  # Bangla
USE_GOOGLE_STT = True       # True = online Google STT via SpeechRecognition
USE_OFFLINE_STT = False     # True = Vosk for full command recognition (offline)
OFFLINE_WAKE_WORD = True    # True = Vosk wake-word detection (offline)
ALLOW_DIRECT_COMMANDS = False

VOSK_MODEL_PATH = os.getenv(
    "VOSK_MODEL_PATH",
    os.path.join(os.path.dirname(__file__), "models", "vosk-model-small-en-us-0.15"),
)

BN_DIGIT_TRANSLATION = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")

ASSISTANT_NAME = "Mike"

# Map friendly app names to OS commands
APPS = {
    "browser": "browser",
    "chrome": "google-chrome",
    "firefox": "firefox",
    "terminal": "gnome-terminal",
    "files": "nautilus",
    "calculator": "gnome-calculator",
    "ব্রাউজার": "browser",
    "ক্রোম": "google-chrome",
    "গুগল ক্রোম": "google-chrome",
    "ক্রোম ব্রাউজার": "google-chrome",
    "ফায়ারফক্স": "firefox",
    "ফায়ারফক্স": "firefox",
    "টার্মিনাল": "gnome-terminal",
    "ফাইলস": "nautilus",
    "ফাইল ম্যানেজার": "nautilus",
    "ক্যালকুলেটর": "gnome-calculator",
}

PATH_ALIASES = {
    "home": "~",
    "desktop": "~/Desktop",
    "downloads": "~/Downloads",
    "documents": "~/Documents",
    "music": "~/Music",
    "pictures": "~/Pictures",
    "videos": "~/Videos",
    "ডেস্কটপ": "~/Desktop",
    "ডাউনলোড": "~/Downloads",
    "ডাউনলোডস": "~/Downloads",
    "ডকুমেন্টস": "~/Documents",
    "ডকুমেন্ট": "~/Documents",
    "মিউজিক": "~/Music",
    "সংগীত": "~/Music",
    "ছবি": "~/Pictures",
    "ভিডিও": "~/Videos",
}

SITES = {
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "messenger": "https://www.messenger.com",
    "whatsapp": "https://web.whatsapp.com",
    "reddit": "https://www.reddit.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt": "https://chat.openai.com",
    "ইউটিউব": "https://www.youtube.com",
    "ফেসবুক": "https://www.facebook.com",
    "গুগল": "https://www.google.com",
    "জিমেইল": "https://mail.google.com",
    "মেসেঞ্জার": "https://www.messenger.com",
    "হোয়াটসঅ্যাপ": "https://web.whatsapp.com",
    "হোয়াটসঅ্যাপ": "https://web.whatsapp.com",
    "রেডডিট": "https://www.reddit.com",
    "গিটহাব": "https://github.com",
    "স্ট্যাকওভারফ্লো": "https://stackoverflow.com",
    "চ্যাটজিপিটি": "https://chat.openai.com",
    "চ্যাট জিপিটি": "https://chat.openai.com",
}

KEY_ALIASES = {
    "এন্টার": "enter",
    "রিটার্ন": "enter",
    "স্পেস": "space",
    "স্পেসবার": "space",
    "ব্যাকস্পেস": "backspace",
    "ডিলিট": "delete",
    "ট্যাব": "tab",
    "এস্কেপ": "esc",
    "এসকেপ": "esc",
    "এস্ক": "esc",
    "আপ": "up",
    "ডাউন": "down",
    "লেফট": "left",
    "রাইট": "right",
    "কন্ট্রোল": "ctrl",
    "কন্ট্রল": "ctrl",
    "কন্ট্রোল": "ctrl",
    "কন্ট্রল": "ctrl",
    "সিফট": "shift",
    "শিফট": "shift",
    "অল্ট": "alt",
    "অ্যাল্ট": "alt",
    "আল্ট": "alt",
    "হোম": "home",
    "এন্ড": "end",
    "পেজ আপ": "pageup",
    "পেজ ডাউন": "pagedown",
    "পেজআপ": "pageup",
    "পেজডাউন": "pagedown",
}

# Simple patterns -> handler names
COMMAND_PATTERNS = [
    # Files
    (r"^open folder (.+)$", "open_folder"),
    (r"^open file (.+)$", "open_file"),
    (r"^create folder (.+)$", "create_folder"),
    (r"^(?:ফোল্ডার|ডিরেক্টরি) (?:খুলো|খুলে দাও|ওপেন কর) (.+)$", "open_folder"),
    (r"^ফাইল (?:খুলো|খুলে দাও|ওপেন কর) (.+)$", "open_file"),
    (r"^(?:নতুন )?ফোল্ডার (?:বানাও|তৈরি কর|ক্রিয়েট কর|ক্রিয়েট কর) (.+)$", "create_folder"),

    # Sites
    (r"^open (youtube|facebook|google|gmail|messenger|whatsapp|reddit|github|stackoverflow|chatgpt)$", "open_site"),
    (
        r"^(ইউটিউব|ফেসবুক|গুগল|জিমেইল|মেসেঞ্জার|হোয়াটসঅ্যাপ|হোয়াটসঅ্যাপ|রেডডিট|গিটহাব|স্ট্যাকওভারফ্লো|চ্যাটজিপিটি|চ্যাট জিপিটি)"
        r" (?:খুলো|খুলে দাও|চালু কর|ওপেন কর)$",
        "open_site",
    ),

    # Apps / Web
    (r"^open (.+)$", "open_app"),
    (r"^(?:খুলো|খুলে দাও|ওপেন কর|ওপেন|চালু কর|স্টার্ট কর|লঞ্চ কর) (.+)$", "open_app"),
    (r"^search (?:for )?(.+)$", "web_search"),
    (r"^(?:খুঁজে দাও|সার্চ কর|সার্চ) (.+)$", "web_search"),
    (r"^(?:গুগলে|ইন্টারনেটে) (?:খুঁজে দাও|সার্চ কর|সার্চ) (.+)$", "web_search"),
    (r"^go to (.+)$", "open_url"),
    (r"^(?:যাও|গো টু|ওয়েবসাইট খুলো|ওয়েবসাইট খুলো) (.+)$", "open_url"),

    # Input
    (r"^type (.+)$", "type_text"),
    (r"^press (.+)$", "press_key"),
    (r"^write note (.+)$", "write_note"),
    (r"^(?:টাইপ কর|টাইপ করো|লিখে দাও|লিখো|লিখ) (.+)$", "type_text"),
    (r"^(?:চাপ দাও|চাপো|প্রেস কর|প্রেস করো|কি চাপো|কী চাপো) (.+)$", "press_key"),
    (r"^(?:নোট লেখো|নোট লিখ|নোটে লিখ|নোটে লিখে রাখ) (.+)$", "write_note"),

    # Window
    (r"^(?:switch window|next window|alt tab)$", "window_next"),
    (r"^(?:previous window|back window)$", "window_prev"),
    (r"^(?:উইন্ডো বদলাও|পরের উইন্ডো|আল্ট ট্যাব)$", "window_next"),
    (r"^(?:আগের উইন্ডো)$", "window_prev"),

    # Volume
    (r"^(?:volume up|increase volume|turn up volume)$", "volume_up"),
    (r"^(?:volume down|decrease volume|turn down volume)$", "volume_down"),
    (r"^set volume (\d{1,3})%?$", "set_volume"),
    (r"^(?:mute)$", "mute_volume"),
    (r"^(?:unmute)$", "unmute_volume"),
    (r"^(?:ভলিউম বাড়াও|ভলিউম বাড়াও|সাউন্ড বাড়াও|সাউন্ড বাড়াও|শব্দ বাড়াও|শব্দ বাড়াও)$", "volume_up"),
    (r"^(?:ভলিউম কমাও|সাউন্ড কমাও|শব্দ কমাও)$", "volume_down"),
    (r"^ভলিউম সেট কর (\d{1,3})%?$", "set_volume"),
    (r"^(?:মিউট কর|মিউট করো)$", "mute_volume"),
    (r"^(?:আনমিউট কর|আনমিউট করো)$", "unmute_volume"),

    # Brightness
    (r"^(?:brightness up|increase brightness|turn up brightness)$", "brightness_up"),
    (r"^(?:brightness down|decrease brightness|turn down brightness)$", "brightness_down"),
    (r"^set brightness (\d{1,3})%?$", "set_brightness"),
    (r"^(?:ব্রাইটনেস বাড়াও|ব্রাইটনেস বাড়াও|উজ্জ্বলতা বাড়াও|উজ্জ্বলতা বাড়াও)$", "brightness_up"),
    (r"^(?:ব্রাইটনেস কমাও|উজ্জ্বলতা কমাও)$", "brightness_down"),
    (r"^ব্রাইটনেস সেট কর (\d{1,3})%?$", "set_brightness"),

    # System
    (r"^(?:what time is it|time)$", "tell_time"),
    (r"^(?:stop listening|sleep)$", "sleep"),
    (r"^(?:exit|quit|goodbye)$", "quit"),
    (r"^(?:সময় কত|সময় কত|কয়টা বাজে)$", "tell_time"),
    (r"^(?:চুপ কর|ঘুমাও)$", "sleep"),
    (r"^(?:বন্ধ কর|বিদায়|বিদায়)$", "quit"),
]


class MikeAssistant:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(sample_rate=MIC_SAMPLE_RATE)
        self.engine = pyttsx3.init()
        self.sleeping = False
        self.running = True
        self._speech_queue: "queue.Queue[str]" = queue.Queue()
        self._lock = threading.Lock()
        self._last_wake_time = 0.0
        self._init_offline_models()
        self._configure_voice()

    def _init_offline_models(self) -> None:
        self._use_vosk_wake = False
        self._use_vosk_stt = False
        self._vosk_rec_wake = None
        self._vosk_rec_full = None

        if not (OFFLINE_WAKE_WORD or USE_OFFLINE_STT):
            return

        if vosk is None:
            print("Offline wake-word/STT requested but Vosk is not installed.")
            return

        if not os.path.isdir(VOSK_MODEL_PATH):
            print(
                "Offline wake-word/STT requested but Vosk model not found at "
                f"{VOSK_MODEL_PATH}."
            )
            return

        model = vosk.Model(VOSK_MODEL_PATH)
        if OFFLINE_WAKE_WORD:
            self._vosk_rec_wake = vosk.KaldiRecognizer(model, MIC_SAMPLE_RATE)
            self._use_vosk_wake = True
        if USE_OFFLINE_STT:
            self._vosk_rec_full = vosk.KaldiRecognizer(model, MIC_SAMPLE_RATE)
            self._use_vosk_stt = True

    # -------------------- Speech Output --------------------
    def _configure_voice(self) -> None:
        """Try to select a British English voice. Fall back to default."""
        try:
            voices = self.engine.getProperty("voices")
        except Exception:
            return

        british_candidates = []
        for v in voices:
            name = (getattr(v, "name", "") or "").lower()
            vid = (getattr(v, "id", "") or "").lower()
            if "british" in name or "uk" in name or "england" in name:
                british_candidates.append(v)
            elif "en-gb" in vid or "english (united kingdom)" in name:
                british_candidates.append(v)

        if british_candidates:
            self.engine.setProperty("voice", british_candidates[0].id)

        self.engine.setProperty("rate", 175)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text: str) -> None:
        """Speak a response with a more natural, warm tone."""
        if not text:
            return
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception:
            # As a fallback, print text to console
            print(text)

    # -------------------- Speech Input --------------------
    def _vosk_recognize(self, recognizer: "vosk.KaldiRecognizer | None", audio: sr.AudioData,
                       partial_ok: bool = False) -> str:
        if recognizer is None:
            return ""
        data = audio.get_raw_data(convert_rate=MIC_SAMPLE_RATE, convert_width=2)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result()).get("text", "")
        else:
            if not partial_ok:
                return ""
            result = json.loads(recognizer.PartialResult()).get("partial", "")
        return result.strip().lower()

    def _recognize(self, audio: sr.AudioData) -> str:
        """Try to recognize speech in English, then Bangla."""
        if USE_OFFLINE_STT and self._use_vosk_stt:
            return self._vosk_recognize(self._vosk_rec_full, audio, partial_ok=False)

        if not USE_GOOGLE_STT:
            return ""

        try:
            return self.recognizer.recognize_google(audio, language=LANG_PRIMARY)
        except sr.RequestError:
            return ""
        except Exception:
            try:
                return self.recognizer.recognize_google(audio, language=LANG_SECONDARY)
            except Exception:
                return ""

    def _wake_word_detected(self, audio: sr.AudioData) -> bool:
        if not self._use_vosk_wake:
            return False
        text = self._vosk_recognize(self._vosk_rec_wake, audio, partial_ok=True)
        if not text:
            return False
        words = set(text.split())
        return any(word in words for word in WAKE_WORDS)

    def listen_once(self, timeout: float | None = 5, phrase_limit: float | None = 7) -> str:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.6)
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            except sr.WaitTimeoutError:
                return ""
        text = self._recognize(audio)
        return text.strip().lower()

    # -------------------- Command Handling --------------------
    def _normalize_text(self, text: str) -> str:
        cleaned = text.strip().lower()
        cleaned = cleaned.translate(BN_DIGIT_TRANSLATION)
        cleaned = re.sub(r"[^\w\s./:~%+\-?&=]", " ", cleaned, flags=re.UNICODE)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned

    def _contains_wake_word(self, text: str) -> bool:
        words = set(text.split())
        return any(word in words for word in WAKE_WORDS)

    def _strip_wake_word(self, text: str) -> str:
        words = [w for w in text.split() if w not in WAKE_WORDS]
        return " ".join(words).strip()

    def _on_wake(self) -> None:
        if self.sleeping:
            self.sleeping = False
        self.speak(self._emotional_ack())
        cmd = self.listen_once(timeout=6, phrase_limit=8)
        if cmd:
            self._dispatch(cmd)

    def _emotional_ack(self) -> str:
        return random.choice([
            "Yes?",
            "I'm here.",
            "Ready when you are.",
            "How can I help?",
            "Right here.",
            "Go on.",
            "Listening.",
            "At your service.",
        ])

    def _emotional_done(self) -> str:
        return random.choice([
            "All done.",
            "Done.",
            "Sorted.",
            "Consider it handled.",
            "That's taken care of.",
            "Finished.",
            "As you wished.",
        ])

    def _emotional_error(self) -> str:
        return random.choice([
            "I hit a snag with that.",
            "Sorry, that didn't work.",
            "I ran into a problem doing that.",
            "I couldn't complete that just now.",
        ])

    def _emotional_clarify(self) -> str:
        return random.choice([
            "I didn't catch that. Try a simpler command.",
            "Sorry, I missed that. Say it a bit more clearly.",
            "I'm not sure I understood. Try again, please.",
        ])

    def _greeting(self) -> str:
        hour = _dt.datetime.now().hour
        if 5 <= hour < 12:
            day_part = "morning"
        elif 12 <= hour < 18:
            day_part = "afternoon"
        else:
            day_part = "evening"
        return f"Good {day_part}. {ASSISTANT_NAME} is ready."

    def handle_text(self, text: str) -> None:
        if not text:
            return
        text = self._normalize_text(text)
        if not text:
            return

        # Wake word gate
        if self.sleeping:
            if self._contains_wake_word(text):
                self._on_wake()
            return

        if self._contains_wake_word(text):
            remainder = self._strip_wake_word(text)
            if remainder:
                self._dispatch(remainder)
            else:
                self._on_wake()
            return

        # Direct command without wake word (optional)
        if ALLOW_DIRECT_COMMANDS:
            self._dispatch(text)

    def _dispatch(self, text: str) -> None:
        text = self._normalize_text(text)
        if not text:
            return
        no_done_handlers = {"sleep", "quit", "tell_time"}
        for pattern, handler_name in COMMAND_PATTERNS:
            match = re.match(pattern, text)
            if match:
                handler = getattr(self, handler_name, None)
                if handler:
                    try:
                        result = handler(*match.groups())
                        if handler_name not in no_done_handlers and result is not False:
                            self.speak(self._emotional_done())
                    except Exception as exc:
                        self.speak(self._emotional_error())
                    return
        # Fallback
        self.speak(self._emotional_clarify())

    # -------------------- Handlers --------------------
    def _has_cmd(self, name: str) -> bool:
        return shutil.which(name) is not None

    def _run_quiet(self, args: list[str]) -> bool:
        try:
            completed = subprocess.run(
                args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
            )
            return completed.returncode == 0
        except FileNotFoundError:
            return False

    def _resolve_path(self, raw: str) -> str:
        cleaned = raw.strip()
        alias = PATH_ALIASES.get(cleaned.lower()) or PATH_ALIASES.get(cleaned)
        path = alias if alias else cleaned
        path = os.path.expanduser(path)
        if path.startswith("."):
            return os.path.abspath(path)
        if os.path.isabs(path):
            return path
        return os.path.join(os.path.expanduser("~"), path)

    def _open_path(self, path: str) -> bool:
        return self._run_quiet(["xdg-open", path])

    def _clamp_percent(self, value: int) -> int:
        return max(0, min(100, value))

    def open_app(self, name: str) -> None:
        name = name.strip().lower()
        if name in ("browser", "internet"):
            webbrowser.open("https://www.google.com")
            return

        cmd = APPS.get(name)
        system = platform.system().lower()

        if system == "windows":
            os.startfile(name)  # type: ignore[attr-defined]
            return

        if not cmd:
            # Try to run as-is
            cmd = name

        subprocess.Popen([cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def web_search(self, query: str) -> None:
        url = "https://www.google.com/search?q=" + _url.quote(query)
        webbrowser.open(url)

    def open_url(self, url: str) -> None:
        if not re.match(r"^https?://", url):
            url = "https://" + url
        webbrowser.open(url)

    def open_site(self, name: str) -> bool:
        key = name.strip().lower()
        url = SITES.get(key)
        if not url:
            url = SITES.get(key.replace(" ", ""))
        if not url:
            self.open_url(key)
            return True
        webbrowser.open(url)
        return True

    def open_folder(self, name: str) -> bool:
        path = self._resolve_path(name)
        if not os.path.isdir(path):
            self.speak("I couldn't find that folder.")
            return False
        if not self._open_path(path):
            self.speak("I couldn't open that folder.")
            return False
        return True

    def open_file(self, name: str) -> bool:
        path = self._resolve_path(name)
        if not os.path.exists(path):
            self.speak("I couldn't find that file.")
            return False
        if not self._open_path(path):
            self.speak("I couldn't open that file.")
            return False
        return True

    def create_folder(self, name: str) -> bool:
        path = self._resolve_path(name)
        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            self.speak("I couldn't create that folder.")
            return False
        return True

    def type_text(self, text: str) -> bool:
        if pyautogui is None:
            self.speak("Keyboard control is not available. Install pyautogui first.")
            return False
        pyautogui.typewrite(text)
        return True

    def press_key(self, key: str) -> bool:
        if pyautogui is None:
            self.speak("Keyboard control is not available. Install pyautogui first.")
            return False
        key = key.strip().lower()
        if key in KEY_ALIASES:
            pyautogui.press(KEY_ALIASES[key])
            return True

        parts = [p for p in re.split(r"[ +]+", key) if p]
        if not parts:
            return False
        parts = [KEY_ALIASES.get(p, p) for p in parts]
        if len(parts) > 1:
            pyautogui.hotkey(*parts)
        else:
            pyautogui.press(parts[0])
        return True

    def window_next(self) -> bool:
        if self._run_quiet(["xdotool", "key", "alt+Tab"]):
            return True
        if pyautogui is not None:
            pyautogui.hotkey("alt", "tab")
            return True
        self.speak("Window switching isn't available.")
        return False

    def window_prev(self) -> bool:
        if self._run_quiet(["xdotool", "key", "alt+Shift+Tab"]):
            return True
        if pyautogui is not None:
            pyautogui.hotkey("alt", "shift", "tab")
            return True
        self.speak("Window switching isn't available.")
        return False

    def volume_up(self) -> bool:
        if self._run_quiet(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"]):
            return True
        if self._run_quiet(["amixer", "-D", "pulse", "sset", "Master", "5%+"]):
            return True
        self.speak("Volume control isn't available.")
        return False

    def volume_down(self) -> bool:
        if self._run_quiet(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"]):
            return True
        if self._run_quiet(["amixer", "-D", "pulse", "sset", "Master", "5%-"]):
            return True
        self.speak("Volume control isn't available.")
        return False

    def set_volume(self, value: str) -> bool:
        try:
            percent = int(value)
        except ValueError:
            return False
        percent = self._clamp_percent(percent)
        if self._run_quiet(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{percent}%"]):
            return True
        if self._run_quiet(["amixer", "-D", "pulse", "sset", "Master", f"{percent}%"]):
            return True
        self.speak("Volume control isn't available.")
        return False

    def mute_volume(self) -> bool:
        if self._run_quiet(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "1"]):
            return True
        if self._run_quiet(["amixer", "-D", "pulse", "sset", "Master", "mute"]):
            return True
        self.speak("Volume control isn't available.")
        return False

    def unmute_volume(self) -> bool:
        if self._run_quiet(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "0"]):
            return True
        if self._run_quiet(["amixer", "-D", "pulse", "sset", "Master", "unmute"]):
            return True
        self.speak("Volume control isn't available.")
        return False

    def brightness_up(self) -> bool:
        if self._run_quiet(["brightnessctl", "set", "+10%"]):
            return True
        if self._run_quiet(["brightnessctl", "set", "10%+"]):
            return True
        if self._run_quiet(["xbacklight", "-inc", "10"]):
            return True
        self.speak("Brightness control isn't available.")
        return False

    def brightness_down(self) -> bool:
        if self._run_quiet(["brightnessctl", "set", "10%-"]):
            return True
        if self._run_quiet(["brightnessctl", "set", "-10%"]):
            return True
        if self._run_quiet(["xbacklight", "-dec", "10"]):
            return True
        self.speak("Brightness control isn't available.")
        return False

    def set_brightness(self, value: str) -> bool:
        try:
            percent = int(value)
        except ValueError:
            return False
        percent = self._clamp_percent(percent)
        if self._run_quiet(["brightnessctl", "set", f"{percent}%"]):
            return True
        if self._run_quiet(["xbacklight", "-set", str(percent)]):
            return True
        self.speak("Brightness control isn't available.")
        return False

    def write_note(self, content: str) -> None:
        notes_path = os.path.join(os.path.dirname(__file__), "notes.txt")
        timestamp = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {content}\n"
        with open(notes_path, "a", encoding="utf-8") as f:
            f.write(line)

    def tell_time(self) -> None:
        now = _dt.datetime.now().strftime("%I:%M %p")
        self.speak(f"It's {now}.")

    def sleep(self) -> None:
        self.sleeping = True
        self.speak("Going quiet. Say Mike to wake me.")

    def quit(self) -> None:
        self.running = False
        self.speak("Goodbye.")

    # -------------------- Run Loop --------------------
    def _bg_callback(self, recognizer: sr.Recognizer, audio: sr.AudioData) -> None:
        with self._lock:
            if self._use_vosk_wake:
                if self._wake_word_detected(audio):
                    now = time.time()
                    if now - self._last_wake_time >= WAKE_COOLDOWN_SECONDS:
                        self._last_wake_time = now
                        self._speech_queue.put("__WAKE__")
                elif ALLOW_DIRECT_COMMANDS:
                    try:
                        text = self._recognize(audio)
                    except Exception:
                        text = ""
                    if text:
                        self._speech_queue.put(text.lower())
                return

            try:
                text = self._recognize(audio)
            except Exception:
                text = ""
            if text:
                self._speech_queue.put(text.lower())

    def run(self) -> None:
        self.speak(self._greeting())
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.8)

        stop_bg = self.recognizer.listen_in_background(self.microphone, self._bg_callback)

        try:
            while self.running:
                try:
                    text = self._speech_queue.get(timeout=0.5)
                    if text == "__WAKE__":
                        self._on_wake()
                    else:
                        self.handle_text(text)
                except queue.Empty:
                    continue
        finally:
            stop_bg(wait_for_stop=False)


if __name__ == "__main__":
    assistant = MikeAssistant()
    try:
        assistant.run()
    except KeyboardInterrupt:
        assistant.speak("Shutting down.")
