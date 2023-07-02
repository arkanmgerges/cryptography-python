"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.caesar_cipher import *


def test_encrypt_and_decrypt_with_key_offset_3():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    ciphertext = encrypt(3, plaintext)
    assert plaintext == decrypt(3, ciphertext)

def test_encrypt_and_decrypt_with_key_offset_30():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    ciphertext = encrypt(30, plaintext)
    assert plaintext == decrypt(30, ciphertext)

def test_encrypt_and_decrypt_with_key_offset_100():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    ciphertext = encrypt(100, plaintext)
    assert plaintext == decrypt(100, ciphertext)

def test_encrypt_and_decrypt_with_different_keys():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    ciphertext = encrypt(100, plaintext)
    assert plaintext != decrypt(30, ciphertext)