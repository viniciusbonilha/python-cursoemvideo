from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range (1,8):
    nasc = int(input(f'Digite o seu ano de nascimento da {pessoas}º pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade.')
print(f'Ao todo tivemos {totalmenor} pessoas menores de idade.')