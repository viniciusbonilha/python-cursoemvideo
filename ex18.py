import math
angulo = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo {angulo:.0f}º tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo {angulo:.0f}º tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo {angulo:.0f}º tem a tangente de {tangente:.2f}')
