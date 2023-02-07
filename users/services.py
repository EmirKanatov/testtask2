import random
import string

characters = list(string.ascii_letters + string.digits + "1234567890!@#$%^&*()")


def generate_random_password(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)
