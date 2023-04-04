import random
from typing import Tuple


class RSA:
    """
    A class that implements the RSA algorithm.

    Usage:
        # Create a new RSA object with a key bit size of 1024 bits.
        rsa = RSA(key_size=1024)

        # Encrypt a message using the public key.
        crypto = rsa.encrypt("Hello, world!")

        # Decrypt the crypto using the private key.
        message = rsa.decrypt(crypto)
    """

    def __init__(self, key_size: int = 512):
        self._public_key, self._private_key = self.generate_keys(key_size)

    def _n_bit_random(self, n: int) -> int:
        """
        Returns a random integer with n bits.
        """
        return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)

    def _miller_rabin(self, n: int) -> bool:
        """
        Returns True if n is probably prime, False if n is composite.
        """
        k = 20
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        # Perform k rounds of the Miller-Rabin test
        for _ in range(20):  # Adjust the number of rounds for higher accuracy
            a = random.randrange(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def _gen_prime_number(self, n: int):
        """
        Generates a prime number of n bits using the Miller-Rabin primality test.
        """
        while True:
            num = self._n_bit_random(n)
            if self._miller_rabin(num):
                return num

    def _gcd(self, a, b):
        """
        Returns the greatest common divisor of a and b.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def generate_keys(self, b: int) -> (int, int):
        """
        Generates a public/private keypair for the RSA algorithm.
        """
        p, q = self._gen_prime_number(b), self._gen_prime_number(b)
        n, m = p * q, (p - 1) * (q - 1)

        e = random.randrange(1, m)
        while self._gcd(e, m) != 1:
            e = random.randrange(1, m)

        d = pow(e, -1, m)
        return (e, n), (d, n)

    def encrypt(self, message, public_key):
        """
        Encrypts the message using the public key.
        """
        e, n = public_key
        crypto = [pow(ord(char), e, n) for char in message]
        return crypto

    def decrypt(self, crypto, private_key):
        """
        Decrypts the crypto using the private key.
        """
        d, n = private_key
        plaintext = [chr(pow(char, d, n)) for char in crypto]
        return ''.join(plaintext)

    def get_public_key(self) -> Tuple[int, int]:
        """
        Returns the RSA public key as a tuple of (n, e).
        """
        return self._public_key

    def get_private_key(self) -> Tuple[int, int]:
        """
        Returns the RSA private key as a tuple of (d, n).
        """
        return self._private_key
