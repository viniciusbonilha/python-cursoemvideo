import math
n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
r = math.hypot(n1,n2)
print(f'O comprimento da hipotenusa é igual a: {r:.2f}')