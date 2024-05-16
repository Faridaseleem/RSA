# RSA
implementation of RSA python code
RSA Encryption in Python
This Python program implements a simple RSA encryption and decryption system. RSA (Rivest-Shamir-Adleman) is a widely used asymmetric cryptographic algorithm that uses a pair of keys: a public key for encryption and a private key for decryption. This implementation includes key generation, encryption, and decryption functions.

Features
Prime Number Generation: Generates prime numbers within a specified range.
Key Generation: Generates RSA public and private key pairs.
Encryption: Encrypts a plaintext message using the public key.
Decryption: Decrypts an encrypted message using the private key.
ASCII Conversion: Converts encrypted numerical values to a readable ASCII format.
Requirements
Python 3.x
random module (part of the standard library)
math module (part of the standard library)
Example Interaction
The program will generate a pair of public and private keys.
You will be prompted to enter a plaintext message.
The program will output the encrypted message in an ASCII format.
The program will then decrypt the message and display the original plaintext.
Notes
This implementation uses a simple method for prime number checking and might not be suitable for production use where larger primes are required.
The ASCII conversion is just a simple mapping for demonstration purposes and is not a secure way to handle encrypted values.
For practical use, consider using established libraries such as PyCryptodome for cryptographic operations.
