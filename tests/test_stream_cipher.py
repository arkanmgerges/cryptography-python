"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest
from src.stream_cipher import *


def test_encrypt_and_decrypt_are_equal():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    key = Lcg(10)
    ciphertext = process(key, bytes(plaintext.encode()))
    key = Lcg(10)
    assert plaintext == process(key, ciphertext).decode()

def test_encrypt_and_decrypt_are_not_equal_when_keys_are_different():
    plaintext = "This is a secret and you should not be able to read it 0123456789!@#$%^&*()_+{}[]|\\:;\"',./<>?`~"
    key = Lcg(10)
    ciphertext = process(key, bytes(plaintext.encode()))
    key = Lcg(11)
    with pytest.raises(UnicodeDecodeError):
        assert plaintext == process(key, ciphertext).decode()