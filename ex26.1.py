frase = str(input('Digite uma frase: ')).strip().upper()
contar = frase.count('A')
print(f'A letra A aparece {contar} vezes na frase')
encontrar = frase.find('A') + 1
print(f'A letra A apareceu na posição {encontrar}')
rencontrar = frase.rfind('A') + 1
print(f'O último A apareceu na posição {rencontrar}')