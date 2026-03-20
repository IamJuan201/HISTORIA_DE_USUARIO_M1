# HISTORIA_DE_USUARIO_M1
## Descripcion

Este proyecto es un programa en Python que permite gestionar un inventario de ventas desde la consola. El usuario puede registrar el nombre del producto, 
precio unitario y cantidad, tambien puede visualizar el inventario y consultar estadísticas generales como el valor total acumulado y la cantidad de unidades registradas.
 
Además incluye validaciones de datos usando try y except para evitar errores cuando el usuario ingrese valores no numéricos.

## Funcionalidades
- Mostrar un menú con 4 opciones.
- Solicitar el nombre el usuario.
- Solicitar el precio del producto.
- Solicitar la unidades del producto.
- Validar que el precio y las unidades sean valores numéricos.
- Registrar uno o varios productos consecutivamente.
- Validar que el precio y la cantidad del producto sean datos numericos.
- Calcular el subtotal por producto y el total acumulado del inventario.
- Mostrar el inventario con el nombre, precio unitario y unidades de cada producto.
- Mostrar los productos distintos registrados, cantidad total de unidades, lista de nombres y valor total del inventario.

## Tecnologias utilizadas
- Python 3

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado en tu equipo.
2. Clona el repositorio:
```
   git clone <url-del-repositorio>
```
3. Ejecuta el programa con el siguiente comando:
```
   inventario.py
```

## Usos
- Registrar ventas ingresando nombre del producto, precio y cantidad.
- Calcular automáticamente el costo total de una compra.
- Validar que los datos ingresados sean numéricos, evitando errores en el registro.


## CODIGO inventario: registar nombre, precio del producto, cantidad del producto y calcular total de la venta.

```python
# Variables globales, Se definen fuera de las funciones para que sean accesibles en todo el programa

n = 60 # Variable para multiplicar equitativamente el numero de caracteres en los print,
        # para mejorar la estetica del programa

inventario = [] # Lista vacia que se llenara con los productos registrados, 
                # cada producto se guardara como un diccionario con sus respectivas caracteristicas 
                # (nombre, precio unitario, unidades, subtotal y total)

productos_registrados = 0 # Variable para contar la cantidad de productos distintos registrados

total = 0 # Variable para summar todos los subtotales y mostrar el valor total del inventario

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

# muestra el menú, lee la opción y ejecuta la función correspondiente hasta que el usuario elija la opción 4.
opcion = menu_opciones()
while opcion != 4:
    if opcion == 1:
        inventario, total, productos_registrados = agregar_productos(inventario, total, productos_registrados)
    
    elif opcion == 2:
        mostrar_inventario()

    elif opcion == 3:
         calcular_estadisticas()
         
    else:
        # Manejo de las opciones fuera del rango válido
        print(f"\nERROR! La opcion {opcion} no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')
    
    opcion = menu_opciones()  # Vuelve a mostrar el menú al terminar cada acción

```

## Representacion en consola:
```
============================================================
                     REGISTRO DE VENTAS                     
============================================================
 
1. Agregar productos
2. Mostrar productos
3. Calcular estadisticas
4. Salir
 
============================================================
Ingrese la opcion que desea realizar (1-4): 1
============================================================
Nombre del producto: Lapiz
Precio del producto: 1500
Unidades del producto: 10
 
Producto Lapiz añadido con exito.
------------------------------------------------------------
¿Quiere seguir agregando productos?(Si/No): no
```
 
```
============================================================
                         ESTADISTICAS                       
============================================================
Productos distintos registrados: 1
------------------------------------------------------------
Cantidad total de productos: 10
------------------------------------------------------------
Productos:
-Lapiz
------------------------------------------------------------
Valor total del inventario: 15000.0
============================================================
```

## Autor
### Juan Rangel
