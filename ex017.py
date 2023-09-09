from math import hypot

cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))

hip = (cop ** 2 + cad ** 2) ** (1/2)
hi = hypot(cop, cad)

print(f'O valor da hipotenusa é {hip:.2f}.')
print(f'O valor da hipotenusa é {hi:.2f}.')