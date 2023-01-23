import os
import time

def limpar():
    os.system("cls")

while True:
    try:
        limpar()
        hora = int(input("digite a hora: "))
        min = int(input("digite o minuto: "))
        if hora > 24 or min > 60:
            raise Exception
        else:
            break
    except:
        limpar()
        print("Erro!\nDigite novamente!")
        time.sleep(2)
        continue

if hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')