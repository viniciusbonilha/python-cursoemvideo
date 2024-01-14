def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {a:.2f}m².')


print('     CONTROLE DE TERRENOS     ')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
