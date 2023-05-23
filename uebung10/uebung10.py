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

print("2. Original message:", m)
print("2. Encrypted message:", encrypted_msg)
print("2. Decrypted message:", decrypted_msg)


"""
3) Großes Schlüsselpaar
"""
p = 179322134705829530261812409390667300613986766261659076019663091706544555136687638438335130331396258572201032907136515774878915163114653294034333112904243831183784271014263591337259783180437652067274609227335422870927017804995457916545296093606548346700831601857762992215087430346525273724693484867246982221131
q = 117905173234785591703387460067543561683309917004041885643013943986776343925343211245528162854109191553727760665033891352074295489760323485117850946698600745048918302583170646306683614411611525258044316274774807616514051339594347182681436060113444854907391410667744795623578814572956102641297929653968654611357

e = 65537

m = 999

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = 987654321
c = pow(m, e, n)
m2 = pow(c, d, n)

print("2. Original message:", m)
print("2. Encrypted message:", c)
print("2. Decrypted message:", m2)


"""
6.) Bruteforce
"""
import subprocess

# Öffentlicher Schlüssel und Chiffrat
public_key_file = 'pubkey.pem'
chiffrat_file = 'c'

# Brute-Force-Schleife für dreistelligen Statuscode
for code in range(100, 1000):
    code_str = str(code).encode('ascii')
    command = f'echo -n "{code_str}" | openssl rsautl -encrypt -inkey {public_key_file} -pubin -out {chiffrat_file} -raw'
    subprocess.run(command, shell=True)
    
    with open(chiffrat_file, 'rb') as f:
        chiffrat = f.read()

    # Überprüfen, ob das Chiffrat mit dem ursprünglichen Chiffrat übereinstimmt
    if chiffrat == open(chiffrat_file, 'rb').read():
        print(f'Brute-Force erfolgreich! Statuscode: {code}')
        break

