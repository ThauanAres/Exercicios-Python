# Função para registrar compras de produtos e calcular a soma total das compras por pessoa.

def registrar_compras():
    '''Função para registrar nome, idade, produto, valor do produto
    e calcular a soma total das compras da pessoa caso ela tenha mais
    uma compra'''

#Dicionário para armazenar os dados de cada pessoa
registros = {}

print('--- Sistema de Registro de Compras ---')

while True:
    #Pede o nome da pessoa
    nome = input('Digite o nome da pessoa (ou ''sair'' para encerrar): ').strip()

    if nome.lower() == 'sair':
        break

        #Verifica se a pessoa já está registrada
    if nome not in registros:

        #Caso seja a primeira vez, pede a idade e inicializa o registro
        try:
            idade = int(input(f'Digite a idade de {nome}: '))
        except ValueError:
            print('Idade inválida. Tente novamente!')
            continue
    registros[nome] = {'idade': idade, 'compras': [], 'total_gasto': 0.0}

    #Loop para registrar produtos para a pessoa atual
    print(f'\n--- Registrando compras para {nome} ---')
    while True:
        produto = input('Digite o nome do produto (ou ''fim'' para a próxima pessoa): ').strip().title()

        if produto.lower() == 'fim':
            break
        try:
            valor_str = input(f'Digite o valor do produto {produto} (não é necessário vírgulas ou pontos): R$ ').replace(',','.')
            valor = float(valor_str)
            if valor < 0:
                print('O valor do produto não pode ser negativo!')
                continue
        except ValueError:
            print('Valor inválido. Use números (ex 10.50). Tente novamente!')
            continue

        #Adiciona a compra ao registro da pessoa
        registros[nome]['compras'].append({'produto':produto, 'valor': valor})

        #Atualiza a soma dos produtos comprados
        registros[nome]['total_gasto'] += valor

        print(f"Produto '{produto}' (R${valor:.2f}) registrado para {nome}!")

        #Exibe os resultados
        print('\n' + '=' * 40)
        print('--- RESUMO DAS COMPRAS REGISTRADAS ---')
        print('=' * 40)

        if not registros:
            print('Nenhum registro de compra foi encontrado!')
        else:
            for nome, dados in registros.items():
                print(f'\nNome: {nome} (idade:{dados['idade']}')
                print('Produtos Comprados: ')

            if dados['compras']:
                for item in dados['compras']:
                    print(f'   - {item['produto']}: R${item['valor']:.2f}')
                print(f'Total Gasto: R${dados['total_gasto']:.2f}')
            else:
                print('Nenhum produto registrado!')

#Chama a função para iniciar o programa
if __name__ == '__main__':
    registrar_compras()