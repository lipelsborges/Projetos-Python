senha = 1234
tentativas = 0

s1 = int(input("Digite a senha: "))

while s1 != senha:
    tentativas += 1
    print("Senha incorreta, tente novamente")
    s1 = int(input("Digite a senha correta: "))


print("Acesso permitido")


numeros = 0
soma = 0
s2 = int(input("Digite um numero(ou 0/negativo para encerrar): "))

while s2 > 0:
    numeros += 1
    soma += s2
    s2 = int(input("Digite outro numero(ou 0/negativo para encerrar): "))
    

print(f"Numeros digitados: {numeros}")
print(f"Soma total dos numeros digitados {soma}")
print(f"Você errou a senha {tentativas} vezes!")
