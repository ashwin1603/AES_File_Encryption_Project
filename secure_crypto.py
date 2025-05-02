from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

def encrypt_message(message, key, iv):
    # Add padding to make the message a multiple of block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    # Create AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_message(ciphertext, key, iv):
    # Create AES Cipher for decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted_data.decode()

def simulate_secure_file_encryption():
    # Step 1: User input
    message = input("Enter your message: ")

    print("\n--- ENCRYPTION PROCESS ---")
    
    # Step 2: Generate random key and IV
    key = os.urandom(32)  # 256-bit AES key
    iv = os.urandom(16)   # 128-bit IV

    print(f"Generated AES Key (Base64): {b64encode(key).decode()}")
    print(f"Generated IV (Base64): {b64encode(iv).decode()}")

    # Step 3: Encrypt the message
    ciphertext = encrypt_message(message, key, iv)
    encoded_ciphertext = b64encode(ciphertext).decode()
    print(f"Encrypted Ciphertext (Base64): {encoded_ciphertext}")

    # Step 4: Save encrypted text to file
    with open("encrypted.txt", "w") as f:
        f.write(encoded_ciphertext)
    print("Encrypted message saved to 'encrypted.txt'")

    print("\n--- DECRYPTION PROCESS ---")

    # Step 5: Read encrypted message from file
    with open("encrypted.txt", "r") as f:
        file_data = f.read()

    loaded_ciphertext = b64decode(file_data)

    # Step 6: Decrypt the message
    decrypted_message = decrypt_message(loaded_ciphertext, key, iv)
    print(f"Decrypted Message: {decrypted_message}")

    # Step 7: Save decrypted text to file
    with open("decrypted.txt", "w") as f:
        f.write(decrypted_message)
    print("Decrypted message saved to 'decrypted.txt'")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    simulate_secure_file_encryption()
