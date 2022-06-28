from random import shuffle

num1 = str(input('Primeiro aluno: '))
num2 = str(input('Segundo aluno: '))
num3 = str(input('Terceiro aluno: '))
num4 = str(input('Quarto aluno: '))

lista = [num1, num2, num3, num4]
shuffle(lista)

print('A ordem de apresentação será\n%s'%(lista))