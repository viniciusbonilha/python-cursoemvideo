números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado na lista! Não irei adicionar!')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
números.sort()
print(f'Você digitou os seguintes valores {números}')
