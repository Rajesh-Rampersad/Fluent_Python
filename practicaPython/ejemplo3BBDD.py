import sqlite3

miConexion=sqlite3.connect("GestionProducto")

miCursor=miConexion.cursor()


#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCIÓN='Deporte'")
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO = 'pelota'")
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

productos=miCursor.fetchall()

print(productos)


miConexion.commit()

miConexion.close()