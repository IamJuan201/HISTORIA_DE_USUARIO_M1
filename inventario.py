# Importo las funciones que cree en mi archivo funciones_librerias.py
import funciones_libreria

# Variables globales, Se definen fuera de las funciones para que sean accesibles en todo el programa

n = 60 # Variable para multiplicar equitativamente el numero de caracteres en los print,
        # para mejorar la estetica del programa

productos_registrados = 0 # Variable para contar la cantidad de productos distintos registrados

total = 0 # Variable para summar todos los subtotales y mostrar el valor total del inventario

inventario = [] # Lista vacia que se llenara con los productos registrados, 
                # cada producto se guardara como un diccionario con sus respectivas caracteristicas 
                # (nombre, precio unitario, unidades, subtotal y total)

# muestra el menú, lee la opción y ejecuta la función correspondiente hasta que el usuario elija la opción 4.
opcion = funciones_libreria.menu_opciones()
while opcion != 4:
    if opcion == 1:
        inventario, total, productos_registrados = funciones_libreria.agregar_productos(inventario, productos_registrados, total)
    
    elif opcion == 2:
        funciones_libreria.mostrar_inventario(inventario)

    elif opcion == 3:
        funciones_libreria.calcular_estadisticas(inventario, total, productos_registrados)

    else:
        # Manejo de las opciones fuera del rango válido
        print(f"\nERROR! La opcion {opcion} no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')
    
    opcion = funciones_libreria.menu_opciones()  # Vuelve a mostrar el menú al terminar cada acción