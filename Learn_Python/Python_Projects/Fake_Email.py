import random
import time
def generate_email():
    domains = ["gmail.com"]
    letters = "abcdefghijklmnopqrstuvwxyz"
    name_length = random.randint(5, 10)
    name = ''.join(random.choice(letters) for _ in range(name_length))
    domain = random.choice(domains)
    number = random.randint(1000, 9999)
    email = f"{name}{number}@{domain}"
    return email

# Example usage
for _ in range(100):
    print(generate_email())
    # time.sleep()  # Sleep for 1 second between generating emails