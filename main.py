import time


def obtener_precio():
    try:
        precio_venta_base = int(input("Ingrese el precio de venta base: "))
        return precio_venta_base
    except ValueError:
        print("\n\n❌ Error, ingrese un número entero válido. No se permiten otros caracteres")
        print("Ejemplo válido: 250000, 10000, 2500, 500\n")
        return obtener_precio()


def calcular_precio_venta():
    precio_venta_base = obtener_precio()
    precio_con_iva = precio_venta_base * 1.19
    iva = precio_venta_base * 0.19
    print(f"IVA: ${iva:,.0f} COP")
    print(f"\n\n💰--> Con IVA del 19% lo venderías en: ${precio_con_iva:,.0f} COP")
    print("=================================================")

    time.sleep(1.3)
    calcular_precio_con_comision(precio_con_iva)



def calcular_precio_con_comision(precio_venta_con_iva):

    print("\nTe van a pagar por datáfono?")
    opcion_datafono = input("    1. Sí, comisión del 3%    \n    2. Si, comisión del 3,5%\n    3. No\n\n\t--> :  ")
    if opcion_datafono == "1":
        porcentaje_comision = 3
        precio_con_comision = precio_venta_con_iva * 1.03

    elif opcion_datafono == "2":
        porcentaje_comision = 3.5
        precio_con_comision = precio_venta_con_iva * 1.035

    elif opcion_datafono == "3":
        time.sleep(1.3)
        calcular_precio_con_cuatropormil(precio_venta_con_iva, False)
        return
    else:
        print("\nOpción no válida, por favor ingresa 1,2 o 3.\n")
        time.sleep(1)
        return calcular_precio_con_comision(precio_venta_con_iva)
    
    print(f"\n\n💳--> Con IVA del 19% + comisión {porcentaje_comision}%: ${precio_con_comision:,.0f} COP")
    print("=================================================")
    time.sleep(1.3)
    calcular_precio_con_cuatropormil(precio_con_comision, True)



def calcular_precio_con_cuatropormil(precio, tiene_comision):

    opcion_cuatropormil = input("\n\t¿Desea agregar el 4x1000 a esta venta?\n\t    1. Sí\n\t    2. No\n\n\t\t--> :  ")
    if opcion_cuatropormil == "1":
        precio_con_cuatropormil = precio * 1.004

        if tiene_comision:
            print(f"\n\n🏦--> Con IVA del 19% + comisión + 4x1000: ${precio_con_cuatropormil:,.0f} COP")
        else:
            print(f"\n\n🏦--> Con IVA del 19% + 4x1000: ${precio_con_cuatropormil:,.0f} COP")
        print("=================================================\n")
    elif opcion_cuatropormil == "2":
        return
    else:
        print("\nOpción no válida, por favor ingresa 1 o 2.\n")
        time.sleep(1)
        return calcular_precio_con_cuatropormil(precio)



def otra_consulta():
    repetir_consulta = input("¿Deseas hacer otra consulta?\n1. Sí\n2. No\n\n\t--> :  ")
    if repetir_consulta == "1":
        return True
    elif repetir_consulta == "2":
        return False
    else:
        print("\nOpción no válida, por favor ingresa 1 o 2.\n")
        time.sleep(1)
        return otra_consulta()


################# MENU INTERACTIVO

print("¿No sabes cuánto cobrar por tu producto? calcula el precio de venta exacto, incluyendo todos sus impuestos")
time.sleep(2)
print("\n\nCALCULADORA DE PRECIO DE VENTA")
print("=================================================\n")

while True:
    calcular_precio_venta()
    time.sleep(1)
    
    if not otra_consulta():
        print("\n\nGracias por usar la calculadora de precio de venta...\n\n")
        break 