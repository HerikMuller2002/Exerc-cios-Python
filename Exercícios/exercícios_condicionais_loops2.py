#exercício 4
from itertools import count


lista1=[]
for i in range (100, 151,2):
    print(i)

print('='*100)

#exercício 5
temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura = temperatura-1

print('='*100)

#exercício 6
contador = 0
while contador < 100:
    if contador == 23:
        break
    else:
        print(contador)
        contador = contador+1