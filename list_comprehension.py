def list_comprension(my_list):
    pares = [i for i in my_list if i % 2 == 0]
    doubles = [i**2 for i in my_list]

    print(f'Pares: {pares}\n')
    print(f'Dobles: {doubles}\n')

my_list = range(100)

list_comprension(my_list)
