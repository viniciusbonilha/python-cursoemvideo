print('=' * 30)
print('{:^30}' .format('Banco Bonilha'))
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
cedula = 50
totalceldula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalceldula += 1
    else:
        if totalceldula > 0:
            print(f'Total de {totalceldula} cédulas de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalceldula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Bonilha. Tenha um ótimo dia!')
