número = (int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')),)
print(f'Você digitou os valores: {número}')
print(f'O valor 9 apareceu {número.count(9)} vezes.')
if 3 in número:
    print(f'O valor 3 apareceu na {número.index(3)+1}º posição. ')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores digitados pares foram: ', end='')
for n in número:
    if n % 2 ==0:
        print(n, end=' ')
