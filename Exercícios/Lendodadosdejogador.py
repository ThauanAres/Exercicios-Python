# Lendo dados de vários jogadores de futebol e armazenando em uma lista de dicionários.

jogadores = []

while True:
    jogador = {}
    jogador['Nome'] = input('Nome do jogador: ').strip()

    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    gols_por_partida = []
    for c in range(1, total + 1):
        gols = int(input(f'   Gols na partida {c}? '))
        gols_por_partida.append(gols)

    jogador['Gols'] = gols_por_partida
    jogador['Total'] = sum(gols_por_partida)

    jogadores.append(jogador.copy())

    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resposta == 'N':
        break
#         Até aqui foi para ler os jogadores
# A partir daqui vem a análise de dados

print('-=' * 40)
print(f'{"COD":<4} {"NOME":<15} {"GOLS":<20} {"TOTAL":<5}')
print('-' * 40)
for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["Nome"]:<15} {str(j["Gols"]):<20} {j["Total"]:<5}')
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR: {jogadores[busca]["Nome"]}')
        for i, g in enumerate(jogadores[busca]["Gols"], start=1):
            print(f'   No jogo {i} fez {g} gols.')
    print('-' * 40)

print('PROGRAMA ENCERRADO.')