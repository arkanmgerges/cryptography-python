"""
:author: Arkan M. Gerges<arkan.m.gerges@gmail.com>

The Linear Congruential Generator (LCG) is a simple pseudorandom number generator.
`See <https://en.wikipedia.org/wiki/Linear_congruential_generator>`_
"""
class Lcg:    
    def __init__(self, seed: int = 1):
        self._next = seed
        self._modulus = 2 ** 31
    
    def next_number(self) -> int:
        # The following numbers were taken from the Wikipedia article on LCGs (see the link above), and uses the ANSI C parameters.
        self._next = (1103515245 * self._next + 12345) % self._modulus
        return self._next
    
    def next_number_mod_256(self) -> int:
        return self.next_number() % 256
    
def process(key: Lcg, message: bytes) -> bytes:
    return bytes([message[i] ^ key.next_number_mod_256() for i in range(len(message))])
