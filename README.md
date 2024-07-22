# SuckSCrypt

A Fastest & Secure Encryption System.

## Installation

You can install SuckSCrypt via pip:

```bash
pip install SuckSCrypt
```

## Example Uses

```python
from suckscrypt import core

# Example usage of the SuckSCrypt
key, salt = core.generate_key()
plaintext = b'Wow, SuckSCrypt is very Secure.'

# Enc
encrypted_text = core.sucks_encrypt(key, plaintext)
print(f'Encrypted text: {encrypted_text.hex()}')

# Dec
decrypted_text = core.sucks_decrypt(key, encrypted_text)
print(f'Decrypted text: {decrypted_text.decode()}')
```

