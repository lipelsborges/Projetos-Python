#open
salarios = [1000, 5000, 7000, 850]
funcionarios = ["Felipe", "Daiana","Luiza","Flavio"]


#arquivo = open("salarios_funcionarios.txt", "w", encoding="utf-8")

"""for funcionario, salario in zip(funcionarios, salarios):
    arquivo.write(f"Novo salario do {funcionario} é {salario * 1.1:.2f}\n")
arquivo.close()

arquivo = open("salarios_funcionarios.txt", "r", encoding="utf-8")
texto = arquivo.read()
print("Texto do arquivo:")
print(texto)
arquivo.close()"""


# Recomendado a fazer desta forma----------------------------------------------
with open("salarios_funcionarios.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
print("Texto do arquivo:")
print(texto)



#APPEND---------------------------------------------------------------------------
#arquivo = open("salarios_funcionarios.txt", "a", encoding="utf-8")

#for funcionario, salario in zip(funcionarios, salarios):
    #arquivo.write(f"Novo salario do {funcionario} é {salario * 1.1:.2f}\n")
#arquivo.close()