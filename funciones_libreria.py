# Variables globales, Se definen fuera de las funciones para que sean accesibles en todo el programa

n = 60 # Variable para multiplicar equitativamente el numero de caracteres en los print,
        # para mejorar la estetica del programa

productos_registrados = 0 # Variable para contar la cantidad de productos distintos registrados

total = 0 # Variable para summar todos los subtotales y mostrar el valor total del inventario

inventario = [] # Lista vacia que se llenara con los productos registrados, 
                # cada producto se guardara como un diccionario con sus respectivas caracteristicas 
                # (nombre, precio unitario, unidades, subtotal y total)

# Menu de opciones para el usuario, muestra las opciones disponibles al usuario y segun la opcion elegida,
# se llama a la funcion correspondiente para realizar la accion deseada
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

    return opcion # Retorna la opción elegida para procesarla en el bucle principal

# Funcion que permite registrar uno o varios productos en el inventario
def agregar_productos(inventario, total, productos_registrados):

    # Para que el usuario pueda seguir agregando productos mientras escriba que si en la elecion
    elecion = 'si'
    while elecion == 'si':
        print("="*n)
        nombre_producto = input("Nombre del producto: ")

        # Se usa try para que el precio sea un número decimal y las unidades un número entero, 
        # Si el usuario ingresa texto u otro valor inválido se le muestra un error y se reinicia 
        # con continue sin agregar datos incorrectos al inventario
        try:
            precio_producto = float(input("Precio del producto: "))
            Unidades_producto = int(input("Unidades del producto: "))
            
            subtotal = precio_producto * Unidades_producto
            total += subtotal
            productos_registrados += 1

            # Cada producto se representa como un diccionario con sus características
            producto = {"Nombre": nombre_producto, 
                        "Precio unitario" : precio_producto, 
                        "Unidades" : Unidades_producto, 
                        "Subtotal" : subtotal, 
                        "Total": total
                        }
            
            inventario.append(producto) # Se añade el producto a la lista de inventario

            print(f"\nProducto {nombre_producto} añadido con exito.")
            print("-"*n)

            elecion = input("¿Quiere seguir agregando productos?(Si/No): ").lower()

        except ValueError:
            print("ERROR! El precio y las unidades deben ser numeros.")
            continue
            # Si el precio o las unidades no son numéricos se muestra un mensaje de error y se reinicia
            # el bucle para que el usuario pueda ingresar los datos nuevamente
    
    # Se retornan los tres valores modificados para actualizar
    # las variables globales desde el bucle principal
    return inventario, total, productos_registrados

# Recorre la lista global de productos y muestra los datos de cada producto registrado, 
# si la lista esta vacia se muestra un mensaje que no hay productos registrados
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

# Muestra el número de productos distintos, cantidad total de unidades, lista de nombres y valor total acumulado.
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