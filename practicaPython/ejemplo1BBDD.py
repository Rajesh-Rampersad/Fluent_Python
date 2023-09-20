import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #sentecia para crear tablas

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON','15', 'DEPORTES')") #insertar datos en la tabla

variosProductos=[                #para insertar lotes registros al mismo tiempo se crea tuplas
                 ("Cama", 100, "Casa"),
                 ("Armario de ropa", 150, "Casa"),
                 ("muebles de salas", 200, "casa")
                    ]
#variosProductos.append(["Tenis", 40, "Calzado"]) # se usa la sentencia append para agregar mas elementos a la lista

#variosProductos.extend(["Tenis", 40, "Calzado"])# se usa la sentencia insert para agregar uno mas elementos en una posicion indicada por el usuario

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print("Nombre Articulo ",producto[0], "precio: ", producto[1], " Seccion: ", producto[2])


miConexion.commit()

miConexion.close()