import si

print(si.list_primes(10,35))


"""
2.)
"""
def aufgabe2(number):
    if pow(number, 3, 25) == 1 or pow(number, 3, 25) == 24:
        return True
    elif pow(number, 2*3, 25) == 24:
        return True

for n in range(1, 25):
    

