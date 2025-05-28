from funciones import menu

#matriz de notas
matriz_notas_estudiantes = [
    [4, 7, 2, 9, 1],
    [6, 3, 8, 5, 10],
    [2, 2, 4, 7, 6],
    [9, 0, 5, 3, 8],
    [10, 4, 6, 2, 7],
    [3, 5, 9, 1, 0],
    [7, 8, 3, 6, 2],
    [1, 6, 10, 4, 5],
    [5, 9, 0, 8, 3],
    [8, 2, 1, 10, 9],
    [4, 3, 6, 0, 7],
    [2, 7, 8, 1, 6],
    [9, 5, 4, 3, 10],
    [6, 1, 0, 7, 8],
    [None, '', None, '', None],  # Posición 15 modificada
    [10, 4, 7, 2, 1],
    [5, 6, 3, 8, 0],
    [7, 2, 9, 4, 5],
    [1, 10, 6, 0, 7],
    [8, 3, 4, 5, 2],
    [4, 9, 1, 6, 10],
    [2, 5, 8, 7, 3],
    [6, 7, 10, 1, 4],
    [3, 1, 0, 9, 8],
    [9, 8, 2, 4, 6],
    [5, 4, 7, 10, 1],
    [10, 6, 3, 2, 5],
    [7, 3, 9, 8, 4],
    [1, 2, 6, 5, 9],
    [8, 0, 4, 3, 7]]
#lista de nombres
nombres = [
    'Juan', 'María', 'Luis', 'Carlos', 'Ana', 
    'Pedro', 'Sofía', 'Laura', 'Miguel', 'Carmen', 
    'Elena', 'Jorge', 'David', 'Isabel', '',  # Posición 15 modificada
    'Patricia', 'Lucía', 'Daniel', 'Adriana', 'Alejandro', 
    'Roberto', 'Verónica', 'José', 'Gabriela', 'Francisco', 
    'Raquel', 'Ricardo', 'Beatriz', 'Manuel', 'Natalia']
#lista de generos
generos = [
    'M', 'F', 'M', 'M', 'X',
    'F', 'M', 'F', 'X', 'F',
    'M', 'M', 'M', 'X', '',  # Posición 15 modificada
    'F', 'M', 'F', 'X', 'F',
    'M', 'F', 'M', 'X', 'M',
    'F', 'M', 'F', 'M', 'F']
#lista de legajos
legajos = [
    10023, 24578, 41235, 35671, 56789,
    62401, 73159, 89014, 90125, 10236,
    23457, 34568, 45679, 56780, '',  # Posición 15 con '' (índice 14)
    67891, 78902, 81234, 90124, 12340,
    23451, 34562, 45673, 56784, 67895,
    78906, 89017, 90128, 12349, 23450
]
menu.mostrar_menu(matriz_notas_estudiantes,nombres,generos,legajos)
