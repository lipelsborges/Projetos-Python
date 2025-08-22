n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))
n3 = float(input("Nota 3: "))

soma = (n1 + n2 + n3) / 3

if soma >= 7:
    print("Você passou, Nota: ", soma)
else:
    print("Recuperação, Nota: ", soma)
