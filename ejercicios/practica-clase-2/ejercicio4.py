# Un analista necesita separar los registros de ventas en dos grupos: las que superan la meta mensual y las que no. Es el tipo de operación de filtrado más básica en data analysis.

# Consigna: Recorre la lista de ventas y separalas en dos listas nuevas: sobre_meta y bajo_meta. Al final imprimí cuántas hay en cada grupo y el total acumulado de cada uno. La meta es $50.000.

ventas = [23000, 87000, 45000, 102000, 31500, 68000, 49000, 95000, 12000, 74000]
meta = 50000

sobre_meta = []
bajo_meta = []

sobre_meta = [v for v in ventas if v > meta ]
bajo_meta = [v for v in ventas if v < meta ]


print(f"El total de los precios que superan la meta es de: ${sum(sobre_meta)}\nEl total de los precios que están por debajo de la meta es de: ${sum(bajo_meta)}")