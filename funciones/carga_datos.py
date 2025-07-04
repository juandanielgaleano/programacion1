
def validar_nombre()->str:
    """Al ingresar un nombre valida que no tenga espacios al principio y al final. Tampoco puede exceder los 10 caracteres ni ser menor a 2

    Returns:
        str: devuelve un nombre validado que solo utilice caracteres alfabeticos
    """    
    bandera = True
    while bandera:
        contador = 0
        nombre = input("Ingresar nombre del alumno:\n" )
        if nombre == '':
            print("Nombre invalido")
            continue
        if nombre[-1] == ' ' or nombre[0] == ' ':
            print("El nombre no puede terminar o comenzar con un caracter vacio")
            continue
        if len(nombre) > 10 or len(nombre) <= 1:
            print("Nombre largo o muy corto, maximo 10 caracteres")
            continue
        else:
            for i in range(len(nombre)):
                caracter_ascii = ord(str(nombre[i]))
                if caracter_ascii >= 65 and caracter_ascii <= 90 or caracter_ascii >= 97 and caracter_ascii <= 122:
                    contador += 1
                    if contador == len(nombre):
                        bandera = False
                else:
                    print("ERROR!! INGRESO UN CARACTER ERRONEO - SOLO INGRESAR LETRAS")
                    break
    return nombre        

def validar_genero()->str:
    """Valida que el genero sea f x m puede ser mayuscula o minuscula. No permite caracteres especiales ni numeros. Solo se permite 1 caracter

    Returns:
        str: devuelve un caracter validado
    """    
    bandera = True
    while bandera:
        genero = input("Ingresar genero del estudiante: (F)- (M) - (X)\n")
        if len(genero) == 1:
            caracter_ascii = ord(genero)
            if caracter_ascii == 70 or caracter_ascii == 77 or caracter_ascii == 88 or caracter_ascii == 102 or caracter_ascii == 109 or caracter_ascii == 120:
                bandera = False
            else:
                print("ERROR!!Ingreso un caracter invalido")                
                continue
        else:
            print("ERORR!! SOLO INGRESAR 1 CARACTER (F) or (M) or (X)")
    return genero

def validar_legajo()->int:
    """Valida que el legajo sean 5 numero enteros. no puede ser merno o mayor a 5

    Returns:
        int: devuelve un legajo validado
    """    
    bandera = True
    while bandera:
        legajo = input("Ingresar legajo del estudiante: (5 cifras numeros enteros)")
        if len(legajo) == 5:
            for i in range(len(legajo)):
                caracter_ascii = ord(legajo[i])
                if caracter_ascii >=48 and caracter_ascii <=57:
                    bandera = False
        else:
            print("ERORR!!! INGRESE SOLO NUMEROS. DEBEN SER CINCO")
    return legajo

def validar_nota() -> int:
    """La funcion valida que la nota solo sea numerica como maximo 10. 

    Returns:
        int: devuelve un numero validado entre el 1 y 10
    """    
    bandera = True
    nota_valida = None 
    while bandera:
        nota = input("Cargar nota de estudiante (1 al 10): ")
        es_valida = True
        if len(nota) == 0 or len(nota) > 2:
            print("ERROR: Debe ingresar 1 o 2 cifras")
            continue
        for caracter in nota:
            caracter_ascii = ord(caracter)
            if caracter_ascii < 48 or caracter_ascii > 57:
                es_valida = False
                break           
        if not es_valida:
            print("ERROR: Solo se permiten números")
            continue
        entero = int(nota)
        if 1 <= entero <= 10:
            nota_valida = entero
            bandera = False
        else:
            print("ERROR: La nota debe estar entre 1 y 10")
    
    return nota_valida

def cargar_datos_en_matriz(matriz_notas_estudiantes:list, nombres:list, generos:list, legajos:list):
    """la funcion recorre la matriz y verifica que si no tiene datos cargados se puede completar

    Args:
        matriz_notas_estudiantes (list): matriz de enteros
        nombres (list): espera una lista de cadenas
        generos (list): espera una lista con caracteres
        legajos (list): espera una lista de legajos
    """    
    for i in range(len(matriz_notas_estudiantes)):
        for j in range(len(matriz_notas_estudiantes[i])):
            if matriz_notas_estudiantes[i][j] == None or matriz_notas_estudiantes[i][j] == '':
                print(f"Se encontro una posicion para cargar nota.\nlegajo: {legajos[i]}\ngenero: {generos[i]}\nnombre: {nombres[i]}\nMATERIA_{j+1}")                
                matriz_notas_estudiantes[i][j] = validar_nota()
            if nombres[i] == None or len(nombres[i]) < 1:
                print("Debe cargar un nombre para el estudiante")
                nombres[i] = validar_nombre()
            if generos[i] == None or len(generos[i]) < 1:
                print(f"Debe cargar un genero para el estudiante {nombres[i]}")
                generos[i] = validar_genero()            
            if legajos[i] == None or legajos[i] == '':
                print(f"El estudiante {nombres[i]} tiene legajo vacio o erroneo")
                bandera = True
                while bandera:
                    unico = True
                    legajo_unico = int(validar_legajo())                    
                    for k in range(len(legajos)):                                                
                        if legajos[k] == legajo_unico:                            
                            print("El legajo debe ser unico para cada estudiante")                            
                            unico = False
                            break
                    if unico:
                        legajos[i] = legajo_unico
                        bandera = False
            
