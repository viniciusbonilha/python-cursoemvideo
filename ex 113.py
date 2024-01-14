def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não informar este dado.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não informar este dado.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1}.')
print(f'O valor real digitado foi {n2}')
