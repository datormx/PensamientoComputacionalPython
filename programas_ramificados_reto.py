while True:

    name_1 = input('Escribe el nombre de la primera persona: ')
    age_1 = int(input('Escribe la edad de la persona: '))
    name_2 = input('Escribe el nombre de la segunda persona: ')
    age_2 = int(input('Escribe la edad de la segunda persona: '))

    if age_1 > age_2:
        print(f'{name_1} es mayor que {name_2}')
    elif age_1 < age_2:
        print(f'{name_2} es mayor que {name_1}')
    else:
        print(f'{name_1} tiene la misma edad que {name_2}')

