peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (M): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.1f}, seu peso é ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.1f}, você possúi sobrepeso.')
elif 30 <= imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, você possuí obesidade.')
else:
    print(f'Seu IMC é de {imc:.1f}, você possuí obisidade mórbida.')