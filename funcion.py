def suma(a, b):
    total = a + b
    return total

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

    
res = suma(2, 3)
print(res)


name1 = nombre_completo('David', 'Aroesti')
print(name1)
name2 = nombre_completo('David', 'Aroesti', inverso = True)
print(name2)
name3 = nombre_completo(apellido = 'Aroesti', nombre = 'David')
print(name3)