p = 47
g = 5
A = 30
B = 28

alice_priv_key = 1
bob_priv_key = 1

while True:
    if pow(g,alice_priv_key,p) == A:
        print(f"Alice priv_key: {alice_priv_key}")
        print(f"Shared_Secret: {pow(B,alice_priv_key,p)}")
        break
    if pow(g,bob_priv_key,p) == B:
        print(f"Bob priv_key: {bob_priv_key}")
        print(f"Shared_Secret: {pow(A,bob_priv_key,p)}")
        break
    alice_priv_key += 1
    bob_priv_key += 1


