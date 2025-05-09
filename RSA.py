import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#Greatest Common Divisor (GCD) of a and b using the Euclidean Algorithm.
#step keeps reducing the pair (a, b) toward their GCD
#Once b becomes 0, a holds the GCD, so return it.

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
#modular inverse of a under modulo m.  (a × x) % m = 1
#This is very important in cryptography, especially in RSA, where you need this inverse to compute the private key d.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
'''from sympy import isprime

print(isprime(7))   # True
print(isprime(10))  # False

pip install sympy

'''

def generate_random_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def generate_keys():
    p = generate_random_prime()
    q = generate_random_prime()

    while q == p:
        q = generate_random_prime()
#both prime numbers need to be different
    print(f"Randomly chosen primes:\np = {p}, q = {q}")

    n = p * q
    phi = (p - 1) * (q - 1)
    # Euler's Totient Function (phi)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
        #check if e is coprime with phi
    #randomly select a number e (the public exponent) from the range 2 to phi - 1. This e will be part of the public key.
    d = modinv(e, phi)

    return ((e, n), (d, n))
    #return the public key (e, n) and the private key (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

def main():
    print("RSA Encryption/Decryption with Random Keys")

    public_key, private_key = generate_keys()
    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)

    message = input("\nEnter message to encrypt: ")
    encrypted = encrypt(message, public_key)
    print("\nEncrypted:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
'''RSA is a method used to send secret messages safely over the internet.
It uses:

A public key to lock (encrypt) the message.

A private key to unlock (decrypt) it.
✅ AES is considered the most secure symmetric algorithm.
✅ RSA is best for secure key exchange, not bulk data encryption.
❌ DES is obsolete—vulnerable to brute force attacks due to its small key size.

RSA is computationally intensive (uses large prime numbers and modular arithmetic).
AES is much faster than RSA and DES for encrypting large amounts of data.
DES is fast but too weak for modern use.

Modern protocols (like HTTPS) use RSA to securely exchange keys, then use AES for the actual data encryption.
Use RSA when you need secure key exchange or digital signatures.'''