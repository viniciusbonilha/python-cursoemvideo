from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos.')
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JÚNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
elif idade > 25:
    print('Sua categoria é MASTER')

