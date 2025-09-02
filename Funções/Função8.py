#enumerate

salarios = [1000, 5000, 7000, 850]
funcionarios = ["Felipe", "Daiana","Luiza","Flavio"]

for i, salario in enumerate(salarios):
    funcionario = funcionarios[i]
    print(f"Novo salário do {funcionario} é {salario* 1.1:.2f}")