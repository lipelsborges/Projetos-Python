#Função 2
#help

def calcular_imposto(faturamento, taxa):
    """
    faturamento (float): o faturamento da empresa que vamos calcular o imposto
    taxa (float): a taxa porcentual de imposto sobre o faturamento (ex: 0.2)

    return: imposto, faturamento_liquido
    imposto(float): valor total do imposto calculado sobre o faturamento
    faturamento_liquido(float): quanto sobrou do faturamento depois de descontado o imposto
"""
    imposto = faturamento * taxa
    return imposto, faturamento - imposto

help(calcular_imposto)