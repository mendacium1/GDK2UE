from argon2 import argon2_hash

password = "testpassword"
salt = b'somesaltvalue'
hash_len = 32
time_cost = 2**31 - 1
memory_cost = 2**31 - 1
parallelism = 255

hash = argon2_hash(password=password.encode(),
                                salt=salt,
                                buflen=hash_len,
                                t=time_cost,
                                m=memory_cost,
                                p=parallelism)
print(hash.hex())
