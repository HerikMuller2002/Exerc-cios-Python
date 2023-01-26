produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

new_produtos = produtos.copy()

for i in range(5):
    new_preco = produtos[i]['preco']* 1.1
    new_produtos[i]['preco'] = '{:.2f}'.format(new_preco)

print(new_produtos)