from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'ARQUIVO.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
        sleep(2)
    elif resposta == 2:
        # Opção cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        sleep(2)
        cabeçalho('Saindo do sistema.... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
        sleep(2)

