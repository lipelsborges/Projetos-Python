#sorted

salarios = [1000, 5000, 7000, 850]
salarios_ordenados = sorted(salarios, reverse=True)#ORDEM DECRESCENTE
#salarios_ordenados = sorted(salarios)#ORDEM CRESCENTE
print(salarios_ordenados)

salarios = [
    (1000, 500, 180),
    (5000, 40, 200),
    (7000, 0, 0),
    (600, 4000, 150),
]
funcionarios_ordenados = sorted(salarios, reverse=True, key=lambda x: sum(x))
print(funcionarios_ordenados)