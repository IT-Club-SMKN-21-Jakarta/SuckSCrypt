# tests/test_core.py
import unittest
from core import generate_key, sucks_encrypt, sucks_decrypt

class TestSuckSCrypt(unittest.TestCase):
    def setUp(self):
        self.key, self.salt = generate_key()
        self.plaintext = b'Wow, SuckSCrypt is very secure.'
        
    def test_encryption_decryption(self):
        encrypted_text = sucks_encrypt(self.key, self.plaintext)
        decrypted_text = sucks_decrypt(self.key, encrypted_text)
        self.assertEqual(self.plaintext, decrypted_text)

if __name__ == '__main__':
    unittest.main()