usu = "abcd"
senha = 1234
tentativa = 0

usu1= str(input("Digite o Usuario: "))
se1 = int(input("Digite os 5 digitos da senha: "))

while usu1 != usu or se1 != senha :
    print("Usuario incorreto ou senha invalida")
    usu1 = str(input("Digite novamente: "))
    se1 = int(input("Digite novamente a senha: "))
    tentativa += 1

print(f"Acesso permitido e {tentativa} tentativas.")


