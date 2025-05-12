from random import randint

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
    with open("./AmTCD.ini", "r", encoding="utf-8") as file:
        text = file.read()
        lines = text.split("\n")
        key = int(lines[1][10:])
    return key

def encrypt(text):
    key = load_key()
    new_key = generate_new_key()
    combined_key = key * new_key
    encrypted_text = my_xor(text, new_key)
    return f"[main]\nkeyopen = {combined_key}\nmess = {encrypted_text}"

def decrypt(text):
    key = load_key()
    lines = text.split("\n")
    if len(lines) < 3:
        raise ValueError("Неверный формат файла!")
    combined_key = int(lines[1][10:])
    encrypted_text = lines[2][7:]
    for additional_lines in range(4, len(lines)):
        encrypted_text = lines[additional_lines]
    new_key = combined_key // key
    return my_xor(encrypted_text, new_key)