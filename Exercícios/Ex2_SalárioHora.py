#Salário/hora
salario = float(input('quanto vc ganha por mês:'))
horas = float(input('quantas horas vc trabalha por mês:'))

SH = salario / horas

print(' Salário por hora = R$%{:.2f}' .format(SH))