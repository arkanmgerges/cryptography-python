"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.substitution_cipher import *


def test_encrypt_and_decrypt_are_equal():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    key = generate_key()
    ciphertext = encrypt(key, plaintext)
    assert plaintext == decrypt(key, ciphertext)

def test_encrypt_and_decrypt_are_not_equal():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    key = generate_key()
    key2 = generate_key()
    ciphertext = encrypt(key, plaintext)
    assert plaintext != decrypt(key2, ciphertext)

