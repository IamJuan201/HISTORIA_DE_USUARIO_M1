# Importo las funciones que cree en mi archivo funciones_librerias.py
from servicios import menu_opciones, agregar_productos, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

# Variables globales, Se definen fuera de las funciones para que sean accesibles en todo el programa

inventario = [] # Lista vacia que se llenara con los productos registrados

n = 75 # Variable para definir el ancho de lineas y centrar textos

# muestra el menú, lee la opción y ejecuta la función correspondiente hasta que el usuario elija la opción 9.
opcion = menu_opciones()
while opcion != 9:
    if opcion == 1:
        agregar_productos(inventario)
    
    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto: ")
        producto = buscar_producto(inventario, nombre)
        if producto:
            print("-"*n)
            print(f"Producto: {producto['Nombre']} | Precio: {producto['Precio unitario']} | Cantidad: {producto['Cantidad']}")
            print("-"*n)
        else:
            print("Producto no encontrado.")
        input('\nPresione ENTER para continuar...')
    
    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        actualizar_producto(inventario, nombre)

    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 7:
        guardar_csv(inventario)
        
    elif opcion == 8:
        inventario = cargar_csv(inventario)

    else:
        # Manejo de las opciones fuera del rango válido
        print("\nERROR! Esa opcion no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')
    
    opcion = menu_opciones()  # Vuelve a mostrar el menú al terminar cada acción

print("="*n)
print("\nGracias por usar el programa, hasta luego!".center(n))
print("="*n)