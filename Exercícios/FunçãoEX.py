# Exercício de função para ter números inteiros com validação de entrada.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            if  -100 <= n <= 100:
                return n
        except (ValueError, TypeError):
            print('\033[031mERRO! Digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\033[35mEntrada de dados interrompida pelo usuário!\033[m')
            break


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            if -100 <= n <= 100:
                return n
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\033[35mEntrada de dados interrompida pelo usuário!\033[m')
            break


numeroint = leiaint('Digite um número inteiro: ')
numeroreal = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numeroint} e o valor real foi {numeroreal}!.')
