print('========== LOJAS HENRIQUE ==========')
valor = float(input('Preço das compras: R$ '))
print('''Escolha uma das formas de pagamento:
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
if opção == 1:
    a = valor - (valor * 10 / 100)
    print(f'O valor da sua compra com 10% de desconto é: R$ {a:.2f}.')
elif opção == 2:
    a = valor - (valor * 5 / 100)
    print(f'O valor da sua compra com 5% de desconto é: R$ {a:.2f}.')
elif opção == 3:
    a = valor / 2
    print(f'O valor da sua compra é de R$ {valor}. Parcelado em 2x, ficará 2 parcelas de R$ {a:.2f} sem JUROS.')
elif opção == 4:
        total = valor + (valor * 20/ 100)
        parcelas = int(input('Quantas parcelas? '))
        totalparcelas = total / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R$ {totalparcelas} com JUROS.')
        print(f'Sua compra de R$ {valor:.2f} vai custar R$ {total:.2f} no final. ')
else:
    valor = 0
    print('Opção invalida de pagamento.')
