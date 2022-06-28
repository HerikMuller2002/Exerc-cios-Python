#exercício 7
lista1 = list()
var1 = 4
while var1 <=20:
   var1 = var1 + 2
   lista1.append(var1)
   print(lista1)

print('='*100)

#exercício 8
nums = range(5, 45, 2)
print(list(nums))

print('='*100)

#exercício 9
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print('='*100)

#exercício 10
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
#print(frase)
for caracteres in frase:
    if caracteres == 'r':
       count = count+1
print("O caracter r aparece %s vezes na frase." %(count))