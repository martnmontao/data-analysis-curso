# En data analysis, a veces necesitas generar identificadores únicos combinando distintos campos. Es un patrón muy común en pipelines de procesamiento.

# Consigna: Escribe un script que genere un ID de transacción estandarizado combinando los siguientes campos. El ID debe seguir el formato: YYYY-PAIS-TIPO-NUMERO donde el número siempre tiene 6 dígitos (rellena con ceros a la izquierda si hace falta).

anio = 2024
pais = "AR"
tipo_transaccion = "compra"
numero = 847

# Resultado esperado: "2024-AR-COMPRA-000847"
# Pista: investigá el método .zfill() o el formateo con f-strings {numero:06d}

transaction_id = f"{anio}-{pais}-{tipo_transaccion.upper()}-{str(numero).zfill(6)}"


print(transaction_id)