# Criando uma lista composta por pares e ímpares, ordenando os valores em cada lista.

num = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('='*30)
num[0].sort()
print(f'Os valores pares digitados em ordem foram: {num[0]}.')
num[1].sort()
print(f'Os valores impares digitados em ordem foram: {num[1]}.')