"""
:author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


def encrypt(offset: int, plaintext: str):
    key_map = generate_key(offset)
    result = ""
    for c in plaintext:
        if c in key_map:
            result += key_map[c]
        else:
            result += c
    return result


def decrypt(offset: int, plaintext: str):
    key_map = generate_decryption_key(offset)
    result = ""

    for c in plaintext:
        if c in key_map:
            result += key_map[c]
        else:
            result += c
    return result


def generate_key(offset: int):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    key = {}
    count = 0
    letters_len = len(letters)
    for c in letters:
        key[c] = letters[(count + offset) % letters_len]
        count += 1
    return key


def generate_decryption_key(offset: int):
    key = generate_key(offset)
    return {v: k for k, v in key.items()}
