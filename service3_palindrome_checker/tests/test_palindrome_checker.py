import unittest
import asyncio  
from main import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_is_palindrome(self):
        # Utilize asyncio.run para executar a função assíncrona
        self.assertTrue(asyncio.run(is_palindrome(121)))
        self.assertFalse(asyncio.run(is_palindrome(123)))

if __name__ == '__main__':
    unittest.main()
