#AdivinheNúmero
import random

print('adivinhe o número que eu estou pensando entre 1-10')

lista = []

for i in range (1,11):
    lista.append(i)

pc = random.choice(lista)
acertar = False

while not acertar:
    chute = int(input('seu palpite: '))
    
    if chute == pc:
            print('Você acertou! \nO número que eu escolhi era o %d.' %(pc))
            acertar = True

    elif chute > pc:
            print('Você errou! o número é menor.')

    else:
            print('Você errou! o número é maior.')
