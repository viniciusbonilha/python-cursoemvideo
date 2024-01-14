from random import randint
from time import sleep
computador =  randint(0, 5)
jogador = int(input('Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar...'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer! ')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')
