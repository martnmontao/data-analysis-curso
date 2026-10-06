# Una tienda necesita calcular automáticamente el precio final de todos sus productos aplicando el impuesto correspondiente.

# Consigna: Recorre la lista de precios con un bucle for y para cada precio calculá e imprimí el valor sin impuesto y con un impuesto del 19%. Al final, imprimí también el total acumulado de todos los precios con impuesto.

precios = [8500, 32000, 15900, 7200, 54000, 12300]
impuesto = 0.19




for p in precios:

    print(f"Precio base: ${p}. Precio con impuesto: ${p * (1 + impuesto)}.")


print(f"Al final: Total general: ${sum([p * (1 + impuesto) for p in precios])}")



