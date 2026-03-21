"""
Loops Practice (For + While)

Definition of for loop: used to iterate over a sequence (list, tuple, string)
or any iterable object. Iterating over a sequence is called traversal.
Definition of while loop: used to execute a block of code repeatedly as long as
its condition is True.
"""

# =========================
# Basics: for loop traversal
# =========================

numbers = [1, 2, 3, 4, 5]
letters = "abc"

# Nested loops
for num in numbers:
    for letter in letters:
        print(num, letter)

# Range
for num in range(1, 11):
    print(num)

# Enumerate (index + value)
for idx, num in enumerate(numbers, start=1):
    print(f"Index {idx}: {num}")

# Zip (pair two lists)
colors = ["red", "green", "blue", "yellow", "purple"]
for num, color in zip(numbers, colors):
    print(num, color)

# =========================
# Control flow: continue/break/else
# =========================

for num in numbers:
    if num == 3:
        continue
    print("continue ->", num)

for num in numbers:
    if num == 3:
        break
    print("break ->", num)

# for/else executes else if loop did NOT break
for num in numbers:
    if num == 99:
        break
else:
    print("for/else -> loop ended without break")

# =========================
# While loop examples
# =========================

x = 0
while x < 5:
    print("while ->", x)
    x += 1

# Sentinel while loop (non-interactive example)
items = ["apple", "banana", "", "mango"]
idx = 0
while idx < len(items):
    if items[idx] == "":
        break
    print("item ->", items[idx])
    idx += 1

# =========================
# Comprehensions & generators
# =========================

squares = [n * n for n in range(1, 11)]
print("squares ->", squares)

even_squares = [n * n for n in range(1, 21) if n % 2 == 0]
print("even squares ->", even_squares)

square_gen = (n * n for n in range(1, 6))
for val in square_gen:
    print("gen ->", val)

# =========================
# Mini Projects (Advanced Practice)
# =========================

def multiplication_table(n, upto=10):
    """Return a multiplication table (list of strings)."""
    lines = []
    for i in range(1, upto + 1):
        lines.append(f"{n} x {i} = {n * i}")
    return lines


def prime_sieve(limit):
    """Generate all primes up to limit (Sieve of Eratosthenes)."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def fibonacci(n):
    """Return first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def word_frequency(text):
    """Count word frequency (case-insensitive, basic split)."""
    freq = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:")
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq


def longest_word(text):
    """Find the longest word in a sentence."""
    longest = ""
    for word in text.split():
        clean = word.strip(".,!?;:")
        if len(clean) > len(longest):
            longest = clean
    return longest


def collatz_sequence(start):
    """Return Collatz sequence until it reaches 1."""
    seq = [start]
    n = start
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


# =========================
# Interactive Mini Projects
# =========================

RUN_INTERACTIVE = False


def name_greeting_loop():
    """Ask for names until empty input."""
    while True:
        name = input("Enter your name (empty to stop): ").strip()
        if name == "":
            break
        print("Hello, " + name)


def number_guessing_game():
    """Simple guessing game with a fixed secret for practice."""
    secret = 7
    attempts = 0
    while True:
        guess = input("Guess a number (1-10, 'q' to quit): ").strip()
        if guess.lower() == "q":
            print("Goodbye!")
            break
        if not guess.isdigit():
            print("Please enter a number.")
            continue
        attempts += 1
        guess = int(guess)
        if guess == secret:
            print(f"Correct! Attempts: {attempts}")
            break
        if guess < secret:
            print("Too low")
        else:
            print("Too high")


# =========================
# Demo calls (non-interactive)
# =========================

print("table ->")
for line in multiplication_table(7, upto=5):
    print(line)

print("primes ->", prime_sieve(30))
print("fibonacci ->", fibonacci(10))

text = "Loops make code powerful. Loops make repetition easy!"
print("freq ->", word_frequency(text))
print("longest ->", longest_word(text))
print("collatz ->", collatz_sequence(6))

if RUN_INTERACTIVE:
    name_greeting_loop()
    number_guessing_game()
