#exercício 1
dia = str(input('Escreva o dia da semana:'))
if dia == 'domingo' or dia == 'sábado':
    print('hoje é dia de descanso!')
else:
    print('Você precisa trabalhar!')

#exercício 2
lista = ['banana', 'maçã', 'melão', 'abacate', 'framboesa']
print("checando se existe o elemento 'morango' na lista:")
if ('morango' in lista):
    print('Elemento existe')
else:
    print('Elemento não existe')

#exercício 3
tup = (1,2,3,4)
lista2 = []
for elem in tup:
    NovoValor = elem * 2
    lista2.append(NovoValor)
print(lista2)