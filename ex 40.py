n1 = float(input('A nota da primeira prova foi: '))
n2 = float(input('A nota da segunda prova foi: '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'Sua média foi de {m:.1f} REPROVADO!')
elif m >= 7.0:
    print(f'Sua média foi de {m:.1f} APROVADO! Parabéns!')
elif m >= 5 and m <=6.9:
    print(f'Sua média foi de {m:.1f} RECUPERAÇÃO! Estude mais!')