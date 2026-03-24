# 5. Cargar CSV (persistencia de entrada + validaciones):
# En archivos.py, implementa:
# cargar_csv(ruta) → retorna lista de productos con la misma estructura de inventario.
# Reglas de validación:
# El archivo debe tener encabezado válido: nombre,precio,cantidad.
# Cada fila debe tener exactamente 3 columnas.
# precio debe convertirse a float y cantidad a int, no negativos.
# Si hay filas inválidas, omítelas y acumula un contador de errores para informar al final (p. ej. “3 filas inválidas omitidas”).
# Manejar FileNotFoundError, UnicodeDecodeError, ValueError y errores genéricos con mensajes claros.
# Al cargar, preguntar al usuario:
# “¿Sobrescribir inventario actual? (S/N)”
# Si S: reemplaza inventario por lo cargado.
# Si N: fusiona por nombre:
# Si un nombre ya existe, actualiza precio/cantidad u omite (define una política y muéstrala al usuario; por defecto, actualiza cantidad sumando y si el precio difiere, actualiza al nuevo).
# Al finalizar, refresca la salida/menú y muestra un resumen: productos cargados, filas inválidas, acción (reemplazo/fusión).

# Modulo con todas las funciones

n = 60 # Ancho de lineas decorativas

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
            Cantidad_producto = int(input("Cantidad del producto: "))
            
            if precio_producto < 0 or Cantidad_producto < 0:
                print("ERROR! El precio y la cantidad no pueden ser negativos.")
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
def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["Nombre"].lower() == nombre.lower().strip():
            return producto # Retorna el producto encontrado (su diccioario)
    return None # El producto no se encontro en el iventario

def actualizar_producto(inventario, nombre):
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

    except:
        print("ERROR! El precio y la cantidad deben ser numeros.")
        # Si el usuario ingresa un valor no numérico para el precio o la cantidad, se muestra un mensaje de error y no se actualiza el producto
        # El programa sigue funcionando normalmente después de mostrar el mensaje de error  

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    
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
