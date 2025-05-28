
def mostrar_datos(matriz_notas:list, lista_nombres:list, lista_genero:list, lista_legajo:list):
    
    for i in range(len(matriz_notas)):
        print(f"-----ESTUDIANTE {i+1}-----")
        print(f"NOMBRE: {lista_nombres[i]}\nGENERO: {lista_genero[i]}\nLEGAJO: {lista_legajo[i]}\nNOTAS")
        for j in range(len(matriz_notas[i])):
            print(f"MATERIA_{j+1}: {matriz_notas[i][j]}")
        print("---------------------------")   

def mostrar_estudiante(matriz_notas:list, lista_nombres:list, lista_genero:list, lista_legajo:list):
    
    estudiante =  int(input("Ingrese legajo de estudiante a visualizar\n"))
    print("---------------------------") 
    for i in range(len(lista_legajo)):
        if estudiante == lista_legajo[i]:
            print(f"NOMBRE: {lista_nombres[i]}\nGENERO: {lista_genero[i]}\nLEGAJO: {lista_legajo[i]}")
            for j in range(len(matriz_notas[i])):
                print(f"MATERIA_{j+1}: {matriz_notas[i][j]}")
    print("---------------------------") 

def seleccionar_muestreo(matriz_notas:list, lista_nombres:list, lista_genero:list, lista_legajo:list):
    
    while True:        
        print("[1] - Mostrar todos")
        print("[2] - Mostrar un estudiante")       
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
                mostrar_datos(matriz_notas, lista_nombres, lista_genero, lista_legajo)
            case 2:
                mostrar_estudiante(matriz_notas, lista_nombres, lista_genero, lista_legajo)
            case 3:
                print("Saliendo...")
                break