depositos = ["Haedo", "Tigre", "San Martin", "Florencio Varela", "Mercedes", "Ezeiza", "Jose Leon Suarez"]
tipos = ["cemento", "ladrillo", "cal", "arena", "varilla de acero", "pintura"]
valor = [10,20,30,40,50,60]
planilla = [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]

def castear_numero(numero_ingresado: int, mensaje_error: str) -> int:
    """
    Castea un texto a un numero.
    Parametros: "numero_ingresado" -> valor ingresado
                "mensaje_error" -> mensaje que se va a mostrar en la planilla en el caso de que no se ingrese un valor"
    """
    bandera = True
    for i in range(len(numero_ingresado)):
        if ord(numero_ingresado[i]) < 48 or ord(numero_ingresado[i]) > 57:
            bandera = False 
    if bandera:
        return int(numero_ingresado)
    else: 
        print(mensaje_error)

def get_int(mensaje:str, mensaje_error: str) -> int:
    """
    Funcion para obtener un numero entero positivo.
    Parametros: "mensaje" -> es el mensaje que se le mostrara al usuario para que ingrese un numero
                "mensaje error" -> es el mensaje que se le mostrara al usuario en el caso que no haya ingresado un numero"
    """
    numero = input(mensaje)
    numero_casteado = castear_numero(numero,mensaje_error)

    while type(numero_casteado) != int:
        numero = input(mensaje)
        numero_casteado = castear_numero(numero, mensaje_error)
    return numero_casteado

#Punto 2
def sumar_array(planilla: list) -> int:
    """
    suma los numeros del array.
    parametros: "planilla" -> planilla a la que se le sumaran todos los elementos
    """
    total = 0
    for i in range(len(planilla)):
        total += planilla[i]
    return total
def calcular_elementos_almacenados(planilla: list, depositos: list) -> None:
    """
    Muestra la cantidad de elementos almacenados en cada deposito
    parametros: planilla -> es donde se guardaran los datos obtenidos
                depositos: localidad donde se encuentran los depositos.
    """
    total_elementos = 0
    for i in range(len(planilla)):
        total_elementos = sumar_array(planilla[i])
        print(f"La cantidad de elementos almacenados en el deposito de {depositos[i]} es de {total_elementos}")

#Punto 3
def buscar_menor_array(planilla: list) -> int:
    """
    Busca el elemento con menos cantidad en el array
    parametro: "planilla" -> planilla a recorrer
    Retorno: Devuelve el indice del numero menor en el array
    """
    posicion_menor = 0
    for i in range(len(planilla)):
        if planilla[posicion_menor] > planilla[i]:
            posicion_menor = i
    return posicion_menor

def buscar_elemento_menos_cantidad(planilla: list, depositos: list, tipos: list) -> None:
    """
    Busca el elemento con menor cantidad en cada deposito
    Parametro: "planilla" -> planilla a buscar en cada deposito
                "deposito" -> localidad de cada deposito
                "tipos" -> son los todos los elementos
    """
    for i in range(len(planilla)):
        material_menor = buscar_menor_array(planilla[i])
        print(f"El elemento con menos cantidad en el deposito de {depositos[i]} es: {tipos[material_menor]}")

#Punto 5
def calcular_recaudacion_total(depositos: list, valor: list) -> int:
    """
    Calcular la recaudacion de cada deposito
    Retorna la recaudacion de cada deposito
    """
    recuadacion = 0
    for i in range(len(depositos)):
        recuadacion += depositos[i] * valor[i]
    return recuadacion
def calcular_recaudacion_mayor(planilla: list, depositos: list, valor:list) -> None:
    """
    Devuelve el deposito con mayor recaudacion
    """
recaudacion = 0 
for i in range(len(planilla)):
    recaudacion = calcular_recaudacion_total(planilla[i], valor)
    if planilla[i] > planilla[i + 1]:
        mayor = planilla[i]
#punto 6
def mostrar_mayor_miles(planilla: list, valor:list) -> None:
    contador = 0
    for i in range(len(planilla)):
        recaudado = planilla[i] * valor
        if recaudado > 50000:
            contador += 1
    print(f"Los depositos que recaudaron mas de 50mil materiales fueron: {contador}")
    mostrar_mayor_miles(planilla, valor)

#punto 8
def ordenar_lista_mayor_menor(lista: list) -> list:
    """
    Ordena la lista de mayor a menor
    Retorna la lista ordenada
    """
    reemplazado = 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] < lista[j + 1]:
                reemplazado = lista[j]
                lista[j + 1] = reemplazado
    return lista