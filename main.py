from Paquete.funciones import *
from os import system

planilla_clientes = cargar_clientes_random(15,3)
print(planilla_clientes)
while True:
    print("Sistema de gestios de Envíos")
    print("Selecciona una opción:\n1. Cantidad de paquetes que envía cada cliente\n2. Cantidad de clientes que no enviaron ni paquetes pequeños ni grandes\n3. Totales a pagar de forma descendente\n4. Totales de recaudacion por tamaños. Y tamaño que mas recuadó\n5. Cliente/s que más paquete medianos envió\n6. Salir")
    opcion = input("Escribe la opción deseada: ")
    match opcion:
        case "1":
            print("Cantidad de paquetes que envía cada cliente:")
            totales_clientes = contar_paquetes_clientes(planilla_clientes)
            mostrar_matriz(totales_clientes)
        case "2":
            cantidad_clientes_solo_medianos = contar_clientes_solo_medianos(planilla_clientes)
            if cantidad_clientes_solo_medianos > 0:    
                print(f"Hay {cantidad_clientes_solo_medianos} cliente/s que no mandaron paquetes pequeños ni medianos")
            else:
                print("No hay clientes que no hayan mandado paquetes grandes ni pequeños")
        case "3":
            totales_a_pagar = ordenar_a_pagar_descendente(planilla_clientes)
            print("Totales a pagar de clientes (descendente):")
            mostrar_lista(totales_a_pagar)
        case "4":
            total_recaudacion_tamaños = calcular_total_recaudacion_por_tamaño(planilla_clientes)
            mostrar_lista(total_recaudacion_tamaños)
            print(f"El tamaño que mas recaudó es el {calcular_tamaño_mayor_recaudacion(planilla_clientes)}")
        case "5":
            clientes_mas_medianos = calcular_clientes_mas_paquetes_medianos(planilla_clientes)
            print("El/Los clientes que enviaron mas medianos:")
            mostrar_lista(clientes_mas_medianos)
        case "6":
            print("saliendo...")
            break
        case _:
            print("Opción inválida")
    system("pause")
    system("cls")