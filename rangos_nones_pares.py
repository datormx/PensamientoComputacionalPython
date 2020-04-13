def pares(limit):
    for i in range(0, limit + 1, 2):
        print(f'Par: {i}')

def nones(limit):
    for i in range(1, limit, 2):
        print(f'Non: {i}')


limit = int(input('Escribe hasta que número imprimir los números pares y nones: '))
pares(limit)
nones(limit)
