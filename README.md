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
   git clone https://github.com/IamJuan201/HISTORIA_DE_USUARIO_M1.git
```
3. Entra al proyecto
```
   cd HISTORIA_DE_USUARIO_M1
```
4. Ejecutar el programa
```
   python3 app.py
```

## Usos
- Registrar ventas ingresando nombre del producto, precio y cantidad.
- Calcular automáticamente el costo total de una compra.
- Validar que los datos ingresados sean numéricos, evitando errores en el registro.

## Autor
### Juan Rangel
