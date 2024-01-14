total18 = totalhomens = totalmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}. ')
print(f'Ao todo temos {totalhomens} homens cadastrados. ')
print(f'Temos {totalmulher20} mulheres com menos de 20 anos. ')
