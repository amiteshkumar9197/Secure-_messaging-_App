from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES
from Crypto.Random import get_random_bytes
import base64

# Padding for DES (since DES requires data in 8-byte blocks)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Generate RSA key pair (for receiver)
receiver_key = RSA.generate(2048)
receiver_public_key = receiver_key.publickey()

# Simulate Sender encrypting a DES key using Receiver's public RSA key
des_key = get_random_bytes(8)  # DES uses 8-byte key
rsa_cipher = PKCS1_OAEP.new(receiver_public_key)
encrypted_des_key = rsa_cipher.encrypt(des_key)

# Receiver decrypts DES key using their private RSA key
rsa_decipher = PKCS1_OAEP.new(receiver_key)
decrypted_des_key = rsa_decipher.decrypt(encrypted_des_key)

# --- Messaging Simulation ---
# Sender encrypts message using DES
message = input("enter the message")
des_cipher = DES.new(des_key, DES.MODE_ECB)
padded_message = pad(message)
encrypted_msg = des_cipher.encrypt(padded_message.encode())

# Receiver decrypts message using the same DES key
des_decipher = DES.new(decrypted_des_key, DES.MODE_ECB)
decrypted_msg = des_decipher.decrypt(encrypted_msg).decode().strip()

# --- Outputs ---
print("Original Message: ", message)
print("Encrypted DES Key (Base64): ", base64.b64encode(encrypted_des_key).decode())
print("Encrypted Message (Base64):", base64.b64encode(encrypted_msg).decode())
print("Decrypted Message: ", decrypted_msg)
