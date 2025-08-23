import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}". format(num, raiz))

#Se quiser utilizar apenas 1 funcionalidade

from math import sqrt, floor
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}". format(num, floor(raiz)))   #floor arredondar para baixo.



import random
num = random.randint(1, 10)   #randint 
print(num)

