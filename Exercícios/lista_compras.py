# import
import os
from time import sleep

# variáveis
lista = []
opcoes_val = "ial"

# funções
def limpar():
    os.system("cls")

def opcoes():
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    return opcao

def inserir(lista):
    while True:  
        limpar()
        print("Digite os itens que deseja...")
        print("[s]air\n")
        x = " ".join(lista)
        print(x)
        item = input("\nQual item deseja adidicionar: ")
        if item == "s":
            break
        else:
            lista.append(item)
            continue

def apagar(lista):
    limpar()
    print("Index dos itens:")
    for i in lista:
        print(lista.index(i), i)
    ind = int(input("\nIndex do item que deseja excluir: "))
    lista.pop(ind)

def listar(lista):
    while True:
        limpar()
        for i in lista:
            print(lista.index(i), i)
        sair = input("\n[s]air: ")
        if sair == "s":
            break
        else:
            continue

while True:
    limpar()
    opcao = opcoes()
    if opcao == "i":
        inserir(lista)
    elif opcao == "a":
        apagar(lista)
    elif opcao == "l":
        listar(lista)
    else:
        break
print(lista)