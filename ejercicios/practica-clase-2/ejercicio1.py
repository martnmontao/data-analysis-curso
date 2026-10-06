# Ejercicio 1 — Clasificar una transacción
# En cualquier sistema de pagos existe una lógica de clasificación automática. Dependiendo del monto, una transacción recibe una categoría distinta que determina cómo se procesa.

# Consigna: Dado el monto de una transacción, escribí un programa que lo clasifique según estas reglas y lo imprima con un mensaje descriptivo:

# Menos de $1.000: "micro transacción"
# Entre 
# 9.999: "transacción estándar"
# Entre 
# 99.999: "transacción importante"
# $100.000 o más: "transacción de alto valor"

monto = 45750


if monto < 1000:
    mensaje = "micro transacción"
elif monto > 1000 and monto < 9999:
    mensaje = "transacción estándar"
elif monto > 10000 and monto < 99999:
    mensaje = "transacción importante"
else:
    mensaje = "transacción de alto valor"


print(mensaje)