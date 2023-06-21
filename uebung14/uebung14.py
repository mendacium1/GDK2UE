"""
2.)
"""
p = 89
q = 83
e = 257
m = 6666

phi = (p - 1) * (q - 1)
n = p * q


d = pow(e, -1, phi)

pub_key = n, e
priv_key = n, d

signed_m = pow(m, d, n)
verified_m = pow(signed_m, e, n)

print(f"Original message: {m}")
print(f"Signed message: {signed_m}")
print(f"Verified message: {verified_m}")


"""
3.)
"""
n, e = 23411215188986094455431744210054114669691530375288687585642796295898030433723300550399114027259594139700141733103286885796949525800470892001358771354169807132489677852177840764527999402644443972441174160502322342668019261586682115020654667310092072757897673412738688129588721422956010114240344299008152524695437457576628737749042351050100906740557082710388084040576637298725223308970456812903344355459650171391228398755503597719116973861648355375789345620618654254353052915033393814687502208667750068945876769860483181405125381876466402201193914968425594247700415792865904386608474376376884996912771408039442207590309, 65537

s = 981754905789187519258

m = pow(s, e, n)

print(f"Nachrichten paar: {s} {m}")

"""
4.)
"""
import random
import math
p = 42961
w = 179
h = 0
ggt = 2
r = 2
g = 2
while g != 1:
    while r != 1:
        h = 1
        while ggt != 1:
            h = 2
            ggt = math.gcd(h, p)
            print(f"h: {h}")
        print(f"r = {h} ^ {int((p-1)/w)} mod {p}")
        r = pow(h, int((p-1)/w), p)
        print(f"r: {r}")
    print(f"g = {r} ^ {int((p-1)/w)} mod {p}")
    g = pow(r, int((p-1)/w), p)
    print(f"g: {g}")

print(f"G hat die Ordnung w in Z*p: {g}")

"""
5.)
"""
# openssl dsaparam -genkey 3072

"""
6.)
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

with open("dsa_param.pem", "rb") as key_file:
    dsa_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
p = dsa_key.parameter_numbers().p
q = dsa_key.parameter_numbers().q
g = dsa_key.parameter_numbers().g

