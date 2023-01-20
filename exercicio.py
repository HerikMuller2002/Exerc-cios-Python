nome = str(input("seu nome: "))

inv = nome[::-1]

espaco = nome.split()
if len(espaco) > 1:
    espacos = True
else:
    espacos = False

letras = 0
for i in espaco:
    for j in i:
        letras += 1

primeira = nome[0]
ultima = nome[-1]

print("seu nome: %s" %(nome))
print("nome invertido: %s" %(inv))
print("tem espaço: %s" %(espacos))
print("tem %s letras" %(letras))
print("primeira letra: %s" %(primeira))
print("última letra: %s" %(ultima))