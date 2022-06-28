print(' ')
print("{:=^80}".format('Calculadora python'))
print(' ')
print('selecione o número da operação desejada:')
print(' ')
print('1-soma \n2-subtração \n3-multiplicação \n4-divisão')
print(' ')

escolha = str(input('digite sua opção (1/2/3/4): '))

print(' ')

def somar ():
    num1 = float(input('digite o primeiro número: '))
    num2 = float(input('digite o segundo número: '))
    soma = num1 + num2
    print('%d + %d = %d'%(num1, num2, soma))

def subtrair ():
    num1 = float(input('digite o primeiro número: '))
    num2 = float(input('digite o segundo número: '))
    subtracao = num1 - num2
    print(' ')
    print('%d - %d = %d'%(num1, num2, subtracao))

def dividir ():
    num1 = float(input('digite o primeiro número: '))
    num2 = float(input('digite o segundo número: '))
    divisao = num1 / num2
    print(' ')
    print('%d / %d = %d'%(num1, num2, divisao))

def multiplicar ():
    num1 = float(input('digite o primeiro número: '))
    num2 = float(input('digite o segundo número: '))
    multiplicacao = num1 * num2
    print(' ')
    print('%d * %d = %d'%(num1, num2, multiplicacao))

if escolha == '1':
    somar()
    print(' ')

elif escolha == '2':
    subtrair()
    print(' ')

elif escolha == '3':
    multiplicar()
    print(' ')

elif escolha == '4':
    dividir()
    print(' ')

else:
    print('opção inválida!')