#Desafio1--->programa que lê um número inteiro e mostra seu sucessor e o antecessor.
n1 = int(input("digite um número: "))
print("o sucessor de {} é {}, e o antecessor é {}.".format(n1, n1+1, n1-1))

#=======================================================
print('='*100)
#=======================================================

#Desafio2--->programa que calcula a média.
nota1= float(input('1ª nota: '))
nota2= float(input('2ª nota: '))
nota3= float(input('3ª nota: '))
med= (nota1+nota2+nota3)/3
print('sua média é {:.1f}' .format(med))

#=======================================================
print('='*100)
#=======================================================

#Desafio3--->programa que calcula o dobro, triplo e a raíz quadrada.
n= float(input('digite um número: '))
print('o dobro de {} é {:.1f}, o triplo é {:.1f} e a raíz quadrada é {:.2f}.' .format(n, n*2, n*3, n**0.5))

#=======================================================
print('='*100)
#=======================================================

#Desafio4---> conversor de metros
m= float(input('escreva um valor em metros: '))
cm= m*100
mm= m*1000
print('o valor em centímetros é {}cm \no valor em milímetros é {}mm' .format(cm, mm))
