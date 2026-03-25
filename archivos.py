import csv
from servicios import buscar_producto

def guardar_csv(inventario):

    if not inventario:
        print("No hay productos para guardar.")
        return
    
    ruta = input("Nombre del archivo (EJ: inventario.csv): ")
    datos_viejos = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)

            for fila in reader:
                datos_viejos.append = ({
                    "Nombre": fila[0],
                    "Precio unitario": float(fila[1]),
                    "Cantidad": int(fila[2])
                    })

    except FileNotFoundError:
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
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Precio unitario", "Cantidad"])

            for producto in datos_finales:
                writer.writerow([producto["Nombre"], producto["Precio unitario"], producto["Cantidad"]])

            archivo.close()
            print("Archivo guardado correctamente.")

    except:
        print("Error al guardar el archivo.")

def cargar_csv(inventario):
    ruta = input("Nombre del archivo (EJ: inventario.csv): ")
    datos_nuevos = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            for fila in reader:
                try:
                    datos_nuevos.append({
                        "Nombre": fila[0],
                        "Precio unitario": float(fila[1]),
                        "Cantidad": int(fila[2])
                    })

                except ValueError:
                    errores += 1

    except FileNotFoundError:
        print("ERROR! El archivo no fue encontrado")
        return inventario
    
    if datos_nuevos:
        respuesta = input("Desea sobrescribir el inventario actual con los datos del archivo? (Si/No): ").lower()

        if respuesta == "si":
            print(f"Se leyeron {len(datos_nuevos)} productos y fueron sobrescritos con {errores} errores.")
            return datos_nuevos

        else:
            print("Archivos cargados exitosamente.")
            for nuevo in datos_nuevos:
                existente = buscar_producto(inventario, nuevo["Nombre"])

                if existente:
                        existente["Cantidad"] += nuevo["Cantidad"]
                        existente["Precio unitario"] = nuevo["Precio unitario"]
                else:
                    inventario.append(nuevo)
            
            return inventario

    return inventario
