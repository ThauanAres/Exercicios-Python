# Exercício de ajuda interativa com funções de Python.

from time import sleep


def ajuda(comando):
    titulo('Acessando o manual de comando')
    print('\033[33m')
    help(comando)
    try:
        help(eval(comando))
    except (NameError, AttributeError):
        print(f'O comando {comando} não existe! Tente outro.')
    print('\033[m')
    sleep(2)


def titulo(msg):
    print('-' * (len(msg) + 4))
    print(msg.center(len(msg) + 4))
    print('-' * (len(msg) + 4))
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp')
    comando = str(input('Função Biblioteca (digite ''sair'' para fechar) > ')).lower().strip()
    if comando in 'sair':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO')