#zip

salarios = [1000, 5000, 7000, 850]
funcionarios = ["Felipe", "Daiana","Luiza","Flavio"]

for funcionario, salario in zip(funcionarios, salarios):
    print(f"Novo salario do {funcionario} é {salario * 1.1:.2f}")

dic_salarios = dict(zip(funcionarios, salarios))
print(dic_salarios)