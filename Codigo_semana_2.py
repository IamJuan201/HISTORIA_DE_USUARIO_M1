# TASK 5
# 5. Documentación y limpieza del código:
# Comenta el código explicando la funcionalidad de cada sección (menú, bucle, validación, estadísticas).
# Estructura el código en funciones simples:

# agregar_producto()
# mostrar_inventario()
# calcular_estadisticas()
# Deja un comentario final resumiendo el objetivo de la semana.
 
# Criterios de aceptación
# El menú debe manejar opciones inválidas sin cerrar el programa.

# Variables globales
n = 60
inventario = []
productos_registrados = 0
total = 0

# Menu de opciones para el usuario

def menu_opciones():
    print("="*n)
    print("REGISTRO DE VENTAS".center(n))
    print("="*n)
    print('\n1. Agregar productos')
    print('2. Mostrar productos')
    print('3. Calcular estadisticas')
    print('4. Salir\n\n')
    print("="*n)
    opcion = int(input("Ingrese la opcion que desea realizar (1-4): "))
    return opcion

def agregar_productos(inventario, total, productos_registrados):
    elecion = 'si'
    while elecion == 'si':
        print("="*n)
        nombre_producto = input("Nombre del producto: ")

        try:
            precio_producto = float(input("Precio del producto: "))
            Unidades_producto = int(input("Unidades del producto: "))
            
            subtotal = precio_producto * Unidades_producto
            total += subtotal
            productos_registrados += 1

            producto = {"Nombre": nombre_producto, 
                        "Precio unitario" : precio_producto, 
                        "Unidades" : Unidades_producto, 
                        "Subtotal" : subtotal, 
                        "Total": total
                        }
            
            inventario.append(producto)
            print(f"\nProducto {nombre_producto} añadido con exito.")
            print("-"*n)

            elecion = input("¿Quiere seguir agregando productos?(Si/No): ").lower()

        except ValueError:
            print("ERROR! El precio y las unidades deben ser numeros.")
            continue
        
    return inventario, total, productos_registrados

def mostrar_inventario():
    print("="*n)
    print("INVENTARIO".center(n))
    print("="*n)

    if not inventario:
            print("La lista esta vacia, necesita agregar productos.")

    else:
        for productos in inventario:
            print("-"*n)
            print(f"Producto: {productos['Nombre']} | Precio Unitario: {productos['Precio unitario']} | Unidades: {productos['Unidades']}")

        print("-"*n)
        input('\nPresione ENTER para volver al menu principal...')

def calcular_estadisticas():
    print("="*n)
    print("ESTADISTICAS".center(n))
    print("="*n)
         
    if not inventario:
        print("La lista esta vacia, no se pueden ver las estadisticas.")

    else:
        print(f"Productos distintos registrados: {productos_registrados}")

        cantidad_total_productos = 0
        for productos in inventario:
            cantidad_total_productos += productos['Unidades']

        print("-"*n)
        print(f"Cantidad total de productos: {cantidad_total_productos}")
        print("-"*n)
        print("Productos:")

        for productos in inventario:
            print(f"-{productos['Nombre']}")
        print("-"*n)

        print(f"Valor total del inventario: {total}")

        print("="*n)
        input('\nPresione ENTER para volver al menu principal...')

opcion = menu_opciones()
while opcion != 4:
    if opcion == 1:
        inventario, total, productos_registrados = agregar_productos(inventario, total, productos_registrados)
    
    elif opcion == 2:
        mostrar_inventario()

    elif opcion == 3:
         calcular_estadisticas()
         
    else:
        print(f"\nERROR! La opcion {opcion} no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')
    
    opcion = menu_opciones()