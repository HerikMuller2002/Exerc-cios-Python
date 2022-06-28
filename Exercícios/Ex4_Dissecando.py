#Dissecando
num = input('\ndigite algo: ')

print('\nQual o tipo primitivo?', type(num))
print('É um número?', num.isnumeric())
print('É alfabético?', num.isalpha())
print('É alfanumérico?', num.isalnum())
print('Só tem espaço?', num.isspace())
print('Está em minúscula?', num.islower())
print('Está em maiúscula?', num.isupper())
print('Está capitalizada?', num.istitle())