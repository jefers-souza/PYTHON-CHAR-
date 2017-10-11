from math import hypot
co = float(input('Compartment of the opposite catheter:'))
ca = float(input('Length of adjacent leg:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('The hypotenuse will measure: {}'.format(hi))
hi2 = hypot(co, ca)
print('The hypotenuse will measure: {}'.format(hi2))

