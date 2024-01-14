casa = float(input('Digite o valor do imóvel que desaja comprar: R$ '))
salário = float(input('Digite o valor do seu salário: R$ '))
financiamento = int(input('Em quantos anos deseja quitar o seu financiamento? '))
prestação = casa / (financiamento * 12)
mínimo = salário * 30 / 100
print(f'Para pagar um imóvel de R$ {casa:.2f} em {financiamento} anos, a prestação será de R$ {prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
