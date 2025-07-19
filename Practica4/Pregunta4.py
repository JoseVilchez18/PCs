# problema 4
import requests
from pymongo import MongoClient

def obtener_datos_sunat():
    datos = []
    for mes in range(1, 13):
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2023"
            response = requests.get(url)
            response.raise_for_status()
            resultados = response.json()
            if isinstance(resultados, list):
                datos.extend(resultados)
        except requests.RequestException as e:
            print(f"Error al consultar el mes {mes}: {e}")
    return datos

def guardar_en_mongo(datos):
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["base_tipos_cambio"]
        coleccion = db["sunat_info"]
        coleccion.delete_many({})  # limpiar datos anteriores
        if datos:
            coleccion.insert_many(datos)
            print(f"{len(datos)} registros insertados en MongoDB.")
    except Exception as e:
        print("Error al conectar con MongoDB:", e)

def mostrar_datos():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["base_tipos_cambio"]
    coleccion = db["sunat_info"]
    for doc in coleccion.find():
        print(doc)

# Ejecutar
datos = obtener_datos_sunat()
guardar_en_mongo(datos)
mostrar_datos()
