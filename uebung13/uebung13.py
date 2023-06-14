"""
1.)
"""
import si

prime_number = 23
for g in range(1, prime_number):
    print(f"Orders for g = {g}:")
    for i in range(1, 22):
        ord = pow(g,i,prime_number-1)
        if ord == 1:
            print(f"\033[92mord({g}^{i}) = {pow(g,i,prime_number-1)} \033[0m")
        else:
            print(f"ord({g}^{i}) = {pow(g,i,prime_number-1)} ")
    print('\n')


