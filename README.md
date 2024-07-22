# SuckSCrypt

A Fastest & Secure Encryption System.

## Installation

You can install SuckSCrypt via pip:

```bash
pip install SuckSCrypt
```

## Example Uses

```python
rom suckscrypt.core import generate_key, sucks_encrypt, sucks_decrypt

# generate keyy and salt
key, salt = generate_key()

# enc
plaintext = b'Wow, SuckSCrypt is very secure.'
encrypted_text = sucks_encrypt(key, plaintext)

# dec
decrypted_text = sucks_decrypt(key, encrypted_text)

print(f'Encrypted text (hex): {encrypted_text.hex()[:20]}...')
print(f'Decrypted text: {decrypted_text.decode()}')
```

