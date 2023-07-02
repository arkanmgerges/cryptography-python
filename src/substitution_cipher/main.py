"""
:author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import secrets



def encrypt(key: dict, plaintext: str):
    result = ""
    for c in plaintext:
        if c in key:
            result += key[c]
        else:
            result += c
    return result

def decrypt(key: dict, ciphertext: str):
    result = ""
    decryption_key = generate_decrypt_key(key)
    for c in ciphertext:
        if c in decryption_key:
            result += decryption_key[c]
        else:
            result += c
    return result

def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    tmp_letters = list(letters)
    key = {}
    for c in letters:
        key[c] = secrets.choice(tmp_letters)
        tmp_letters.remove(key[c])
    return key

def generate_decrypt_key(key: dict):
    return {v:k for k, v in key.items()}