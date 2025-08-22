

# i = 1

# while i < 9:
# print(i)
# i += 1


# ---------------------------------------------------------------------------------------------------------------

# c1 = str(input("Nome 1:"))
# c2= str(input("Nome 2:"))
# c3= str(input("Nome 3:"))

# nomes = [c1, c2, c3]

# for cri in nomes:
#   print("------------------------")
#  print(cri)

# ----------------------------------------------------------------------------------------------------------------

# sc = "1234"
# tentativa = ""
# tentativas = 0

# while tentativa != sc:
# tentativa = input("Digite a senha: ")
# tentativas += 1
# if tentativa != sc:
# print("Senha incorreta, tente novamente!")

# print(f"Acesso permitido em {tentativas} tentativas!!")


# -----------------------------------------------------------------------------------------------------------


# c = int(input("Digite um numero:"))

# while c >= 0:
# print(c)
# c -= 1
# print("Fim da Contagem")

# -----------------------------------------------------------------------------------------------------------------

# matrizNUM = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9],
#    [0],
# ]

# for linha in matrizNUM:
#    print("-----")
#   for coluna in linha:
#        print(coluna)

#-----------------------------------------------------------------------------------------------------------------------

soma = 0

numero = int(input("Digite um numero positivo: "))

while numero > 0:
    soma += numero

    numero=int(input("Digite outro numero positivo ou (0/negativo para sair) "))

print(f"A soma de todos os numeros positivos é:{soma}")
