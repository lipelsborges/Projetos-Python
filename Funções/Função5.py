#filter

salarios = [1000, 5000, 7000, 850]

salarios_altos = list(filter(lambda x: x > 2000, salarios))
print(salarios_altos)