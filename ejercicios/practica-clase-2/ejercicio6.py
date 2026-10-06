# En la práctica, los datos que llegan de fuentes externas rara vez están limpios. Valores negativos, campos vacíos, tipos incorrectos — todo eso aparece antes de poder analizar nada. Saber detectarlo y manejarlo es una habilidad central en data analysis.

# Consigna: Recorre la lista de registros e identificá los que tienen problemas. Un registro es inválido si el precio es negativo, si el nombre está vacío, o si el stock no es un número entero. Separalos en dos listas: validos e invalidos, y para cada inválido indicá el motivo.

registros = [
    {"nombre": "Notebook",   "precio": 320000, "stock": 5},
    {"nombre": "",           "precio": 8500,   "stock": 10},
    {"nombre": "Monitor",    "precio": -210000,"stock": 2},
    {"nombre": "Teclado",    "precio": 45000,  "stock": 3.5},
    {"nombre": "Mouse",      "precio": 8500,   "stock": 0},
    {"nombre": "Auriculares","precio": 32000,  "stock": 7},
    {"nombre": "Cámara",     "precio": 0,      "stock": 4},
]

validos = []
invalidos = []


for r in registros:
    if r['precio'] <= 0 or r['stock'] != int(r['stock']) or r['nombre'] == "":
        invalidos.append(r)
    else:
        validos.append(r)


print("--- VALIDOS ---\n")

for i in validos:
    print(f"Nombre: {i['nombre']}. Precio: {i['precio']}. Stock: {i['stock']}")

print("--- INVALIDOS ---\n")
for i in invalidos:
    print(f"Nombre: {i['nombre']}. Precio: {i['precio']}. Stock: {i['stock']}")