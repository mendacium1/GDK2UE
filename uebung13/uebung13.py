"""
1.)
"""
input("\nAufgabe 1")

prime_number = 23
for g in range(1, prime_number):
    print(f"\nOrders for g = {g}:")
    ord_list = []
    for i in range(1, 23):
        ord_list.append(pow(g,i,prime_number))
    for j in range(0, len(ord_list)):
        if ord_list[(j+1) % len(ord_list)] == 1:
            print(f"\033[92mord({g}^{j+1} || {pow(g,j,prime_number)*g}) = {ord_list[j]} \033[0m")
            print(f"\033[94mord({g}^{j+2} || {pow(g,j+1,prime_number)*g}) = {ord_list[j+1]} \033[0m")
            break
        else:
            print(f"ord({g}^{j+1} || {pow(g,j,prime_number)*g}) = {ord_list[j]}")

"""
2.)
"""

input("\nAufgabe 2")

import si

prime_number = 137

element_ords = {}

for g in range(1, prime_number):
    for power in range(1, prime_number):
        if pow(g,power,prime_number) == 1:
            if power in element_ords:
                element_ords[power] += 1
            else:
                element_ords[power] = 1
            break

print(f"Alle möglichen Elementordnungen + Anzahl: {element_ords}")
print()

"""
3.)
Es kann 1, 2, p - 1, (p - 1) / 2
"""
input("\nAufgabe 3")
safe_prime = 167

element_ords = {}

for g in range(1, safe_prime):
    for power in range(1, safe_prime):
        if pow(g,power,safe_prime) == 1:
            if power in element_ords:
                element_ords[power] += 1
            else:
                element_ords[power] = 1
            break

print(f"Mögliche Ordnungen einer safe prime: {element_ords}")

"""
4.)
Keine wiederholungen aka 1 steht am ende
"""
input("\nAufgabe 4")
prime_number = 137

for g in [4,5]:
    for power in range(1, prime_number):
        if pow(g,power,prime_number) == 1 and power == prime_number - 1:
            print(f"{g} ist EIN erzeugendes Element von {prime_number}")
            break
        elif pow(g,power,prime_number) == 1 and not power == prime_number - 1:
            print(f"{g} ist KEIN erzeugendes Element von {prime_number}")
            print(f"Das ist die Ordnung von {g}:")
            for power in range(1, prime_number):
                if pow(g, power, prime_number) == 1:
                    print(power)
                    break
            break

"""
5.)
"""
input("\nAufgabe 5")
p=137
g=3
for w in [34,8]:
    if pow(p-1,1,w) == 0:
        print(f"Die Ordnung von {w} ist {pow(g,int((p-1)/w),p)}")
    else:
        print(f"{w} hat keine Ordnung")

