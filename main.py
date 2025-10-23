import generales

depositos = ["Haedo", "Tigre", "San Martin", "Florencio Varela", "Mercedes", "Ezeiza", "Jose Leon Suarez"]
tipos = ["cemento", "ladrillo", "cal", "arena", "varilla de acero", "pintura"]
valor = [10,20,30,40,50,60]
planilla = [[0,3,0,40,0,0],
            [33,0,0,0,50,0],
            [0,0,53,0,33,0],
            [60,0,0,5,0,0],
            [0,4,0,0,80,0],
            [33,0,44,0,0,0],
            [0,4,0,43,0,0]]

def existencias(planilla: list, depositos: list, tipos: list) -> int:
    for i in range(len(planilla)):
        for j in range(len(planilla[i])):
            planilla [i][j]= planilla[i][j] + generales.get_int(f"La cantidad de {tipos} en el deposito de {depositos} es: ", "Porfavor ingrese la cantidad")

bandera = True
while bandera: 
    desicion = 0
    print("--------")
    print("1- Cargar planilla de elementos")
    print("2- Mostrar la cantidad de elementos de cada deposito")
    print("3- Material con menos cantidad")
    print("4- Deposito con más cantidad de cada material")
    print("5- Deposito con mayor recaudacion")
    print("6- Cantidad de depositos que hayan almacenado más de 50mil entre todos los materiales")
    print("7- Porcentaje de cada material y el mayor porcentaje")
    print("8- Mostrar la recaudacion de cada deposito ordenada de mayor a menor")
    print("9- Salir del menu")
    print("--------")

    desicion = generales.get_int("Elija una de las opciones: ", "Opcion no valida")

    match desicion:
        case 1: 
            for i in range(len(planilla)):
                for j in range(len(planilla[i])):
                    dato = generales.get_int(f"La cantidad de {tipos[j]} en el deposito de {depositos[i]} es: ", "Porfavor ingrese la cantidad")
                    planilla[i][j] = dato
                
        case 2: 
            generales.calcular_elementos_almacenados(planilla, depositos)
        case 3: 
            generales.buscar_elemento_menos_cantidad(planilla, depositos, tipos)
        case 5: 
            generales.calcular_recaudacion_total(depositos, valor)
        case 6:
            generales.mostrar_mayor_miles(planilla, valor)
        case 8:
            recaudacion = [False] * len(depositos)
            for i in range(len(recaudacion)):
                recaudacion[i] = generales.calcular_recaudacion_total(planilla[i], valor)
            recaudacion = generales.ordenar_lista_mayor_menor(recaudacion)
            print(f"La recaudacion de los depositos es de: ")
            for i in range(len(recaudacion)):
                print(f"{i+1} - {recaudacion[i]}$ ", end = "")
        case 9:
            print("Adios")
            bandera = False