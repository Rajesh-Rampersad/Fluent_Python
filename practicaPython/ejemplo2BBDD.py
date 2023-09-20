import sqlite3

miConexion=sqlite3.connect("GestionProducto")

miCursor=miConexion.cursor()

# miCursor.execute('''
#                    CREATE TABLE IF NOT EXISTS Productos(ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#                    PRECIO INTEGER,
#                    SECCIÓN VARCHAR(20))
#                    ''')


# productos=[
    
#     ("pelota", 20, "Deporte"),
#     ("bate", 25, "Deporte"),
#     ("guantes", 30, "Deporte"),
#     ("casco", 20, "Deporte")
    
#             ]
    
# Productos1=[                                     #para insertar lotes registros al mismo tiempo se crea tuplas
#                  ("Cama", 100, "Casa"),
#                  ("Armario de ropa", 150, "Casa"),
#                  ("muebles de salas", 200, "casa")
#             ]

# productos.extend(Productos1)
                
#miCursor.executemany("INSERT INTO Productos VALUES(NULL,?,?,?)", productos)
miCursor.execute("SELECT * FROM Productos")
productos=miCursor.fetchall()

for producto in productos:
    print("Nombre Articulo ",producto[1], "precio: ", producto[2], " Seccion: ", producto[3])


miConexion.commit()

miConexion.close()