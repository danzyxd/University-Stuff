from random import randint
import configparser

def is_prime(num):
    for i in range(2, round((num)**0.5) + 1):
        if num % i == 0:
            return False
    return True

def my_xor(text, key):
    key_str = str(key)
    return "".join(chr(ord(c) ^ ord(key_str[i % len(key_str)])) for i, c in enumerate(text))

def generate_new_key():
    while True:
        new_key = randint(500_000, 1_000_000)
        if is_prime(new_key):
            return new_key

def load_key():
    config = configparser.ConfigParser()
    config.read("AmTCD.ini")
    key = int(config.get("main", "keyuser"), 16)
    return key

def encrypt(text):
    key = load_key()
    new_key = generate_new_key()
    combined_key = key * new_key
    encrypted_text = my_xor(text, new_key)
    return f"{combined_key}\n{encrypted_text}"

def decrypt(text):
    key = load_key()
    lines = text.split("\n", 1)
    if len(lines) < 2:
        raise ValueError("Неверный формат файла!")
    combined_key = int(lines[0])
    encrypted_text = lines[1]
    new_key = combined_key // key
    return my_xor(encrypted_text, new_key)