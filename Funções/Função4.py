#map

salarios = [1000, 5000, 7000, 850]

"""def aumentar_salario(salario):
    if salario > 3000:
        novo_salario = salario * 1.08
    else:
        novo_salario = salario * 1.1
    return novo_salario
    
novos_salarios = list(map(aumentar_salario, salarios))
print(novos_salarios)"""

def aumentar_salario(salario):
    return salario * 1.1

novos_salarios = list(map(lambda x: x * 1.1, salarios))
print(novos_salarios)