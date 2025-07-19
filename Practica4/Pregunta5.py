# problema 5
import csv
from pymongo import MongoClient

def obtener_tipo_cambio(fecha, coleccion_sunat):
    registro = coleccion_sunat.find_one({"fecha": fecha})
    if registro:
        return registro.get("venta", 0)
    return 0

def procesar_ventas():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["base_tipos_cambio"]
    coleccion_sunat = db["sunat_info"]
    coleccion_ventas = db["ventas_solarizadas"]

    ventas_por_producto = {}

    try:
        with open("ventas.csv", "r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                fecha = fila["fecha"]
                producto = fila["producto"]
                precio_dolares = float(fila["precio"])

                tipo_cambio = obtener_tipo_cambio(fecha, coleccion_sunat)
                precio_soles = precio_dolares * tipo_cambio

                if producto not in ventas_por_producto:
                    ventas_por_producto[producto] = 0
                ventas_por_producto[producto] += precio_soles

        # Guardar resultados en MongoDB
        coleccion_ventas.delete_many({})
        documentos = [{"producto": prod, "total_soles": round(total, 2)} for prod, total in ventas_por_producto.items()]
        coleccion_ventas.insert_many(documentos)

        print("Resultados guardados en MongoDB:")
        for doc in coleccion_ventas.find():
            print(doc)

    except FileNotFoundError:
        print("El archivo ventas.csv no se encontró.")

procesar_ventas()
