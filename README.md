
![image](https://github.com/user-attachments/assets/bce7a65a-0a85-4069-831d-a128dcb33911)
# Secure Messaging App

This is a simple secure messaging application implemented in Python that demonstrates hybrid encryption using RSA and DES algorithms. The app simulates secure message exchange by encrypting a DES key with RSA and then using the DES key to encrypt the actual message.
## Features
- Generates RSA key pair for secure key exchange.
- Uses RSA to encrypt and decrypt the DES symmetric key.
- Encrypts and decrypts messages using DES encryption.
- Demonstrates hybrid encryption combining asymmetric and symmetric cryptography.

## Installation

This project requires Python 3 and the `pycryptodome` library. You can install the library using pip:
pip install pycryptodome
## Usage

Run the script using Python
python secure_messaging_app.py
You will be prompted to enter a message. The script will then:

- Encrypt the message using DES with a randomly generated key.
- Encrypt the DES key using RSA.
- Decrypt the DES key using RSA.
- Decrypt the message using DES.
- Display the original message, encrypted DES key, encrypted message, and decrypted message.

## How It Works

1. The receiver generates an RSA key pair (public and private keys).
2. The sender generates a random DES key.
3. The sender encrypts the DES key using the receiver's RSA public key.
4. The sender encrypts the message using the DES key.
5. The receiver decrypts the DES key using their RSA private key.
6. The receiver decrypts the message using the decrypted DES key.

This hybrid approach leverages the security of RSA for key exchange and the efficiency of DES for message encryption.

## License

This project is open source and available under the MIT License.

## Author

Created by @Amitesh kumar choudhary
