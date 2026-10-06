# Tu jefa te pide que armes un mini-reporte de ventas del día para enviarlo por mensaje. Tiene que ser legible y estar en una sola variable.

# Consigna: Usa las variables dadas para construir un reporte en varias líneas usando \n dentro de un string, o un f-string multilínea con """. El reporte debe incluir todos los campos y calcular el promedio de ventas.


fecha = "2024-11-14"
vendedor = "Carlos Méndez"
ventas = [45000, 32000, 67500, 28000, 91000]
producto_estrella = "Auriculares Bluetooth"
total_ventas = sum(ventas)
promedio_ventas = total_ventas / len(ventas)

reporte = (f"Reporte de ventas - {fecha}\n" 
        f"Vendedor: {vendedor}\n"
        f"Total de ventas: ${total_ventas}\n"
        f"Promedio de ventas: ${promedio_ventas}\n"
        f"Producto estrella: f{producto_estrella}")

print(reporte)