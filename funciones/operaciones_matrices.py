'''Inicializar matriz'''
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

'''suma de matriz'''
def sumar_matriz(matriz_uno:list, matriz_dos:list) -> list:
    matriz_resultado = inicializar_matriz(len(matriz_uno), len(matriz_uno[0]), 0)
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_uno[i])):
            matriz_resultado[i][j] = matriz_uno[i][j] + matriz_dos[i][j]
    return matriz_resultado


'''Escalar de una matriz'''
def escalar_matriz(matriz_uno:list, escalar:int) -> list:
    matriz_resultado = inicializar_matriz(len(matriz_uno), len(matriz_uno[0]), 0)
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_uno[i])):
            matriz_resultado[i][j] = matriz_uno[i][j] * escalar
    return matriz_resultado
