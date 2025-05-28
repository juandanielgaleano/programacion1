
def mostrar_datos(matriz_notas:list, lista_nombres:list, lista_genero:list, lista_legajo:list):
    
    for i in range(len(matriz_notas)):
        print(f"NOMBRE: {lista_nombres[i]}\nGENERO: {lista_genero[i]}\nLEGAJO: {lista_legajo[i]}\nNOTAS")
        for j in range(matriz_notas[i]):
            print(f"MATERIA_{j+1}: {matriz_notas[i][j]}")
            