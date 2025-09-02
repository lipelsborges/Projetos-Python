#range

lista = list(range(1, 6))
lista = list(range(1, 10, 2))
lista = list(range(5, 0 , -1))

print(lista)

import time
for i in range(5, 0 ,-1):
    print(i, end="\r")
    time.sleep(1)