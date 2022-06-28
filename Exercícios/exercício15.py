d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

a = (60 * d) + (0.15*km)

print ('O total a pagar é R${:.2f}'.format(a))