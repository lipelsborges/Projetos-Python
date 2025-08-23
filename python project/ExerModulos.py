from math import floor

num = float (input("Digite um numero: "))
print("O numero {} tem a parte inteira de {}". format(num, floor(num)))


#Exercicio 2

import random

alu = ["Felipe", "Flavio", "Luiza", "Daiana"]
sort =  random.choice(alu) #choice sorteia um da lista

print("O aluno sorteado foi {}". format (sort))


#Exercicio 3 

import random

alu = ["Felipe", "Flavio", "Luiza", "Daiana"]
random.shuffle(alu) #shuffle sorteia em ordem
print(alu)

#Exercicio 4

import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adicente: "))
hi = math.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))