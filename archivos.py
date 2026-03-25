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