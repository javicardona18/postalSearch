import sqlite3
import os
import json

# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "base_datos", "postalsearch.db")


def conectar():
    return sqlite3.connect(DB_PATH)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pasajeros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            ci TEXT NOT NULL,
            correo TEXT,
            telefono TEXT
        )
    """)

    conexion.commit()
    conexion.close()


def agregar_pasajero(nombre, apellido, ci, correo, telefono):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO pasajeros (nombre, apellido, ci, correo, telefono)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellido, ci, correo, telefono))

    conexion.commit()
    conexion.close()


def obtener_pasajeros():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, apellido, ci, correo, telefono FROM pasajeros")
    filas = cursor.fetchall()

    pasajeros = []

    for fila in filas:
        pasajeros.append({
            "nombre": fila[0],
            "apellido": fila[1],
            "ci": fila[2],
            "correo": fila[3],
            "telefono": fila[4]
        })

    return pasajeros


def eliminar_pasajero(ci):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM pasajeros WHERE ci = ?", (ci,))

    conexion.commit()
    conexion.close()

def insertar_datos_prueba():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM pasajeros")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        datos = [
            ("Juan", "Pérez", "12345678", "juan@email.com", "555-1234"),
            ("María", "Gómez", "87654321", "maria@email.com", "555-5678"),
            ("Carlos", "Rodríguez", "45678912", "carlos@email.com", "555-9012"),
            ("Ana", "Martínez", "74125896", "ana@email.com", "555-3456"),
        ]

        cursor.executemany("""
            INSERT INTO pasajeros (nombre, apellido, ci, correo, telefono)
            VALUES (?, ?, ?, ?, ?)
        """, datos)

        conexion.commit()

    conexion.close()

class ModeloPasajero:

    def __init__(self, ruta_json="data/pasajeros.json"):
        self.ruta_json = ruta_json

    def obtener_pasajeros(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos
    
    def insertar_pasajeros_api(self, pasajeros):

        conexion = sqlite3.connect("base_datos/postalSearch.db")
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM pasajeros")

        for p in pasajeros:
            cursor.execute("""
            INSERT INTO pasajeros (nombre, apellido, ci, correo, telefono)
            VALUES (?, ?, ?, ?, ?)
            """, (
                p["nombre"],
                p["apellido"],
                p["ci"],
                p["correo"],
                p["telefono"]
            ))

        conexion.commit()
        conexion.close()