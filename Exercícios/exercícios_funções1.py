'''
#exercício 1
def pares():
    for item in range(1,21):
        if item % 2 == 0:
            print (item)
pares()

#exercício 2
def maiuscula ():
    txt = str(input('digite uma palavra:'))
    x = txt.upper()
    print(x)
maiuscula()

#exercício 3
def adicionar (list2):
    print(list2.append(5))
    print(list2.append(6))
list1 = [1, 2, 3, 4]
adicionar(list1)
print(list1)
'''