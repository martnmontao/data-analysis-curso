# Muchos sistemas de scraping o formularios web devuelven todos los datos como strings, incluso los números. Antes de poder operar con esos datos, tiens que convertirlos al tipo correcto.

# Consigna: El sistema te entregó estos datos de un producto como strings. Conviertelos al tipo adecuado para poder calcular el precio con descuento y el IVA.

precio_str = "15990"
descuento_str = "0.15"
cantidad_str = "4"
tiene_iva_str = "True"

print("------ INFORMACIÓN COMPLETA ------")

precio_int = int(precio_str)
descuento_float = float(descuento_str)
cantidad_int = int(cantidad_str)
tiene_iva_bool = bool(tiene_iva_str)


precio_final = precio_int * (1 - descuento_float)

if tiene_iva_bool:
    precio_final *= 1.21


print(f"Precio final: ${precio_final}")
