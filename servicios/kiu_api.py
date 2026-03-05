import requests


def obtener_pasajeros_api():

    url = "https://api.kiusystem.com/pasajeros"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return []