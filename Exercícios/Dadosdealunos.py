# Analisando e gerando dados de uma turma de alunos, podendo ou não incluir a situação.

def notas(* num, sit=False):
    """=> Avaliação de um ou vários alunos:
    param num: uma ou várias notas de alunos
    param sit: valor opcional, indicando se deve ou não adicionar a situação
    param return: dicionário com varias informações sobre a turmar"""
    alunos = {}
    alunos['Total'] = len(num)
    alunos['Maior'] = max(num)
    alunos['Menor'] = min(num)
    alunos['Média'] = round((sum(num)) / alunos['Total'])
    if sit:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'BOA'
        elif alunos['Média'] >= 5:
            alunos['Situação'] = 'RAZOÁVEL'
        else:
            alunos['Situação'] = 'PÉSSIMA'
    return alunos



resp = notas(5.5, 6.5, 9.5, sit=True)
print(resp)