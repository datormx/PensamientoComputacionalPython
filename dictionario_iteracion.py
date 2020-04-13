my_dict = {'Miguel': 25, 'David': 35, 'Juan': 40,}

for llave in my_dict.keys():
    print(f'Llave: {llave}')

for valor in my_dict.values():
    print(f'Valor: {valor}')

for llave, valor in my_dict.items():
    print(f'Llave: {llave}, Valor: {valor}')

print('David' in my_dict)
