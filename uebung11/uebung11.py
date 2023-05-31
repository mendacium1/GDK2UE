"""
2.)
"""
# n - 1 = 2^3 * 3
for i in range(1, 25):
    for s in range(0,4):
        if (pow(i, 2**s, 25)) == 1 or (pow(i, 2**s, 25)) == 24:
            print(f"{i} ist ein Zeuge")

