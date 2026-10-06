# Ejercicio 2 — Etiqueta de producto
# Un sistema de inventario necesita generar automáticamente una descripción de producto combinando distintos campos almacenados por separado.

# Consigna: Tienes las siguientes variables ya declaradas. Usa concatenación de strings para construir la etiqueta de producto y guardala en una nueva variable llamada etiqueta.

nombre_producto = "Notebook"
marca = "Lenovo"
precio = 320000
stock = 8

etiqueta = marca + " " + nombre_producto + " | " + "Precio: $" + str(precio) + " | " + "Stock: " + str(stock) + " unidades"

print(etiqueta)