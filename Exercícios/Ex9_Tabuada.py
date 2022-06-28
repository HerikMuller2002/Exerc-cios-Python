#Tabuada
print('\n{:=^60}\n'.format('Tabuada'))

num = int(input('digite um número: '))

for i in range (10):
    i += 1
    print('%d * %d = %d' %(i,num,num * (i)))
