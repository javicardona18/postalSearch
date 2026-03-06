import sqlite3

conexion = sqlite3.connect("base_datos/postalSearch.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM pasajeros")
datos = cursor.fetchall()

for fila in datos:
    print(fila)

conexion.close()