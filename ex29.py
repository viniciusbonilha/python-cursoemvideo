velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia, dirija com segurança!')
