from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor para jogar: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você deseja ser PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou o número {jogador} e o computador jogou o número {computador}. Total de {total}.', end= ' ')
    print('Deu PAR!' if total % 2 == 0 else 'Deu IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
