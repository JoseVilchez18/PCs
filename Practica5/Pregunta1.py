import pandas as pd
#PREGUNTA 1
# Cargar dataset
df_airbnb = pd.read_csv("./Practica5/DATA/airbnb.csv")

# 1. Ver tamaño del dataset (filas, columnas)
print("Shape (filas, columnas):", df_airbnb.shape)

# 2. Ver nombres de columnas
print("\nColumnas:")
print(df_airbnb.columns)

# 3. Ver primeras 5 filas
print("\nPrimeras 5 filas:")
print(df_airbnb.head())

# 4. Tipos de datos y valores nulos
print("\nInformación general:")
print(df_airbnb.info())

# 5. Estadísticas descriptivas (para columnas numéricas)
print("\nEstadísticas descriptivas:")
print(df_airbnb.describe())

# 6. Número de valores únicos por columna
print("\nValores únicos por columna:")
print(df_airbnb.nunique())

# 7. Valores nulos por columna
print("\nValores nulos por columna:")
print(df_airbnb.isnull().sum())

# 8. Distribución por tipo de habitación
print("\nDistribución por room_type:")
print(df_airbnb['room_type'].value_counts())

# 9. Distribución por barrio
print("\nDistribución por neighborhood:")
print(df_airbnb['neighborhood'].value_counts())


#PREGUNTA 2
##Caso 1
import pandas as pd

# Cargar datos
df_airbnb = pd.read_csv("Practica5/DATA/airbnb.csv")

# Filtrar según condiciones
filtro = df_airbnb[
    (df_airbnb['accommodates'] >= 4) &
    (df_airbnb['bedrooms'] >= 2) &
    (df_airbnb['reviews'] > 10) &
    (df_airbnb['overall_satisfaction'] > 4)
]

# Ordenar por satisfacción y, en caso de empate, por número de críticas
resultado = filtro.sort_values(
    by=['overall_satisfaction', 'reviews'],
    ascending=[False, False]
)

# Mostrar las 3 mejores opciones
print("Las 3 mejores opciones para Alicia son:")
print(resultado.head(3))

#Caso2
import pandas as pd

# Cargar el dataset
df_airbnb = pd.read_csv("Practica5/DATA/airbnb.csv")

# IDs de las propiedades
id_roberto = 97503
id_clara = 90387

# Filtrar las propiedades
df_propiedades = df_airbnb[df_airbnb['room_id'].isin([id_roberto, id_clara])]

# Mostrar DataFrame filtrado
print("Propiedades de Roberto y Clara:")
print(df_propiedades)

# Comparar las críticas
criticas_roberto = df_propiedades[df_propiedades['room_id'] == id_roberto]['reviews'].values[0]
criticas_clara = df_propiedades[df_propiedades['room_id'] == id_clara]['reviews'].values[0]

if criticas_roberto > criticas_clara:
    print("✅ Roberto tiene más críticas que Clara.")
elif criticas_roberto < criticas_clara:
    print("❌ Clara tiene más críticas que Roberto.")
else:
    print("⚠ Ambos tienen la misma cantidad de críticas.")

# Guardar en Excel
df_propiedades.to_excel("roberto.xls", index=False)
print("Archivo 'roberto.xls' guardado correctamente.")

#Caso3
import pandas as pd

# Cargar dataset
df_airbnb = pd.read_csv("Practica5/DATA/airbnb.csv")

# Filtrar por presupuesto
filtro = df_airbnb[df_airbnb['price'] <= 50]

# Crear columna auxiliar para priorizar Shared room
filtro['prioridad'] = filtro['room_type'].apply(lambda x: 0 if x == "Shared room" else 1)

# Ordenar:
# 1) prioridad (Shared room primero)
# 2) precio (menor a mayor)
# 3) puntuación (mayor a menor)
resultado = filtro.sort_values(
    by=['prioridad', 'price', 'overall_satisfaction'],
    ascending=[True, True, False]
)

# Seleccionar las 10 primeras propiedades
diana_props = resultado.head(10)

# Mostrar resultado
print("Las 10 mejores opciones para Diana:")
print(diana_props[['room_id', 'room_type', 'price', 'overall_satisfaction', 'reviews', 'neighborhood']])


#Pregunta3
#Agrupamiento1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df_airbnb = pd.read_csv("Practica5/DATA/airbnb.csv")

# 1. Agrupamiento: Precio promedio por barrio
agrupamiento1 = df_airbnb.groupby('neighborhood')['price'].mean().sort_values(ascending=False)

print("Precio promedio por barrio:")
print(agrupamiento1)

# Gráfico de barras
plt.figure(figsize=(10,5))
sns.barplot(x=agrupamiento1.index, y=agrupamiento1.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Precio promedio por barrio")
plt.ylabel("Precio (€)")
plt.show()


#Agrupamiento2
# 2. Agrupamiento: Satisfacción promedio por tipo de habitación
agrupamiento2 = df_airbnb.groupby('room_type')['overall_satisfaction'].mean().sort_values(ascending=False)

print("\nSatisfacción promedio por tipo de habitación:")
print(agrupamiento2)

# Gráfico de barras
plt.figure(figsize=(6,4))
sns.barplot(x=agrupamiento2.index, y=agrupamiento2.values, palette="viridis")
plt.title("Satisfacción promedio por tipo de habitación")
plt.ylabel("Puntuación")
plt.show()
