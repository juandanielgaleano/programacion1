from funciones import carga_datos
from funciones import mostrar_datos_estudiantes
from funciones import promedios
from funciones import ordenamiento

def mostrar_menu(matriz_notas: list, lista_nombres: list, lista_generos: list, lista_legajos: list):

    promedios = [0.0] * 30
    datos_cargados = False
    while True: 
        
        print("\n--- Menú Principal ---")
        print("[1] - Cargar datos")
        print("[2] - Mostrar datos")
        print("[3] - Calcular promedio")
        print("[4] - Ordenar promedios")
        print("[5] - Mostrar materias con mayor promedio general")
        print("[6] - Mostrar datos de estudiante")
        print("[7] - Mostrar cuantas veces se repite la calificación de una asignatura")
        print("[8] - Salir")        
        opcion_valida = False
        opcion = input("\nElija una opción (1-8): ")       
        if len(opcion) == 1:
            codigo = ord(opcion)
            if 49 <= codigo <= 56:
                opcion = int(opcion)
                opcion_valida = True        
        if not opcion_valida:
            print("\nERROR: Debe ingresar un número entre 1 y 8")
            continue
        if not datos_cargados and  (opcion >= 2 and opcion <= 7):  
            print("\nERROR: Debe cargar datos primero (Opción 1)")
            continue      
        match opcion:
            case 1:                
                carga_datos.cargar_datos_en_matriz(matriz_notas, lista_nombres, lista_generos, lista_legajos)
                datos_cargados = True
            case 2:                
                mostrar_datos_estudiantes.seleccionar_muestreo(matriz_notas, lista_nombres, lista_generos, lista_legajos)
            case 3:
                print("\n[3] - Calcular promedio")
                promedios = promedios.calcular_promedios(matriz_notas)
            case 4:
                print("\n[4] - Ordenar promedios")
                ordenamiento.seleccionar_orden(matriz_notas, lista_nombres, lista_generos, lista_legajos,promedios)
            case 5:
                print("\n[5] - Mostrar materias con mayor promedio general")
                
            case 6:
                print("\n[6] - Mostrar datos de estudiante")
                
            case 7:
                print("\n[7] - Mostrar cuantas veces se repite la calificación de una asignatura")
                
            case 8:
                print("\nSaliendo del programa...")
                break

        
        input("\nPresione Enter para continuar...")