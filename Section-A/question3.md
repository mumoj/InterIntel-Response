# Encryption/Hashing Methods.

## (i) One Way Method -  Hashing(SHA-256)
SHA stands for Secure Hash Algorithm. Cryptographic hash functions are designed to produce irreversible and unique hashes.
Irreversible means you can't derive the original data from the hash and unique means that two different data item produce 
two different hash values. SHA-256 is deterministic in such a way that given the same piece of data it would produce 
the same hash value over and over again. Such property makes it ideal for generating signatures to authenticate 
data items.
 
```python
"""An example implementation of  SHA-256  using the  hashlib library."""

import hashlib


def encrypt_script(string):
    hash_value = hashlib.sha256(string.encode()).hexdigest()
    return hash_value

# Example code
print(encrypt_script(string="Garbage In Garbage Out."))
# b5146064da5e3b3a239b5268b78b4b940e4611a0677c00c326a5965f16087183
``` 
 
 
## (ii) Two Way Method - Symmetric Encryption(AES).
 Symmetric encryption uses one key to both encrypt and decrypt data. AES stands for Advanced Encryption Standard. It 
 uses a 128 bit key to encrypt information into an undecipherable cipher-text which can only be decrypted by that key.
   
Python example:

```python

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        """Pad text to  make it a multiple of the 128 bit block"""
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        """Remove extra padded text to complete decryption"""
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

# Example code
cipher = AESCipher(key='alas')
cipher.encrypt('Garbage In Garbage Out')
# '4fHBBSrK/8MX7EJEZb2hLbwMS4/xsXR7XIQ8pF3OI9rgthfk//0Hx7rpkYYk1ZYn'
cipher.decrypt('4fHBBSrK/8MX7EJEZb2hLbwMS4/xsXR7XIQ8pF3OI9rgthfk//0Hx7rpkYYk1ZYn')
# 'Garbage In Garbage Out'
```
 
 


