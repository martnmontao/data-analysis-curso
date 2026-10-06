# En un sistema real de ventas, los reportes se generan automáticamente a partir de los datos crudos. Este ejercicio simula exactamente eso: a partir de una lista de transacciones, construís un reporte completo que podría enviarse por email o guardarse en un archivo.

# Consigna: A partir de la lista de transacciones, construye un reporte que incluya:

# Total de transacciones procesadas
# Monto total y promedio
# Desglose por país (cantidad y monto total)
# Las 3 transacciones de mayor monto
# Transacciones rechazadas (monto negativo o cero) con su motivo

transacciones = [
    {"id": "TX001", "pais": "MX", "monto": 45000,  "moneda": "MXN"},
    {"id": "TX002", "pais": "AR", "monto": 128000, "moneda": "ARS"},
    {"id": "TX003", "pais": "CO", "monto": 0,      "moneda": "COP"},
    {"id": "TX004", "pais": "MX", "monto": 87000,  "moneda": "MXN"},
    {"id": "TX005", "pais": "AR", "monto": -5000,  "moneda": "ARS"},
    {"id": "TX006", "pais": "PE", "monto": 32000,  "moneda": "PEN"},
    {"id": "TX007", "pais": "CO", "monto": 215000, "moneda": "COP"},
    {"id": "TX008", "pais": "MX", "monto": 61000,  "moneda": "MXN"},
    {"id": "TX009", "pais": "AR", "monto": 94000,  "moneda": "ARS"},
    {"id": "TX010", "pais": "PE", "monto": 17000,  "moneda": "PEN"},
]

total_transacciones = len(transacciones)

monto_total = sum(t['monto'] for t in transacciones)

promedio_monto = monto_total / len(transacciones)

desglose_por_pais = {}
transacciones_rechazadas = []


for t in transacciones:
    pais = t['pais']

    if pais not in desglose_por_pais:
        desglose_por_pais[pais] = {"cantidad_transacciones": 1, "monto_total": t["monto"]}
    else:
        desglose_por_pais[pais]["cantidad_transacciones"] += 1
        desglose_por_pais[pais]["monto_total"] += t["monto"]


    if t['monto'] <= 0:
        transacciones_rechazadas.append({
            **t,
            "motivo": "precio inválido"
        })


transacciones_ordenadas_por_mayor_monto = sorted(transacciones, key=lambda t: t['monto'], reverse=True)


primeras_tres_transacciones_mayor_monto = transacciones_ordenadas_por_mayor_monto[:3]


print("----- INFORME COMPLETO DE LAS TRANSACCIONES ------")

print(f"Total de transacciones procesadas {total_transacciones}\n"
      f"Monto total: {monto_total}\n"
      f"Valor promedio de las transacciones: {promedio_monto}\n")


for pais, valor in desglose_por_pais.items():
    print(f"Pais:{pais}.\nCantidad de transsaciones: {valor['cantidad_transacciones']}.\nMonto total: ${valor['monto_total']}\n")



print("Transacciones rechazadas:")
for t in transacciones_rechazadas:
    print(f"\nId: {t['id']}.\nPaís: {t['pais']}.\nMonto: ${t['monto']}\nMoneda: {t['moneda']}.\nMotivo: {t['motivo']}")