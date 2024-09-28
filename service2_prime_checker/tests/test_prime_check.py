import unittest
import asyncio  # Importe o módulo asyncio
from main import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_is_prime(self):
        # Utilize asyncio.run para executar a função assíncrona
        self.assertTrue(asyncio.run(is_prime(7)))
        self.assertFalse(asyncio.run(is_prime(8)))

if __name__ == '__main__':
    unittest.main()
