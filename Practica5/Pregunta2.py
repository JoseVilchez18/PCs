import pandas as pd
import sqlite3
from pymongo import MongoClient

# -------------------------------
# 1. CARGAR DATOS
# -------------------------------
url_vinos = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202401/main/Modulo5/src/winemag-data-130k-v2.csv"
url_paises = "https://gist.githubusercontent.com/kintero/7d1db891401f56256c79/raw/a61f6d0dda82c3f04d2e6e76c3870552ef6cf0c6/paises.csv"

df = pd.read_csv(url_vinos)
paises = pd.read_csv(url_paises)

# -------------------------------
# 2. EXPLORAR DATAFRAME
# -------------------------------
print("Shape:", df.shape)
print("Columnas:", df.columns)
print(df.info())
print(df.describe())

# -------------------------------
# 3. RENOMBRAR 4 COLUMNAS
# -------------------------------
df = df.rename(columns={
    "country": "pais",
    "price": "precio",
    "points": "puntos",
    "variety": "variedad"
})

# -------------------------------
# 4. CREAR 3 NUEVAS COLUMNAS
# -------------------------------
# (a) Relación con países → continente
df = df.merge(paises, how="left", left_on="pais", right_on="Country")
df = df.rename(columns={"Continent": "continente"})

# (b) Clasificación de precio
df["categoria_precio"] = df["precio"].apply(
    lambda x: "Barato" if x < 20 else "Medio" if x < 50 else "Caro"
)

# (c) Clasificación de puntuación
df["categoria_puntos"] = df["puntos"].apply(
    lambda x: "Excelente" if x >= 90 else "Bueno" if x >= 80 else "Regular"
)

# -------------------------------
# 5. GENERAR 4 REPORTES
# -------------------------------

# REPORTE 1: Promedio de precio y puntos por país
reporte1 = df.groupby("pais").agg({"precio": "mean", "puntos": "mean"}).sort_values("puntos", ascending=False)

# REPORTE 2: Mejores vinos por continente
reporte2 = df.groupby("continente").apply(lambda x: x.nlargest(5, "puntos"))[["pais", "variedad", "puntos", "precio"]]

# REPORTE 3: Vinos baratos mejor puntuados
reporte3 = df[df["categoria_precio"] == "Barato"].sort_values("puntos", ascending=False).head(10)

# REPORTE 4: Conteo por categoría de puntos y continente
reporte4 = df.groupby(["continente", "categoria_puntos"]).size().reset_index(name="cantidad")

# -------------------------------
# 6. EXPORTAR REPORTES
# -------------------------------

# CSV
reporte1.to_csv("reporte1.csv", index=True)

# Excel
reporte2.to_excel("reporte2.xlsx", index=False)

# SQLite
conn = sqlite3.connect("vinos.db")
reporte3.to_sql("vinos_baratos", conn, if_exists="replace", index=False)
conn.close()

# MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["vinos_db"]
coleccion = db["reporte4"]
coleccion.delete_many({})
coleccion.insert_many(reporte4.to_dict("records"))
print("Datos insertados en MongoDB")

print("Exportación completa: CSV, Excel, SQLite, MongoDB")
