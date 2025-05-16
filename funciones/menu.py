def mostrar_menu()->int:
    bandera = True
    while bandera:
        print("[1] - Cargar datos")
        print("[2] - Mostrar datos")
        print("[3] - Calcular promedio")
        print("[4] - Ordenar promedios")
        opcion = input("Eliga una opcion: ")
        if opcion >= 1 and opcion <= 4:
            bandera = False
        else:
            print("Seleccione una opcion valida entre el 1 - 4")
    return opcion