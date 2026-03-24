# Importo las funciones que cree en mi archivo funciones_librerias.py
from servicios import menu_opciones, agregar_productos, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

# Variables globales, Se definen fuera de las funciones para que sean accesibles en todo el programa

inventario = [] # Lista vacia que se llenara con los productos registrados

n = 75 # Variable para definir el ancho de lineas y centrar textos

# muestra el menú, lee la opción y ejecuta la función correspondiente hasta que el usuario elija la opción 4.
opcion = menu_opciones()
while opcion != 9:
    if opcion == 1:
        agregar_productos(inventario)
    
    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre = input("Nombre del producto: ")
        producto = buscar_producto(inventario, nombre)
        print(producto if producto else "Producto no encontrado")
    
    elif opcion == 4:
        nombre = input("Nombre del producto: ")
        actualizar_producto(inventario, nombre)

    elif opcion == 5:
        nombre = input("Nombre del producto: ")
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 7:
        ruta = input("Nombre del archivo: ")
        guardar_csv(inventario, ruta)

        datos_viejos = cargar_csv

        if datos_viejos:
            input("El archivo ya existe. Desea sobrescribir los datos? (Si/No)").lower()

            if respuesta == 'si':
                guardar_csv(inventario, ruta)

            else:
                for item_memoria in inventario:
                    encontrado = False
                for item_archivo in datos_viejos:
                    if item_archivo["Nombre"] == item_memoria["Nombre"]:
                        item_archivo["Cantidad"] += item_memoria["Cantidad"]
                        item_archivo["Precio unitario"] = item_memoria["Precio unitario"]
                        encontrado = True
                        break
                if not encontrado:
                    datos_viejos.append(item_memoria)
            
            guardar_csv(datos_viejos, ruta)
            print("Datos mezclados y guardados correctamente.")
        else:
            guardar_csv(inventario, ruta)

        nuevos = cargar_csv(ruta)
        
    elif opcion == 8:
        ruta = input("Nombre del archivo: ")


        if nuevos:
            respuesta = input("Desea sobrescribir el inventario actual con los datos del archivo? (Si/No): ").lower()
            if respuesta == "si":
                inventario = nuevos
            else:
                for nuevo in nuevos:
                    existente = buscar_producto(inventario, nuevo["Nombre"])
                    if existente:
                        existente["Cantidad"] += nuevo["Cantidad"]
                        existente["Precio"] = nuevo["Precio"]
                    else:
                        inventario.append(nuevo)
    
    else:
        # Manejo de las opciones fuera del rango válido
        print("\nERROR! Esa opcion no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')
    
    opcion = menu_opciones()  # Vuelve a mostrar el menú al terminar cada acción

print("="*n)
print("\nGracias por usar el programa, hasta luego!".center(n))
print("="*n)