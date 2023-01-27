import os

lista = [] 
lista_ref = []

while True:
    print("Comandos: ['listar']; ['desfazer']; ['refazer'], ['clear']")
    comando = input("Digite uma tarefa ou comando: ").lower()
    if comando == 'listar':
        if len(lista) < 1:
            print("Nada para listar!")
            continue
        else:
            print(*lista,sep='\n')
    elif comando == 'clear' or comando == 'cls':
        os.system('cls')
    elif comando == 'desfazer':
        if not lista:
            print("Não tem nada para desfazer!")
        else:
            tarefa = lista.pop()
            lista_ref.append(tarefa)
            print(*lista,sep='\n')
    elif comando == 'refazer':
        if not lista:
            print("Não tem nada para desfazer!")
        else:
            tarefa = lista_ref.pop()
            lista.append(str(tarefa))
            print(*lista,sep='\n')
    else:
        lista.append(comando)
        continue