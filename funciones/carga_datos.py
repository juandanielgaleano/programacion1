
#matriz de notas
matriz_notas_estudiantes = [
    [4, 7, 2, 9, 1],
    [6, 3, 8, 5, 10],
    [2, 2, 4, 7, 6],
    [9, 1, 5, 3, 8],
    [10, 4, 6, 2, 7],
    [3, 5, 9, 1, 4],
    [7, 8, 3, 6, 2],
    [1, 6, 10, 4, 5],
    [5, 9, 7, 8, 3],
    [8, 2, 1, 10, 9],
    [4, 3, 6, 5, 7],
    [2, 7, 8, 1, 6],
    [9, 5, 4, 3, 10],
    [6, 1, 2, 7, 8],
    [3, 8, 5, 9, 4],
    [10, 4, 7, 2, 1],
    [5, 6, 3, 8, 9],
    [7, 2, 9, 4, 5],
    [1, 10, 6, 3, 7],
    [8, 3, 4, 5, 2],
    [4, 9, 1, 6, 10],
    [2, 5, 8, 7, 3],
    [6, 7, 10, 1, 4],
    [3, 1, 5, 9, 8],
    [9, 8, 2, 4, 6],
    [5, 4, 7, 10, 1],
    [10, 6, 3, 2, 5],
    [7, 3, 9, 8, 4],
    [1, 2, 6, 5, 9],
    [8, 5, 4, 3, 7]
]
#Lista de nombres
nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sofía', 'Jorge', 'Elena', 
 'David', 'Isabel', 'Pedro', 'Carmen', 'Alejandro', 'Patricia', 'Francisco', 'Lucía', 
 'Daniel', 'Adriana', 'Roberto', 'Verónica', 'José', 'Gabriela', 'Fernando', 'Raquel', 
 'Ricardo', 'Beatriz', 'Manuel', 'Natalia']

#lista de generos
genero = [
    'M', 'F', 'M', 'F', 'X',
    'F', 'M', 'F', 'X', 'F',
    'M', 'F', 'M', 'X', 'M',
    'F', 'M', 'F', 'X', 'F',
    'M', 'F', 'M', 'X', 'M',
    'F', 'M', 'F', 'X', 'F'
]

#Lista de legajos
legajos = [
    10023, 24578, 38912, 41235, 56789,
    62401, 73562, 89014, 90125, 10236,
    23457, 34568, 45679, 56780, 67891,
    78902, 89013, 90124, 12340, 23451,
    34562, 45673, 56784, 67895, 78906,
    89017, 90128, 12349, 23450, 34561
]

def cargar_nombre()->str:
    bandera = True
    while bandera:
        nombre = input("Ingresar nombre del alumno:" )
        for i in range(len(nombre)):
            caracter_ascii = ord(i)
            if caracter_ascii >= 65 and caracter_ascii <= 90 or caracter_ascii >= 97 and caracter_ascii <= 122:
                bandera = False
            else:
                print("ERROR!! INGRESO UN CARACTER ERRONEO - SOLO INGRESAR LETRAS")
    return nombre        

def cargar_genero()->str:
    bandera = True
    while bandera:
        genero = input("Ingresar genero del estudiante: (F)- (M) - (X)")
        if len(genero) == 1:
            caracter_ascii = ord(genero)
            if caracter_ascii == 70 or caracter_ascii == 77 or caracter_ascii == 88 or caracter_ascii == 102 or caracter_ascii == 109 or caracter_ascii == 120:
                bandera = False
        else:
            print("ERORR!! SOLO INGRESAR 1 CARACTER (F) or (M) or (X)")
    return genero

def cargar_legajo()->int:
    bandera = True
    while bandera:
        legajo = input("Ingresar legajo del estudiante: (5 cifras numeros enteros)")
        if len(legajo) == 5:
            for i in range(len(legajo)):
                caracter_ascii = ord(legajo[i])
                if caracter_ascii >=48 and caracter_ascii <=57:
                    bandera = False
        else:
            print("ERORR!!! INGRESE SOLO NUMEROs. DEBEN SER CINCO")
    return legajo

def cargar_datos():
    bandera = True   
    nombre = cargar_nombre()

    
    
