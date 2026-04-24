🔒 AES File Encryption Project
A Python project demonstrating AES-256 file encryption and decryption using the cryptography library. The program encrypts a user-provided message with a randomly generated key and IV, saves the ciphertext to a file, then reads it back and decrypts it — simulating a real secure file encryption workflow.

📌 Overview
This project showcases:

AES-256-CBC symmetric encryption
PKCS7 padding for block-size alignment
Random key and IV generation using os.urandom
Base64 encoding for safe text representation of binary data
File I/O — writing encrypted output and reading it back for decryption


📁 Project Structure
AES_File_Encryption_Project/
├── secure_crypto.py     # Main script: encrypt, decrypt, file I/O
├── encrypted.txt        # Output: Base64-encoded ciphertext (generated on run)
└── decrypted.txt        # Output: Recovered plaintext (generated on run)

⚙️ How It Works
Step-by-step flow
User Input (plaintext message)
         ↓
Generate random 256-bit AES Key + 128-bit IV
         ↓
PKCS7 Pad the message to AES block size (128-bit)
         ↓
AES-CBC Encrypt → raw ciphertext bytes
         ↓
Base64 encode → save to encrypted.txt
         ↓
Read encrypted.txt → Base64 decode → raw ciphertext
         ↓
AES-CBC Decrypt → remove PKCS7 padding → plaintext
         ↓
Save recovered plaintext to decrypted.txt
Key design choices
ChoiceDetailAlgorithmAES (Advanced Encryption Standard)Key size256-bit (os.urandom(32))ModeCBC (Cipher Block Chaining)IV size128-bit (os.urandom(16))PaddingPKCS7 (block size 128 bits)EncodingBase64 for file-safe storage

Note: The key and IV are generated fresh each run and printed to the console. They are not persisted — this is intentional for demonstration purposes.


🚀 Getting Started
Prerequisites

Python 3.7+
cryptography library

Install dependencies
bashpip install cryptography
Run the script
bashpython secure_crypto.py
You will be prompted to enter a message:
Enter your message: Hello, this is a secret!

--- ENCRYPTION PROCESS ---
Generated AES Key (Base64): <base64-key>
Generated IV (Base64): <base64-iv>
Encrypted Ciphertext (Base64): <base64-ciphertext>
Encrypted message saved to 'encrypted.txt'

--- DECRYPTION PROCESS ---
Decrypted Message: Hello, this is a secret!
Decrypted message saved to 'decrypted.txt'

🧩 Code Walkthrough
encrypt_message(message, key, iv)

Applies PKCS7 padding to the plaintext so its length is a multiple of 16 bytes
Creates an AES-CBC cipher with the provided key and IV
Returns raw ciphertext bytes

decrypt_message(ciphertext, key, iv)

Creates an AES-CBC cipher in decryption mode
Decrypts the ciphertext and strips PKCS7 padding
Returns the original plaintext string

simulate_secure_file_encryption()

Orchestrates the full end-to-end flow:

Prompts for user input
Generates a cryptographically random key and IV
Encrypts the message and saves Base64 output to encrypted.txt
Reads encrypted.txt, decrypts, and saves result to decrypted.txt




🛡️ Security Notes

os.urandom is used for key and IV generation — this is cryptographically secure.
CBC mode requires a unique IV per encryption operation. This project correctly generates a fresh IV each run.
The key and IV are printed to the console for demonstration. In a real application, these must be securely stored or exchanged (e.g., via key derivation from a password using PBKDF2 or Argon2, or asymmetric key exchange).
This project does not implement authentication (e.g., HMAC or GCM mode). For production use, consider AES-GCM which provides both encryption and integrity verification.


📚 Dependencies
PackagePurposecryptographyAES cipher, padding, and backend primitives

💡 Possible Extensions

Replace CBC with AES-GCM for authenticated encryption
Derive the AES key from a user password using PBKDF2 or scrypt
Encrypt entire files (binary), not just text messages
Add a CLI interface with argparse for encrypt/decrypt modes
Persist the key and IV securely alongside the encrypted file


📄 License
This project is open for learning and experimentation. Feel free to fork and build upon it.
