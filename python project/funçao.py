


def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    
    return imposto

preco_produto1 = 900
preco_produto2 = 3500
preco_produto3 = 1500
imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)
imposto_produto3 = calcular_imposto(preco_produto3)

print(f"O primeiro produto: {imposto_produto1}")
print(f"O segundo produto : {imposto_produto2}")
print(f"O terceiro produto produto : {imposto_produto3}")