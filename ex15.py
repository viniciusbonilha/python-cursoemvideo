diaria = int(input('Por quantos dias seu veículo foi alugado? '))
km = float(input('Quantos KM você rodou com seu veículo? '))
#a = diaria * 60
#b = km * 0.15
#c = a+b
a = (diaria * 60) + (km * 0.15)
#print(f'O valor total de sua locação é de R$ {c:.2f}')
print(f'O valor total de sua locação é de R$ {a:.2f}')