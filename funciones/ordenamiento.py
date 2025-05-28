from funciones import mostrar_datos_estudiantes
def ordenar_ascendente(matriz_notas: list, lista_nombres: list, lista_genero: list,lista_legajo: list, lista_promedios: list):

    for i in range(len(lista_promedios)):        
        for j in range(len(lista_promedios) - i - 1):
            if lista_promedios[j] > lista_promedios[j + 1]:                
                aux_promedios = lista_promedios[j]
                lista_promedios[j] = lista_promedios[j + 1]
                lista_promedios[j + 1] = aux_promedios              
                
                aux_nombre = lista_nombres[j]
                lista_nombres[j] = lista_nombres[j + 1]
                lista_nombres[j + 1] = aux_nombre

                aux_genero = lista_genero[j]
                lista_genero[j] = lista_genero[j + 1]
                lista_genero[j + 1] = aux_genero
                
                aux_legajo = lista_legajo[j]
                lista_legajo[j] = lista_legajo[j + 1]
                lista_legajo[j + 1] = aux_legajo
                
                aux_notas = matriz_notas[j]
                matriz_notas[j] = matriz_notas[j + 1]
                matriz_notas[j + 1] = aux_notas       
    mostrar_datos_estudiantes.mostrar_datos(matriz_notas,lista_nombres,lista_genero,lista_legajo)
    


def ordenar_descendente(matriz_notas: list, lista_nombres: list, lista_genero: list,lista_legajo: list, lista_promedios: list):
    for i in range(len(lista_promedios)):        
        for j in range(len(lista_promedios) - i - 1):
            if lista_promedios[j] < lista_promedios[j + 1]:                
                aux_promedios = lista_promedios[j]
                lista_promedios[j] = lista_promedios[j + 1]
                lista_promedios[j + 1] = aux_promedios              
                
                aux_nombre = lista_nombres[j]
                lista_nombres[j] = lista_nombres[j + 1]
                lista_nombres[j + 1] = aux_nombre

                aux_genero = lista_genero[j]
                lista_genero[j] = lista_genero[j + 1]
                lista_genero[j + 1] = aux_genero
                
                aux_legajo = lista_legajo[j]
                lista_legajo[j] = lista_legajo[j + 1]
                lista_legajo[j + 1] = aux_legajo
                
                aux_notas = matriz_notas[j]
                matriz_notas[j] = matriz_notas[j + 1]
                matriz_notas[j + 1] = aux_notas 
    mostrar_datos_estudiantes.mostrar_datos(matriz_notas,lista_nombres,lista_genero,lista_legajo)


def seleccionar_orden(matriz_notas: list, lista_nombres: list, lista_genero: list,lista_legajo: list, lista_promedios: list):
    while True:        
        print("[1] - Ordenar ascendente")
        print("[2] - Ordenar descendente")       
        print("[3] - Salir")       
        opcion_valida = False
        opcion = input("\nElija una opción (1-3): ")       
        if len(opcion) == 1:
            codigo = ord(opcion)
            if 49 <= codigo <= 51:
                opcion = int(opcion)
                opcion_valida = True        
        if not opcion_valida:
            print("\nERROR: Debe ingresar un número entre 1 y 3")
            continue
        match opcion:
            case 1:
                ordenar_ascendente(matriz_notas, lista_nombres, lista_genero, lista_legajo,lista_promedios)
            case 2:
                ordenar_descendente(matriz_notas, lista_nombres, lista_genero, lista_legajo,lista_promedios)
            case 3:
                print("Saliendo...")
                break