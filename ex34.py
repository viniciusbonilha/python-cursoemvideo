salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R$ {salário:.2f} passa a ganhar {novo:.2f} agora')
