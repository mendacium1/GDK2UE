import random

"""
1) RSA-Schlüsselpaar
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def generate_rsa_keypair(p, q, e):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q should be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        raise ValueError("The public exponent e and phi(n) must be coprime.")

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    return (n, e), (n, d)


# Prime numbers p and q
p = 29
q = 47
# Public exponent
e = 17

public_key, private_key = generate_rsa_keypair(p, q, e)

print("Public key (n, e):", public_key)
print("Private key (n, d):", private_key)


"""
2) Square-And-Multiply-Algorithmus
"""
def square_and_multiply(base, exponent, modulus):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result


def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = square_and_multiply(message, e, n)
    return encrypted_message


def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = square_and_multiply(encrypted_message, d, n)
    return decrypted_message



m = 999

encrypted_msg = encrypt(m, public_key)
decrypted_msg = decrypt(encrypted_msg, private_key)

print("Original message:", m)
print("Encrypted message:", encrypted_msg)
print("Decrypted message:", decrypted_msg)

