from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número
    [ 4 ] Novos números
    [ 5 ] Encerrar programa ''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a {soma}')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a {multiplicação}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior número digitado é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando....')
    else:
        print('Opção inválida! Tente novamente...')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')