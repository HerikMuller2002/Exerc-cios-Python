# import
import time
import os

# funções
def limpar():
    os.system('cls')

def resultado(result):
    if result:
        limpar()
        print('Acertou!')
        time.sleep(2)
    else:
        limpar()
        print('Errou!')
        time.sleep(2)

def exibe(num):
    if num == 1:
        print(perguntas[0]['pergunta'])
        print('')
        cont = 0
        for j in perguntas[0]['opcoes']:
            alt = ['a)','b)','c)','d)']
            print(alt[cont],j)
            cont += 1
    elif num == 2:
        print(perguntas[1]['pergunta'])
        print('')
        cont = 0
        for j in perguntas[1]['opcoes']:
            alt = ['a)','b)','c)','d)']
            print(alt[cont],j)
            cont += 1
    else:
        print(perguntas[2]['pergunta'])
        print('')
        cont = 0
        for j in perguntas[2]['opcoes']:
            alt = ['a)','b)','c)','d)']
            print(alt[cont],j)
            cont += 1

def verificar(chute,perguntas,questao):
    if questao == 1:
        if chute == perguntas[0]['resposta']:
            resultado(result=True)
            return True
        else:
            resultado(result=False)
            return False
    elif questao == 2:
        if chute == perguntas[1]['resposta']:
            resultado(result=True)
            return True
        else:
            resultado(result=False)
            return False
    else:
        if chute == perguntas[2]['resposta']:
            resultado(result=True)
            return True
        else:
            resultado(result=False)
            return False

def jogar(questao,perguntas):
    while True:
        limpar()
        exibe(questao)
        chute = input("\nSeu palpite: ")
        if chute not in chutes_val:
            limpar()
            print("Digite uma opção válida!")
            time.sleep(2)
            continue
        else:
            resposta = verificar(chute,perguntas,questao)
            if not resposta:
                continue
            else:
                if questao == 3:
                    return 'acabou'
                else:
                    return True

# código
perguntas = [{'pergunta':'Qual é a capital da comlômbia?','opcoes':['Santiago','Caracas','Bogotá','Medelin'],'resposta':'c'},{'pergunta':'Quantos continentes há no mundo?','opcoes':['6','7','5','4'],'resposta':'a'},{'pergunta':'Quais países não fazem fronteira com o Brasil?','opcoes':['venezuela e colombia','uruguai e paraguai','suriname e bolívia','equador e chile'],'resposta':'d'}]

chutes_val = 'abcd'
questao = 1
while True:
    jogo = jogar(questao,perguntas)
    if jogo:
        questao += 1
    if jogo == 'acabou':
        break