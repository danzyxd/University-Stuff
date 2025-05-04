def is_prime(num):
    for i in range(2, round((num)**0.5) + 1):
        if num % i == 0:
            return False
    return True

def my_xor(text, key):
    key_str = str(key)
    return "".join(chr(ord(c) ^ ord(key_str[i % len(key_str)])) for i, c in enumerate(text))


# c = 0
# for i in range(500_000, 1_000_000):
#     if is_prime(i):
#         c+=1
