# CALCULADORA SIMPLES FELIPE
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero:  "))

print("-----------------------------")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("-------------------------------")

operação = input("Digite o numero da operação: ")

if operação == "1":
    resultado = num1 + num2

elif operação == "2":
    resultado = num1 - num2

elif operação == "3":
    resultado = num1 * num2

elif operação == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida"

print("Resultado", resultado)

