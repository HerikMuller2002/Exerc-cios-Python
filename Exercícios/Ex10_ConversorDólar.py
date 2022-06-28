#ConversorDólar
x = float(input('Quanto dinheiro você tem na carteira? R$'))

y = x / 5.24

print('\nCom R${:.2f} você pode comprar US${:.2f}\n'.format(x, y))