produto = "iphone"
estoque_produto = 200

print("O produto", produto, "tem" , estoque_produto, "unidades no estoque")

import time
print("Contagem")
for i in range(5):
    #print (5 - i)
    print(5 - i, end ="\r") #end = "\r" para fazer a contagem na mesma linha
    time.sleep(1)
print("Acabou")