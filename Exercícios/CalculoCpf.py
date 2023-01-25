import re 

cpf = "746.824.890-70"

nums_point = cpf[:11]
nums = re.sub(r'[^0-9]','',nums_point)
count = 10
j = 0
for i in nums:
    i = int(i)
    j += i * count
    count -= 1 
num1 = (j*10)%11
if num1 > 9:
    num1 = 0

print("O primeiro digito do cpf é:",num1)

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

print("O segundo digito do cpf é:",dig2)