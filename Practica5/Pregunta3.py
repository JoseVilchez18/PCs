import requests
import zipfile
import os
import pandas as pd
from pymongo import MongoClient

# ------------------------------
# 1. DESCARGAR ARCHIVO ZIP
# ------------------------------
url = "https://netsg.cs.sfu.ca/youtubedata/0333.zip"
zip_path = "0333.zip"
carpeta_destino = "data_youtube"

print("Descargando archivo...")
response = requests.get(url)
with open(zip_path, "wb") as f:
    f.write(response.content)
print("Archivo descargado:", zip_path)

# ------------------------------
# 2. DESCOMPRIMIR EN CARPETA
# ------------------------------
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(carpeta_destino)
print("Archivos descomprimidos en:", carpeta_destino)

# ------------------------------
# 3. LEER UNO DE LOS ARCHIVOS
# ------------------------------
# Buscar un archivo en la carpeta
archivos = os.listdir(carpeta_destino)
if len(archivos) == 0:
    print("No se encontraron archivos en la carpeta.")
    exit()

archivo = os.path.join(carpeta_destino, archivos[0])
print("Leyendo archivo:", archivo)

# Leer datos con separador \t (sin nombres de columnas)
df = pd.read_csv(archivo, sep="\t", header=None)

# Asignar nombres de columnas
df.columns = ["VideoID", "edad", "categoria", "views", "rate", "ratings", "comentarios"]

# ------------------------------
# 4. FILTRAR DATOS
# ------------------------------
# Seleccionar solo ciertas columnas
df = df[["VideoID", "edad", "categoria", "views", "rate"]]

# Filtrar categorías (ejemplo: 1 = Film & Animation, 22 = People & Blogs, 10 = Music)
categorias_filtrar = [1, 22, 10]
df_filtrado = df[df["categoria"].isin(categorias_filtrar)]

print("Datos filtrados:")
print(df_filtrado.head())

# ------------------------------
# 5. EXPORTAR A MONGODB
# ------------------------------
try:
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["youtube_db"]
    coleccion = db["videos"]

    # Eliminar datos anteriores
    coleccion.delete_many({})

    # Insertar datos filtrados
    datos_dict = df_filtrado.to_dict("records")
    coleccion.insert_many(datos_dict)

    print(f"{len(datos_dict)} documentos insertados en MongoDB.")
    print("Conéctate a tu MongoDB local para verlos.")
except Exception as e:
    print("Error al conectar con MongoDB:", e)

