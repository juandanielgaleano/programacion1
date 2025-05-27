from funciones import menu

#matriz de notas
matriz_notas_estudiantes = [
    [4, 7, 2, 9, 1],
    [6, 3, 8, 5, 10],
    [2, 2, 4, 7, 6],
    [9, None, 5, 3, 8],
    [10, 4, 6, 2, 7],
    [3, 5, 9, 1, None],
    [7, 8, 3, 6, 2],
    [1, 6, 10, 4, 5],
    [5, 9, None, 8, 3],
    [8, 2, 1, 10, 9],
    [4, 3, 6, None, 7],
    [2, 7, 8, 1, 6],
    [9, 5, 4, 3, 10],
    [6, 1, None, 7, 8],
    [3, 8, 5, 9, 4],
    [10, 4, 7, 2, 1],
    [5, 6, 3, 8, None],
    [7, 2, 9, 4, 5],
    [1, 10, 6, None, 7],
    [8, 3, 4, 5, 2],
    [4, 9, 1, 6, 10],
    [2, 5, 8, 7, 3],
    [6, 7, 10, 1, 4],
    [3, 1, None, 9, 8],
    [9, 8, 2, 4, 6],
    [5, 4, 7, 10, 1],
    [10, 6, 3, 2, 5],
    [7, 3, 9, 8, 4],
    [1, 2, 6, 5, 9],
    [8, None, 4, 3, 7]]
#lista de nombres
nombres = [
    'Juan', 'María', '', 'Carlos', 'Ana', '', 'Luis', 'Laura', 'Miguel', '', 
    'Sofía', 'Jorge', 'Elena', '', 'David', 'Isabel', 'Pedro', '', 'Carmen', 
    'Alejandro', 'Patricia', '', 'Francisco', 'Lucía', 'Daniel', '', 'Adriana', 
    'Roberto', 'Verónica', '', 'José', 'Gabriela', 'Fernando', '', 'Raquel', 
    'Ricardo', 'Beatriz', '', 'Manuel', 'Natalia', '']
#lista de generos
generos = [
    'M', 'F', 'M', None, 'X',
    'F', '', 'F', 'X', 'F',
    'M', None, 'M', 'X', 'M',
    'F', 'M', '', 'X', 'F',
    'M', 'F', None, 'X', 'M',
    'F', 'M', 'F', '', 'F'
    ]
#Lista de legajos
legajos = [
    10023, 24578, None, 41235, 56789,
    62401, '', 89014, 90125, 10236,
    23457, 34568, None, 56780, 67891,
    78902, '', 90124, 12340, 23451,
    34562, 45673, None, 67895, 78906,
    '', 90128, 12349, 23450, 34561
]

menu.mostrar_menu(matriz_notas_estudiantes,nombres,generos,legajos)
