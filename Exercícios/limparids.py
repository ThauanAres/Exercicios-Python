# Limpeza de ids com espaços em branco e conversão para inteiros.

transacoes_brutas = [
    '   1054A  ',
    '2001B',
    '  509C',
    '3000D   '
]

def limpar_e_converter_id(lista_ids):
    id_limpos = [int(identificacao.strip()[:-1]) for identificacao in lista_ids]
    return id_limpos


lista_final_ids = limpar_e_converter_id(transacoes_brutas)
print(lista_final_ids)