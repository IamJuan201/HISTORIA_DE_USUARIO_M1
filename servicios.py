# Modulo con todas las funciones

n = 75 # Ancho de lineas decorativas

# Menu de opciones para el usuario segun la opcion elegida se llama a la funcion correspondiente para realizar la accion deseada
def menu_opciones():
    print("="*n)
    print("REGISTRO DE INVENTARIO".center(n))
    print("="*n)
    print('\n1. Agregar productos')
    print('2. Mostrar inventario')
    print('3. Buscar producto')
    print('4. Actualizar producto')
    print('5. Eliminar producto')
    print('6. Calcular estadisticas')
    print('7. Guardar CSV')
    print('8. Cargar CSV')
    print('9. Salir\n\n')
    print("="*n)

    try:
        opcion = int(input("Ingrese la opcion que desea realizar (1-9): "))
        return opcion # Retorna la opción elegida para procesarla en el bucle principal
    except:
        return 0 # Retorna 0 para indicar que la opción no es válida y mostrar un mensaje de error en el bucle principal

# Funcion que permite registrar uno o varios productos en el inventario
def agregar_productos(inventario):

    # Para que el usuario pueda seguir agregando productos mientras escriba que si en la elecion
    elecion = 'si'

    while elecion == 'si':
        print("="*n)
        nombre_producto = input("Nombre del producto: ")

        # Se usa try para que el precio sea un número decimal y las cantidades un número entero.
        try:
            precio_producto = float(input("Precio del producto: "))
            if precio_producto < 0:
                print("ERROR! El precio no puede ser negativo. Intente de nuevo...")
                continue

            Cantidad_producto = int(input("Cantidad del producto: "))
            if Cantidad_producto < 0:
                print("ERROR! La cantidad no puede ser negativa. Intente de nuevo...")
                continue
                # Si el precio o las unidades son negativos se muestra un mensaje de error y se reinicia
                # el bucle para que el usuario pueda ingresar los datos nuevamente

            # Cada producto se representa como un diccionario con sus características
            producto = {"Nombre": nombre_producto, 
                        "Precio unitario" : precio_producto, 
                        "Cantidad" : Cantidad_producto, 
                        }
            
            inventario.append(producto) # Se añade el producto a la lista de inventario

            print(f"\nProducto {nombre_producto} añadido con exito.")
            print("-"*n)

            elecion = input("¿Quiere seguir agregando productos?(Si/No): ").lower()
            # Dependiendo la eleccion se reinicia el bucle
        
        # Error cuando los valores que ingresan no son numeros
        except ValueError:
            print("ERROR! El precio y la Cantidad deben ser numeros.")

# Recorre la lista global de productos y muestra los datos de cada producto registrado, 
# si la lista esta vacia se muestra un mensaje que no hay productos registrados
def mostrar_inventario(inventario):
    print("="*n)
    print("INVENTARIO".center(n))
    print("="*n)

    if not inventario:
        print("La lista esta vacia, necesita agregar productos.")

    else:
        for productos in inventario:
            print("-"*n)
            print(f"Producto: {productos['Nombre']} | Precio Unitario: {productos['Precio unitario']} | Cantidad: {productos['Cantidad']}")

        print("-"*n)
    input('\nPresione ENTER para volver al menu principal...')

# Busca un producto por su nombre en el inventario, si lo encuentra retorna el diccionario del producto,
# si no lo encuentra retorna None
def buscar_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario, agruegue productos para buscar.")
        input("\nPresione ENTER para continuar...")

    else:
        nombre = input("Nombre del producto: ")
    
        for producto in inventario:
            # Garantizar que ambos nombres sean iguales al momento de la busqueda gracias al .lower() y el .strip()
            if producto["Nombre"].lower() == nombre.lower().strip():
                print(f"\nEl producto {producto} ha sido encontrado.")
                return producto
            
        print(f"\nEl producto {nombre} no fue encontrado.")
        return None

def actualizar_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario, agruegue productos para actualizar.")
        input("\nPresione ENTER para continuar...")
    else:
        nombre = input("Nombre del producto: ")
        # Realiza lo mismo que esta en la funcion buscar_producto solo que aqui se almacena en la variable producto
        producto = buscar_producto(inventario, nombre)

        if not producto:
            print(f"El producto '{nombre}' no se encontró en el inventario.")
            return
        
        try:
            nuevo_precio = input("Nuevo precio (ENTER para omitir): ")
            nueva_cantidad = input("Nueva cantidad (ENTER para omitir): ")

            if nuevo_precio:
                producto["Precio unitario"] = float(nuevo_precio) # Actualiza el precio del producto con el nuevo valor ingresado por el usuario
            if nueva_cantidad:
                producto["Cantidad"] = int(nueva_cantidad) # Actualiza la cantidad del producto con el nuevo valor ingresado por el usuario
            
            print("Producto actualizado con éxito.")

        except ValueError:
            print("ERROR! El precio y la cantidad deben ser numeros.")
            # Si el usuario ingresa un valor no numérico para el precio o la cantidad, se muestra un mensaje de error y no se actualiza el producto
            # El programa sigue funcionando normalmente después de mostrar el mensaje de error  

def eliminar_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario, agruegue productos para eliminar.")
        input("\nPresione ENTER para continuar...")
    else:
        nombre = input("Nombre del producto: ")
        producto = buscar_producto(inventario, nombre)
        # Realiza lo mismo que esta en la funcion buscar_producto solo que aqui se almacena en la variable producto
        
        if not producto:
            print(f"El producto '{nombre}' no se encontró en el inventario.")
            return
        
        inventario.remove(producto)
        print(f"Producto '{nombre}' eliminado con éxito.")
        print("-"*n)

# Muestra el número de productos distintos, cantidad total de unidades, lista de nombres y valor total acumulado.
def calcular_estadisticas(inventario):
    print("="*n)
    print("ESTADISTICAS".center(n))
    print("="*n)

    if not inventario:
        print("La lista esta vacia, no se pueden ver las estadisticas.")
        return None

    unidades_totales = 0
    valor_total = 0
    
    for producto in inventario:
        unidades_totales += producto["Cantidad"] # Suma la cantidad de cada producto para obtener el total de unidades
        valor_total += (producto["Cantidad"] * producto["Precio unitario"]) # Suma el subtotal de cada producto para obtener el valor total del inventario
    
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
    
    for producto in inventario:
        if producto["Precio unitario"] > producto_mas_caro["Precio unitario"]:
            producto_mas_caro = producto # Compara el precio unitario de cada producto para encontrar el producto más caro
        if producto["Cantidad"] > producto_mayor_stock["Cantidad"]:
            producto_mayor_stock = producto # Compara la cantidad de cada producto para encontrar el producto con mayor stock
    
    print(f"Productos registrados: {len(inventario)}")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['Nombre']} (Precio unitario: {producto_mas_caro['Precio unitario']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['Nombre']} (Cantidad: {producto_mayor_stock['Cantidad']})")
        
    input('\nPresione ENTER para volver al menu principal...')
        
    return {
                "Unidades_totales" : unidades_totales,
                "Valor_total" : valor_total,
        }
