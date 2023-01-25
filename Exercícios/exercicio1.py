import os
import time

def limpar():
    os.system("cls")

while True:
    try:
        limpar()
        num = int(input("digite um número inteiro: "))
        break
    except:
        limpar()
        print("Erro!\nVocê não digitou um número inteiro!")
        time.sleep(3)
        continue

if num % 2 == 0:
    limpar()
    print("O número %i, é par!\n"%(num))
else:
    limpar()
    print("O número %i, é ímpar!\n"%(num))