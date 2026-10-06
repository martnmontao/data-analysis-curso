# En un reporte de ventas real necesitas agrupar los datos por algún criterio — categoría, región, vendedor — y calcular métricas por grupo. Antes de usar pandas, este ejercicio te muestra cómo funciona esa lógica por dentro.

# Consigna: Recorre la lista de productos y construí un diccionario que agrupe el total de ventas (precio × cantidad) por categoría. Al final imprimí un reporte con el total por categoría y cuál fue la categoría con mayor ingreso.

productos = [
    {"nombre": "Notebook",    "categoria": "tecnologia", "precio": 320000, "cantidad": 3},
    {"nombre": "Escritorio",  "categoria": "muebles",    "precio": 85000,  "cantidad": 5},
    {"nombre": "Mouse",       "categoria": "tecnologia", "precio": 8500,   "cantidad": 20},
    {"nombre": "Silla",       "categoria": "muebles",    "precio": 45000,  "cantidad": 8},
    {"nombre": "Monitor",     "categoria": "tecnologia", "precio": 210000, "cantidad": 4},
    {"nombre": "Lámpara",     "categoria": "muebles",    "precio": 12000,  "cantidad": 15},
    {"nombre": "Auriculares", "categoria": "tecnologia", "precio": 32000,  "cantidad": 11},
]

totales_por_categoria = {}

for p in productos:
    categoria = p['categoria']

    if categoria not in totales_por_categoria:
        totales_por_categoria[categoria] = p['precio'] * p['cantidad']
    else:
        totales_por_categoria[categoria] += p['precio'] * p['cantidad']

mayor_valor = 0
mayor_categoria = ""

for categoria, valor in totales_por_categoria.items():
    if valor > mayor_valor:
        mayor_valor = valor
        mayor_categoria = categoria

print(f"La categoria con mayor valor es: {mayor_categoria} con un valor total de ${mayor_valor}")

