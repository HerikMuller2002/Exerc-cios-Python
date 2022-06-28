from random import choice

num1 = str(input('Primeiro aluno: '))
num2 = str(input('Segundo aluno: '))
num3 = str(input('Terceiro aluno: '))
num4 = str(input('Quarto aluno: '))

lista = [num1, num2, num3, num4]

escolha = choice(lista)

print('O aluno escolhido foi - %s'%(escolha))