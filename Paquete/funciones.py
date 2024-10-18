from random import randint

def crear_matriz(filas:int,columnas:int,valor_inicialización:any)->list:
    """Crea una matriz con las filas y columnas ingresadas
    Args:
        filas (int): cantidad de filas
        columnas (int): cantidad de columnas
        valor_inicializacion: valor que se le asigna a cada celda creada
    Returns:
        list: la matriz creada
    """
    matriz = []
    for _ in range(filas):
        fila = [valor_inicialización] * columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    """muestra en consola de forma agradable a la vista una matriz ingresada
    Args:
        matriz (list): matriz a mostrar
    """
    for i in range(len(matriz)):
        print(f"N°{i+1}")
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]}",end="\t\t")
        print()

def mostrar_lista(lista:list):
    for i in range(len(lista)):
        print(f"N°{i+1}:{lista[i]}")

def cargar_clientes_random(cantidad_clientes,cantidad_tamaños)->list:
    planilla = crear_matriz(cantidad_clientes,cantidad_tamaños,0)
    for i in range(len(planilla)):
        cantidad_paquetes = randint(0,5)
        if cantidad_paquetes > 0:
            for _ in range(cantidad_paquetes):
                tipo_paquete = randint(1,3)
                match tipo_paquete:
                    case 1:
                        planilla[i][0] += 1
                    case 2:
                        planilla[i][1] += 1
                    case 3:
                        planilla[i][2] += 1
    return planilla


def contar_paquetes_clientes(planilla_clientes:list)->list:
    planilla_total_clientes = crear_matriz(len(planilla_clientes),1,0)
    for i in range(len(planilla_clientes)):
        acumulador_cliente = 0
        for j in range(len(planilla_clientes[i])):
            acumulador_cliente += planilla_clientes[i][j]
        planilla_total_clientes[i][0] = acumulador_cliente
    return planilla_total_clientes

# total_clientes = contar_paquetes_clientes(clientes)
# print("Total de paquetes por cliente")
# mostrar_matriz(total_clientes)

def contar_clientes_solo_medianos(planilla_clientes:list)->int:
    contador_clientes_solo_medianos = 0
    for i in range(len(planilla_clientes)):
        if planilla_clientes[i][0] == 0 and planilla_clientes[i][2] == 0:
            contador_clientes_solo_medianos += 1
    return contador_clientes_solo_medianos

# contador_medianos = contar_clientes_solo_medianos(clientes)
# print(contador_medianos)

def calcular_totales_a_pagar(planilla_clientes:list)->list:
    totales_a_pagar = [None] * len(planilla_clientes)
    precio_envios = [1000,1500,2000]
    for i in range(len(planilla_clientes)):
        acumulador_precios = 0
        for j in range(len(planilla_clientes[i])):
            acumulador_precios += precio_envios[j] * planilla_clientes[i][j]
        totales_a_pagar[i] = acumulador_precios
    return totales_a_pagar


def ordenar_a_pagar_descendente(planilla_clientes:list)->list:
    totales_a_pagar = calcular_totales_a_pagar(planilla_clientes)
    for i in range(len(totales_a_pagar)-1):
        for j in range(i+1,len(totales_a_pagar)):
            if totales_a_pagar[i] < totales_a_pagar[j]:
                aux = totales_a_pagar[i]
                totales_a_pagar[i] = totales_a_pagar[j]
                totales_a_pagar[j] = aux
    return totales_a_pagar

# totales_descendete = ordenar_a_pagar_descendente(clientes)
# mostrar_lista(totales_descendete)

def calcular_total_recaudacion_por_tamaño(planilla_clientes:list)->list:
    recaudacion_paquetes = [0] * len(planilla_clientes[0])
    precio_envios = [1000,1500,2000]
    for i in range(len(planilla_clientes[0])):
        acumulador_paquetes = 0
        for j in range(len(planilla_clientes)):
            acumulador_paquetes += planilla_clientes[j][i] * precio_envios[i]
        recaudacion_paquetes[i] += acumulador_paquetes
    return recaudacion_paquetes

def calcular_tamaño_mayor_recaudacion(planilla_clientes:list)->str:
    recaudacion_por_tamaño = calcular_total_recaudacion_por_tamaño(planilla_clientes)
    tamaños = ["pequeño","mediano","grande"]
    tamaño_mayor_recaudacion = tamaños[0]
    mayor_recaudacion = recaudacion_por_tamaño[0]
    for i in range(1,len(recaudacion_por_tamaño)):
        if recaudacion_por_tamaño[i] > mayor_recaudacion:
            mayor_recaudacion = recaudacion_por_tamaño[i]
            tamaño_mayor_recaudacion = tamaños[i]
    
    return tamaño_mayor_recaudacion



# recaudacion_por_paquete = total_recaudacion_por_tamaño(clientes)
# print(recaudacion_por_paquete)

# tamaño_mas_recaudo = calcular_tamaño_mayor_recaudacion(clientes)
# print(tamaño_mas_recaudo)

def calcular_clientes_mas_paquetes_medianos(planilla_clientes:list):
    clientes_mas_paquetes_medianos = []
    mayor_envios_medianos = planilla_clientes[0][1]
    for i in range(1,len(planilla_clientes)):
        if planilla_clientes[i][1] > mayor_envios_medianos:
            mayor_envios_medianos = planilla_clientes[i][1]
    for i in range(len(planilla_clientes)):
        if mayor_envios_medianos == planilla_clientes[i][1]:
            clientes_mas_paquetes_medianos += [f"Cliente N°{i+1}"]
    return clientes_mas_paquetes_medianos

# medianos = calcular_clientes_mas_paquetes_medianos(clientes)
# print("El/Los clientes que enviaron mas medianos:")
# mostrar_lista(medianos)

    
