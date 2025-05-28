
def calcular_promedio_materias(matriz_notas:list):

    materia_1 = 0.0
    materia_2 = 0.0
    materia_3 = 0.0
    materia_4 = 0.0
    materia_5 = 0.0
    for i in range(len(matriz_notas)):
        
        materia_1 += matriz_notas[i][0]
        materia_2 += matriz_notas[i][1]
        materia_3 += matriz_notas[i][2]
        materia_4 += matriz_notas[i][3]
        materia_5 += matriz_notas[i][4]
    
    materia_1_promedio = materia_1 / 30
    materia_2_promedio = materia_2 / 30
    materia_3_promedio = materia_3 / 30
    materia_4_promedio = materia_4 / 30
    materia_5_promedio = materia_5 / 30

    print(f"PROMEDIO MATERIA_")