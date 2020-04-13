estudiantes = {
    'méxico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes: #Obtiene las llaves del diccionario
    print(pais)

for pais in estudiantes.keys(): #Obtiene las llaves del diccionario
    print(pais)

for numero_de_estudiantes in estudiantes.values(): #Obtiene los valores del diccionario
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items(): #Obtiene las llaves y los valores del diccionario
    print(pais, numero_de_estudiantes)