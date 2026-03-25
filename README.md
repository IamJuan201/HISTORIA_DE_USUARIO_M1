# HISTORIA_DE_USUARIO_M1
## Descripcion

Este proyecto es un programa de gestion de inventario desarrollado en Python que permite registrar, administrar y persistir productos mediante un archivo CSV. 
El usuario puede registrar el nombre del producto, precio unitario y cantidad, tambien puede visualizar el inventario y consultar estadísticas generales como el valor total acumulado y la cantidad de unidades registradas.
El sistema implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar), además incluye validaciones de datos usando try y except para evitar errores cuando el usuario ingrese valores no numéricos.

## Funcionalidades
### CRUD de inventario
- Agregar productos.
- Mostrar inventario.
- Buscar productos por nombre.
- Actualizar productos.
- Eliminar productos.

### Estadisticas
- Total de productos registrados.
- Total de unidades.
- Valor total del inventario.
- Producto más caro.
- Producto con mayor cantidad.

### Persistencia de datos
- Guardar inventario en archivo .csv.
- Cargar inventario desde archivo .csv.
- Opcion de sobrescribir o fusionar datos.
- Validacion de datos al cargar.
- Conteo de filas con errores.

## Estructura del proyecto
PROYECTO PYTHON 
│── app.py          # Programa principal (menú y flujo) 
│── servicios.py    # Lógica del inventario (CRUD y estadísticas) 
│── archivos.py     # Manejo de archivos CSV 
│── README.md

## Tecnologias utilizadas
- Python 3

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado en tu equipo.
2. Clona el repositorio:
```
   git clone <url-del-repositorio>
```
3. Entra al proyecto
```
   cd HISTORIA_DE_USUARIO_M1
```
4. Ejecutar el programa
```
   python app.py
```

## Usos
- Registrar ventas ingresando nombre del producto, precio y cantidad.
- Calcular automáticamente el costo total de una compra.
- Validar que los datos ingresados sean numéricos, evitando errores en el registro.


## Previsualizacion del codigo:
### app.py

```python
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
        
    elif opcion == 8:
        ruta = input("Nombre del archivo: ")
        nuevos = cargar_csv(ruta)

        if nuevos:
            respuesta = input("Desea sobrescribir el inventario actual con los datos del archivo? (Si/No): ").lower()

            if respuesta == "si":
                inventario = nuevos

            else:
                for nuevo in nuevos:
                    existente = buscar_producto(inventario, nuevo["Nombre"])

                    if existente:
                        existente["Cantidad"] += nuevo["Cantidad"]
                        existente["Precio unitario"] = nuevo["Precio unitario"]
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

```

### servicios.py

```python
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

```

### archivos.py

```python
import csv

def guardar_csv(inventario, ruta):
    if not inventario:
        print("No hay productos para guardar.")
        return
    
    datos_viejos = []

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        reader = csv.reader(archivo)
        next(reader)  # saltar encabezado

        for fila in reader:
            producto = {
                "Nombre": fila[0],
                "Precio unitario": float(fila[1]),
                "Cantidad": int(fila[2])
            }

            datos_viejos.append(producto)
        
        archivo.close()

    except:
        datos_viejos = []
    
    if datos_viejos:
        respuesta = input("El archivo ya tiene datos. ¿Desea sobrescribirlo? (s/n): ").lower()
        if respuesta == "s":
            print("Archivo sobreescrito con éxito.")
            datos_finales = inventario
        else:
            print("Los datos nuevos se agregarán al archivo existente.")
            datos_finales = datos_viejos
        
            for nuevo in inventario:
                encontrado = False

                for viejo in datos_viejos:
                    if nuevo["Nombre"].lower() == nuevo["Nombre"].lower():
                        viejo["Cantidad"] += nuevo["Cantidad"]
                        viejo["Precio unitario"] = nuevo["Precio unitario"]
                        encontrado = True
                        break
                if not encontrado:
                    datos_finales.append(nuevo)
    else:
        datos_finales = inventario

    try:
        archivo = open(ruta, "w", newline="", encoding="utf-8")
        writer = csv.writer(archivo)

        writer.writerow(["Nombre", "Precio unitario", "Cantidad"])

        for producto in datos_finales:
            writer.writerow([producto["Nombre"], producto["Precio unitario"], producto["Cantidad"]])

        archivo.close()
        print("Archivo guardado correctamente.")

    except:
        print("Error al guardar el archivo.")


def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        reader = csv.reader(archivo)

        next(reader)

        for fila in reader:
            
            if len(fila) != 3:
                errores += 1
                continue
            
            try:
                producto = {
                    "Nombre": fila[0],
                    "Precio unitario": float(fila[1]),
                    "Cantidad": int(fila[2])
                }
                inventario.append(producto)

            except:
                errores += 1

        archivo.close()

        print("Archivo cargado correctamente.")
        print(f"Filas con error: {errores}")

        return inventario

    except:
        print("Error al cargar el archivo.")
        return []
```
## Representacion en consola:
```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir  

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 1  

===========================================================================  
Nombre del producto: Huevo  
Precio del producto: 500  
Cantidad del producto: 10  

Producto Huevo añadido con exito.  
---------------------------------------------------------------------------  
¿Quiere seguir agregando productos? (Si/No): si  

===========================================================================  
Nombre del producto: Café  
Precio del producto: 1200  
Cantidad del producto: 5  

Producto Café añadido con exito.  
---------------------------------------------------------------------------  
¿Quiere seguir agregando productos? (Si/No): no  

```

```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 2  

===========================================================================  
                               INVENTARIO  
===========================================================================  

---------------------------------------------------------------------------  
Producto: Huevo | Precio Unitario: 500.0 | Cantidad: 10  
---------------------------------------------------------------------------  
Producto: Café | Precio Unitario: 1200.0 | Cantidad: 5  
---------------------------------------------------------------------------  

```

```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 7  
Nombre del archivo: inventario.csv  

El archivo ya tiene datos. ¿Sobrescribir? (si/no): no  
Archivo guardado correctamente.  

```

```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 8  
Nombre del archivo: inventario.csv  

Archivo cargado correctamente.  
Filas con error: 0  

Desea sobrescribir el inventario actual con los datos del archivo? (Si/No): si  

```

```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 6  

===========================================================================  
                               ESTADISTICAS  
===========================================================================  

Productos registrados: 2  
Unidades totales: 15  
Valor total del inventario: 11000.0  
Producto más caro: Café (Precio unitario: 1200.0)  
Producto con mayor stock: Huevo (Cantidad: 10)  

```

```
===========================================================================  
                         REGISTRO DE INVENTARIO  
===========================================================================  

1. Agregar productos  
2. Mostrar inventario  
3. Buscar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Calcular estadísticas  
7. Guardar CSV  
8. Cargar CSV  
9. Salir

===========================================================================  
Ingrese la opcion que desea realizar (1-9): 9  

===========================================================================  
Gracias por usar el programa, hasta luego!  
===========================================================================  
```

## Autor
### Juan Rangel
