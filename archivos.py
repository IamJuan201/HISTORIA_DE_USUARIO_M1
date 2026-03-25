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
    if '.' not in ruta:
        print("ERROR! El nombre del archivo debe incluir la extension .csv")
        input('\nPresione ENTER para volver al menu principal...')
    else:
        datos_viejos = []
        validar_ruta = ruta.split('.')

        if validar_ruta[1] != '.csv':
            print("ERROR! Solo se puede guardar archivos CSV")
        
        else:
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
                respuesta = input("El archivo ya tiene datos. ¿Desea sobrescribirlo? (Si/No): ").lower()
                if respuesta == "si":
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
    if '.' not in ruta:
        print("ERROR! El nombre del archivo debe incluir la extension .csv")
        input('\nPresione ENTER para volver al menu principal...')
    else:
        validar_ruta = ruta.split('.')
        datos_nuevos = []
        errores = 0

        if validar_ruta[1] != '.csv':
            print("ERROR! Solo se puede cargar archivos CSV")
        
        else:
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
