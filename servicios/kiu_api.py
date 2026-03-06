import os
import json


def obtener_pasajeros_api():

    # Carpeta donde está este archivo (servicios)
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Subimos a la raíz del proyecto
    ruta_proyecto = os.path.dirname(ruta_actual)

    # Ruta al JSON dentro de /data
    ruta_json = os.path.join(ruta_proyecto, "data", "pasajeros.json")

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        pasajeros = json.load(archivo)

    return pasajeros