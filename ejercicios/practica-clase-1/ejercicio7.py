# En proyectos reales de data analisis, los datasets suelen tener columnas con tipos mezclados o inesperados. Saber detectar y manejar esto a mano, te da una comprensión mucho más sólida de lo que las herramientas hacen por ti.

# Consigna: Tienes estos valores tal como podrían llegar de un CSV real. Para cada uno:

# Determina qué tipo tiene actualmente con type()
# Determina qué tipo debería tener para análisis
# Conviertelo (si es posible) y maneja los casos problemáticos.


valor_a = "42"
valor_b = "3.14"
valor_c = "True"
valor_d = ""
valor_e = "N/A"
valor_f = "  150  "
valor_g = "$1,250.50"
valor_h = "01/03/2024"

valor_a = int(valor_a)
valor_b = float(valor_b)
valor_c = bool(valor_c)
valor_d = ""
valor_e = "N/A"
valor_f = int(valor_f.strip())
valor_g = float(valor_g.replace("$", "").replace(",", ""))
valor_h = "01/03/2024"


print(f"a={valor_a} ({type(valor_a)})")