# LockBoxPy - A Python Obfuscator and Encryptor that uses AES, RSA and PyArmor

LockBoxPy is a software tool that encrypts a payload and creates an executable file. The tool uses RSA encryption to encrypt an AES key, which is then used to encrypt the payload using AES encryption. The resulting encrypted AES key and encrypted payload are then combined to create an executable file. The tool also obfuscates the executable file using PyArmor for added security.

## Installation

To use LockBoxPy, you must have Python 3.x installed on your system. You can download Python from the official website at https://www.python.org/downloads/.

You will also need to install the following packages:

    cryptography
    tk
    pyarmor

You can install these packages using pip:

```
pip install cryptography tk pyarmor
```

## Working

1. LockBoxPy works by encrypting the payload file using AES encryption with a randomly generated key.
2. The key is then encrypted using RSA encryption with a public key, and both the encrypted key and the encrypted payload are embedded in a Python script stub.
3. When the obfuscated executable is executed, the script stub is decrypted and executed.
4. The script then decrypts the AES key using RSA decryption with a private key, and uses the decrypted key to decrypt the payload.
5. The decrypted payload is then executed.
6. Enjoy!

This process ensures that the payload file remains encrypted and cannot be accessed without the private key, providing an additional layer of security. The obfuscation of the executable also helps to prevent reverse engineering and tampering.

## Usage

To use LockBoxPy, simply run the LockBoxPy.py file. This will launch a GUI window that allows you to select the payload file that you want to encrypt. Once you have selected the file, click the "Encrypt Payload" button to encrypt the payload and create the executable.

To use LockBoxPy, run the following command:

```python
python3 LockBoxPy.py
```

### Note:

For the next step, use only `combined.py` file generated in `dist` directory only. The reason to do is because the file in the `dist` directory is the obfuscated version of the malware whereas the `combined.py` file generated outside the `dist` directory is only an encrypted malware file.

## Python to EXE Converter

### Overview

This is a simple Python script that converts a Python file (.py) into an executable file (.exe) using PyInstaller.

### Installation

This script requires Python and PyInstaller to be installed on the system.

To install `PyInstaller`, run the following command:

`pip install pyinstaller`

### Steps to run it:

1. Run the `py_to_exe.py` file
2. Select the `combined.py` - Python file from the `dist` directory which is created after the obfuscation.
3. Click the "Convert to EXE" button.
4. The resulting executable file will be saved in the same directory as the Python file (`dist` directory).

### Note:

The encrypted executable will be saved as in the same directory as the LockBoxPy.py file.

- UD = Under Development
