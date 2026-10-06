# En un sistema de inventario necesitas verificar si un producto existe antes de intentar consultarlo. Acceder a una clave que no existe genera un error que rompe el programa.

# Consigna: Dado el diccionario de productos y un código de búsqueda, verificá si el producto existe e imprimí su información. Si no existe, imprimí un mensaje indicándolo. Usá .get() para el acceso seguro.
inventario = {
    "NB-001": {"nombre": "Notebook Pro", "precio": 320000, "stock": 5},
    "MS-002": {"nombre": "Mouse Inalámbrico", "precio": 8500, "stock": 42},
    "MN-003": {"nombre": "Monitor 24\"", "precio": 210000, "stock": 0},
    "TC-004": {"nombre": "Teclado Mecánico", "precio": 45000, "stock": 12},
}


codigo_busqueda = "MN-03"


if codigo_busqueda in inventario:

    producto = inventario[codigo_busqueda]


    print(f"Código: {codigo_busqueda}. Nombre: {producto['nombre']}. Precio: ${producto['precio']}. Stock: {producto['stock']}")
else:
    print("El código de busqueda no está relacionado con ningún producto.")