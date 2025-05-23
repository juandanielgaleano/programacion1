def mostrar_menu():
    bandera = True
    while bandera:
        print("[1] - Cargar datos")
        print("[2] - Mostrar datos")
        print("[3] - Calcular promedio")
        print("[4] - Ordenar promedios")
        print("[5] - Mostrar materias con mayor promedio general")
        print("[6] - Mostrar datos de estudiante")
        print("[7] - Mostrar cuantas veces se repite la calificacion de una asignatura")
        print("[8] - Salir")
        opcion = input("Eliga una opcion: ")
        caracter_ascii = ord(opcion)        
        if caracter_ascii >= 49 and caracter_ascii <= 56:
            bandera = False
        else:
            print("ERROR!! NO SELECCIONO UNA OPICION VALIDA \nSeleccione una opcion valida entre el 1 - 8")

    match opcion:
        case 1:
            print("[1] - Cargar datos")
        case 2:
            print("[2] - Mostrar datos")
        case 3:
            print("[3] - Calcular promedio")
        case 4:
            print("[4] - Ordenar promedios")
        case 5:
            print("[5] - Mostrar materias con mayor promedio general")
        case 6:
            print("[6] - Mostrar datos de estudiante")
        case 7:
            print("[7] - Mostrar cuantas veces se repite la calificacion de una asignatura")
        case 8:
            print("[8] - Salir")