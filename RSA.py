import random
from math import gcd

def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_prime():
    while True:
        prime = random.randint(500, 1000)
        if is_prime(prime):
            return prime



def d_function( e, phi):
    k=1
    d = (1 + k * phi) / e

    while not d.is_integer():
        k += 1
        d = (1 + k * phi) / e

    return int(d)

def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    d = d_function(e, phi)
    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    #c= p^e mod n
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def ascii_convertor(encrypted_values):
    character_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join([character_map[val % len(character_map)] for val in encrypted_values])

def decrypt(cipher_text, private_key):
    d, n = private_key
    #p= c^d mod n
    decrypted_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_text)


def main():
    public_key, private_key = generate_keypair()

    print("Public Key:", public_key,"       ","Private Key:", private_key)


    plain_text = input("Enter the plain text: ")

    cipher_values = encrypt(plain_text, public_key)
    # Map the encrypted values back to characters
    cipher_text = ascii_convertor(cipher_values)
    print("Cipher Text (ASCII):", cipher_text)


    decrypted_text = decrypt(cipher_values, private_key)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
