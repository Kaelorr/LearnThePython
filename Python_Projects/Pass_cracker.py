import random
import string
import time

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def crack_password(password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    while True:
        attempts += 1
        guess = ''.join(random.choice(characters) for _ in range(len(password)))
        if guess == password:
            return attempts
if __name__ == "__main__":
    password_length = 16
    password = generate_password(password_length)
    print(f"Generated Password: {password}")
    attempts = crack_password(password)
    print(f"Password cracked in {attempts} attempts!") 