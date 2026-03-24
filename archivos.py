import csv

def guardar_csv(inventario, ruta):
    try:
        lista_nueva = []
        archivo = open(ruta, "w", newline="", encoding="utf-8")

        writer = csv.writer(archivo)

        # Encabezados
        writer.writerow(["Nombre", "Precio unitario", "Cantidad"])

        # Datos
        for producto in inventario:
            writer.writerow([
                producto["Nombre"],
                producto["Precio unitario"],
                producto["Cantidad"]
            ])

        archivo.close()
        print("Archivo guardado con éxito.")
        
    except:
        print("Error al guardar el archivo.")
        

def cargar_csv(ruta):
    inventario = []

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
            inventario.append(producto)

        archivo.close()
        print("Archivo cargado con éxito.")
        return inventario

    except:
        print("Error al cargar el archivo.")
        return []