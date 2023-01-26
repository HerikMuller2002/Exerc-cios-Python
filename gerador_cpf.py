import random
import re

cpf = []
for i in range(0,9):
    n = str(random.randint(0,9))
    cpf.append(n)

a = cpf[:3]
b = cpf[3:6]
c = cpf[6:9]

cpf = ''.join(a) + '.' +''.join(b) + '.' + ''.join(c)
  
nums_point = cpf[:11]
nums = re.sub(r'[^0-9]','',nums_point)
count = 10
j = 0
for i in nums:
    i = int(i)
    j += i * count
    count -= 1 
dig1 = (j*10)%11
if dig1 > 9:
    dig1 = 0

cpf = cpf+'-'+str(dig1)


nums_point = cpf[:13]
nums = re.sub(r'[^0-9]','',nums_point)
count = 11
j = 0
for i in nums:
    i = int(i)
    j += i * count
    count -= 1 
dig2 = (j*10)%11
if dig2 > 9:
    dig2 = 0

cpf = cpf+str(dig2)
print(cpf)