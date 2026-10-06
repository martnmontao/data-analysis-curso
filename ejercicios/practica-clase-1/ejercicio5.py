# Estás depurando un script de análisis que falla intermitentemente porque recibe datos con tipos inconsistentes. Tu tarea es entender por qué falla y corregirlo.

# Consigna: El siguiente código tiene errores relacionados con tipos de datos. Ejecutalo, leé el error, y corrige sin borrar las variables originales, solo agrega las conversiones necesarias.

usuarios_activos = "1523"
ingresos_totales = 847320.50
tasa_conversion = "3.7"
nombre_campania = "BlackFriday2024"

# Estas operaciones fallan — ¿por qué? ¿cómo las corriges?
# ingreso_por_usuario = ingresos_totales / usuarios_activos
# tasa_decimal = tasa_conversion / 100
# resumen = "Campaña " + nombre_campania + " | Conversión: " + tasa_conversion + "% | Ingreso/usuario: $" + ingreso_por_usuario
# print(resumen)

# CORRECION
ingreso_por_usuario = ingresos_totales / int(usuarios_activos)
tasa_decimal = float(tasa_conversion) / 100
resumen = "Campaña " + nombre_campania + " | Conversión: " + tasa_conversion + "% | Ingreso/usuario: $" + str(ingreso_por_usuario)
print(resumen)