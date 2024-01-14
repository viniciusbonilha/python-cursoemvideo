valor = float(input('O valor do produto é: R$ '))
a = valor - (valor * 10 / 100)
b = valor + (valor * 8 / 100)
print(f'O valor do produto com 10% de desconto para pagamento a vista é R$ {a:.2f} e para pagamento a prazo com 8% de acréscimo é de R$ {b:.2f}.')