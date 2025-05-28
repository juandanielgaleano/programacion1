
def calcular_promedios(matriz_notas:list)->list:

    promedios = [0.0] * 30
    for i in range(len(matriz_notas)):
        for j in range(len(matriz_notas[i])):
            promedios[i] += matriz_notas[i][j]
        promedios[i] = promedios[i] / 5
    
    return promedios