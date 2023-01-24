# import
import os
import time

# funções
def limpar():
    os.system("cls")

def erro():
    limpar()
    print("Erro!")
    time.sleep(2.5)

def title():
    limpar()
    print("{:=^40}".format(" Calculadora python "))

def soma(nums):
    soma = sum(nums)
    return soma

def sub(nums):
    subtracao = 0
    for i in nums:
        if nums.index(i) == 0:
            subtracao += i
        else:
            subtracao -= i
    return subtracao

def multi(nums):
    multi = 0
    for i in nums:
        if nums.index(i) == 0:
            multi += i
        else:
            multi *= i
    return multi

def div(nums):
    div = 0
    for i in nums:
        if nums.index(i) == 0:
            div += i
        else:
            div /= i
    return div


# código
limpar()
title()
print("\nQual operação pretende fazer?")
print("\nsoma ==>            +")
print("subtração ==>       -")
print("divisão ==>         /")
print("multiplicação ==>   *\n")
operador = str(input('  '))

lista_num = []
while True:
    limpar()
    title()
    print("\nDigite '=' para a resolver a conta\n")
    print("Digite o número:")
    try:
        block = "abcdefghijklmnopqrstuvwxyz[´`]{;.,:}/?°ºª^~><+-_()*&¨%$#@!'|ç"
        block = list(block)
        num = str(input('     '))
        if num in block:
            raise Exception
        elif num == "=":
            break
        else:
            num = int(num)
            lista_num.append(num)
            continue
    except:
        erro()
        continue

if operador == "+":
    adicao = soma(lista_num)
    print("A soma é:",adicao)
elif operador == "-":
    subtracao = sub(lista_num)
    print("A subtração é:",subtracao)
elif operador == "*":
    multiplicacao = multi(lista_num)
    print("A multiplicação é:",multiplicacao)
elif operador == "/":
    divisao = div(lista_num)
    print("A divisão é:",divisao)