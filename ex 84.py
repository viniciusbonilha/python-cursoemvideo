temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, possuí {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
