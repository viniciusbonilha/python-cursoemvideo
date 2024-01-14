from random import shuffle as embaralhar
aluno1 = input('Digite um nome: ')
aluno2 = input('Digite outro nome: ')
aluno3 = input('Digite mais um nome: ')
aluno4 = input('Digite um último nome: ')
lista = [aluno1,aluno2,aluno3,aluno4]
embaralhar(lista)
print(f'A ordem de apresentação por alunos é: \n {lista}.')