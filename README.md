# HISTORIA_DE_USUARIO_M1
## Repositorio en github:
### https://github.com/IamJuan201/HISTORIA_DE_USUARIO_M1.git

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

# muestra el menú, lee la opción y ejecuta la función correspondiente hasta que el usuario elija la opción 9.
opcion = menu_opciones()
while opcion != 9:
    if opcion == 1:
        agregar_productos(inventario)
    
    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        buscar_producto(inventario)
    
    elif opcion == 4:
        actualizar_producto(inventario)

    elif opcion == 5:
        eliminar_producto(inventario)

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


```

### archivos.py

```python
import csv
from servicios import buscar_producto

# Funcion para guardar el inventario en un archivo csv
def guardar_csv(inventario):
    # Si no hay nada en el inventario entonces se muestra un mensaje al usuario indicandole que no hay productos
    if not inventario:
        print("No hay productos para guardar.")
        return
    
    # En el caso que si hay datos en el inventario entonces se le pregunta al usuario por el nombre del archivo donde se guardará
    ruta = input("Nombre del archivo (EJ: inventario.csv): ")
    datos_viejos = []

    # Para leer el archivo en modo lectura y recuperar datos previos
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader) # Omite la linea de encabezados

            # Recorre cada fila del CSV y la convierte a un diccionario
            for fila in reader:
                datos_viejos.append = ({
                    "Nombre": fila[0],
                    "Precio unitario": float(fila[1]),
                    "Cantidad": int(fila[2])
                    })

    except FileNotFoundError:
        # Si el archivo no se encuentra entonces el usuario decide si lo quiere crear o no
        confirmar = input(f"El archivo {ruta} no existe. ¿Desea crearlo y guardar los datos? (Si/No): ").lower()

        # Si dice que si se prepara una lista vacia para continuar con el guardado
        if confirmar == 'si':
            datos_viejos = []

        else:
            # Si dice que no o escribe otra cosa entonces no se crea el archivo  
            return

    # Cuando el archivo ya tiene datos se le pregunta al usuario si desea sobrescribirlo
    if datos_viejos:
        respuesta = input("El archivo ya tiene datos. ¿Desea sobrescribirlo? (s/n): ").lower()
        if respuesta == "s":
            print("Archivo sobreescrito con éxito.")
            datos_finales = inventario
            # Si responde que simplemente se remplazan los datos que ya estaban en el CSV por los creados

        else:
            print("Los datos nuevos se agregarán al archivo existente.")
            datos_finales = datos_viejos

            for nuevo in inventario:
                encontrado = False

                for viejo in datos_viejos:
                    # Compara si el nombre del producto nuevo ya existe en los datos viejos
                    if nuevo["Nombre"].lower() == nuevo["Nombre"].lower():
                        viejo["Cantidad"] += nuevo["Cantidad"]
                        viejo["Precio unitario"] = nuevo["Precio unitario"]
                        encontrado = True
                        break

                # Si el producto no existia en el archivo entonces se agrega como uno nuevo
                if not encontrado:
                    datos_finales.append(nuevo)

    # Si el archivo no existia o estaba vacio los datos finales seran directamente el inventario actual
    else:
        datos_finales = inventario

    # Para escribir los datos definitivos en el archivo (crea el archivo si no existia)
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Precio unitario", "Cantidad"])

            # Recorre la lista final y escribe cada producto en el archivo csv
            for producto in datos_finales:
                writer.writerow([producto["Nombre"], producto["Precio unitario"], producto["Cantidad"]])

            archivo.close()
            print("Archivo guardado correctamente.")

    except:
        print("Error al guardar el archivo.")

def cargar_csv(inventario):
    # Aqui se le pregunta al usuario por el nombre del archivo CSV donde se guardaran los datos
    ruta = input("Nombre del archivo (EJ: inventario.csv): ")
    datos_nuevos = []
    errores = 0

    try:
        # Intenta abrir el archivo en modo lectura para extraer los datos
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader) # Omite la linea de encabezado

            # Recorre cada fila y la convierte a un diccionario para el inventario
            for fila in reader:
                try:
                    datos_nuevos.append({
                        "Nombre": fila[0],
                        "Precio unitario": float(fila[1]),
                        "Cantidad": int(fila[2])
                    })

                # En caso de que los datos esten mal escritos en el archivo se cuenta como un error (Menos o mas datos de los que deberian)
                except ValueError:
                    errores += 1


    # En caso que no se encuentre el archivo se muestra un mensaje de error y se devuelve el inventario
    except FileNotFoundError:
        print("ERROR! El archivo no fue encontrado")
        return inventario

    # Si se cargaron datos nuevos se le pregunta al usuario como integrarlos al inventario
    if datos_nuevos:
        respuesta = input("Desea sobrescribir el inventario actual con los datos del archivo? (Si/No): ").lower()

        # Si el usuario dice que si entonces el inventario actual se reemplaza por el del archivo
        if respuesta == "si":
            print(f"Se leyeron {len(datos_nuevos)} productos y fueron sobrescritos con {errores} errores.")
            return datos_nuevos
        
        # Si el usuario dice que no entonces se mezclan los productos del archivo con los que ya estan
        else:
            print("Archivos cargados exitosamente.")
            for nuevo in datos_nuevos:
                # Busca si el producto del archivo ya existe en el inventario actual
                existente = buscar_producto(inventario, nuevo["Nombre"])

                # Si ya existe se actualiza la cantidad y precio
                if existente:
                        existente["Cantidad"] += nuevo["Cantidad"]
                        existente["Precio unitario"] = nuevo["Precio unitario"]
                else:
                    inventario.append(nuevo)
                    # Se añade los datos que estan en el archivo a la lista del inventario
            
            return inventario

    return inventario

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
