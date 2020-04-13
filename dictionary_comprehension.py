def dictionary_comprehension(size_of_numbers):
    squares = {num: num**2 for num in range(1,size_of_numbers + 1)}
    cubes = {num: num**3 for num in range(1,size_of_numbers + 1)}
    doubles = {num: num*2 for num in range(1,size_of_numbers + 1)}

    print(squares, cubes, doubles)

size_of_numbers = int(input('Escribe hasta qué número calcularas los valores cuadrados, al cubo y dobles: '))

dictionary_comprehension(size_of_numbers)

