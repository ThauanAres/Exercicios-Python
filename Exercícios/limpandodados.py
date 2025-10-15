# Exercício: Limpeza e Normalização de Dados de clientes

dados_brutos = [
    {'Nome': '   joão silva', 'Idade': '28', 'Status': 'Ativo', 'Valor_Total': 1500.50},
    {'Nome': 'Maria souza  ', 'Idade': '35', 'Status': 'inativo', 'Valor_Total': 75.00},
    {'Nome': 'ANA LIMA', 'Idade': 42, 'Status': 'ATIVO', 'Valor_Total': 3000},
    {'Nome': 'pedro alves', 'Idade': 17, 'Status': 'Ativo', 'Valor_Total': 50.25}
]


#1. FUNÇÃO PARA NORMALIZAR UM ÚNICO CLIENTE
def normalizar_cliente(cliente):
    #Cria uma cópia do dicionário para não alterar o original
    cliente_limpo = cliente.copy()

    # REGRA 1: Limpeza de nome (strip() + title())
    cliente_limpo['Nome'] = cliente_limpo['Nome'].strip().title()

    #REGRA 2: Conversão de Idade para int (trata a possibilidade de ser string ou int)
    idade = int(cliente_limpo['Idade'])
    cliente_limpo['Idade'] = idade

    #REGRA 3: Normalização de status (upper())
    cliente_limpo['Status'] = cliente_limpo['Status'].strip().upper()

    #REGRA 4: Criação da Categoria_Etaria
    if idade < 18:
        cliente_limpo['Categoria Etaria'] = 'Menor'
    else:
        cliente_limpo['Categoria Etaria'] = 'Maior'

    return cliente_limpo

#2. Aplicação com List Comprehension
dados_limpos = [normalizar_cliente(cliente) for cliente in dados_brutos]

print('--- Dados Brutos ---'.center(50, '-'))
for cliente in dados_brutos:
    print(f'Nome: {cliente['Nome']}')
    print(f'Idade: {cliente['Idade']}')
    print(f'Status: {cliente['Status']}')
    print(f'Valor_Total: {cliente['Valor_Total']}')
    print('-' * 50)
print('--- Dados limpos ---'.center(50, '-'))
for cliente in dados_limpos:
    print(f'Nome: {cliente['Nome']}')
    print(f'Idade: {cliente['Idade']}')
    print(f'Status: {cliente['Status']}')
    print(f'Valor_Total: {cliente['Valor_Total']}')
    print(f'Categoria Etaria: {cliente['Categoria Etaria']}')
    print('-' * 50)