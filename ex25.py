nome = str(input('Digite o seu nome completo: ')).strip().upper()
dentro = 'SILVA' in nome.split()
print(f'Seu nome possuí Silva? {dentro}')
