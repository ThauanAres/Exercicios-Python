# Dados brutos em formato de tupla transformados em uma lista de dicionários.

# A ordem é sempre: (Nome, Idade)
dados_brutos = [
    ('Alice', 28),
    ('Bob', 35),
    ('Carol', 22)
]


def converter_para_dicionarios(tupla):
    lista_dicionario = []
    for Nome, Idade in tupla:
        novo_dicionario = {'Nome': Nome, 'Idade': Idade}
        lista_dicionario.append(novo_dicionario)
    return lista_dicionario


resultado_final = converter_para_dicionarios(dados_brutos)
print(resultado_final)