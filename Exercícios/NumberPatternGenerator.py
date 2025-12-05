# Função para gerar o padrão de números de 1 até n.

def number_pattern(n):
    # Primeiro verificamos se o valor passado é realmente um inteiro.
    # Caso não seja, retornamos a mensagem exigida pelo enunciado.
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Em seguida, verificamos se o número é maior que 0.
    # Se for menor que 1 (ou seja, 0 ou negativo), retornamos a mensagem correta.
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Criamos uma string vazia que armazenará o padrão de números.
    result = ""
    
    # Usamos um loop for para gerar os números de 1 até n.
    for i in range(1, n + 1):
        # Convertendo o número 'i' para string e adicionando ao resultado.
        result += str(i)
        
        # Se o número ainda não for o último, adicionamos um espaço ao resultado.
        # Isso evita um espaço no final da string.
        if i < n:
            result += " "
    
    # Retornamos a string final contendo o padrão.
    return result
