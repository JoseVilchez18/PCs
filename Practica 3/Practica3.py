# problema 1
def obtener_combustible():
    while True:
        try:
            fraccion = input("Ingrese fracción (X/Y): ")
            x_str, y_str = fraccion.split("/")
            x = int(x_str)
            y = int(y_str)

            if y == 0 or x > y:
                raise ValueError

            porcentaje = round((x / y) * 100)

            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            break
        except ValueError:
            print("Error: Ingrese solo números enteros, con X <= Y y Y distinto de 0.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

obtener_combustible()

# problema 2
def ingresar_calificaciones():
    entrada = input("Ingrese las calificaciones separadas por comas: ")
    elementos = entrada.split(",")
    calificaciones = []

    for e in elementos:
        try:
            calificaciones.append(int(e.strip()))
        except ValueError:
            print(f"Error al convertir '{e}'. Asegúrese de ingresar solo números.")

    print("Calificaciones válidas:", calificaciones)

ingresar_calificaciones()


# problema 3
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio

c1 = Circulo(5)
c2 = Circulo(10)

print("Área del primer círculo:", c1.calcular_area())
print("Área del segundo círculo:", c2.calcular_area())


# problema 4
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

r = Rectangulo(10, 5)
c = Cuadrado(7)

print("Área del rectángulo:", r.calcular_area())
print("Área del cuadrado:", c.calcular_area())

# problema 5
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}, Edad: {self.edad}, Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

a1 = Alumno("Juan Pérez", "202501")
a1.setAge(20)
a1.setNota([14, 16, 18])
a1.display()


# problema 6
import requests

def obtener_tipos_de_cambio():
    datos = []

    for mes in range(1, 13):
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos.extend(respuesta.json())
        except requests.RequestException as e:
            print(f"Error consultando el mes {mes}: {e}")

    return datos

def analizar(datos):
    min_compra = min(datos, key=lambda d: d["compra"])
    max_venta = max(datos, key=lambda d: d["venta"])
    max_dif = max(datos, key=lambda d: d["venta"] - d["compra"])

    print("Fecha con menor valor de compra:", min_compra["fecha"], "-", min_compra["compra"])
    print("Fecha con mayor valor de venta:", max_venta["fecha"], "-", max_venta["venta"])
    print("Fecha con mayor diferencia compra-venta:", max_dif["fecha"], "-", round(max_dif["venta"] - max_dif["compra"], 3))

tipos = obtener_tipos_de_cambio()
analizar(tipos)


# problema 7
import random
from pyfiglet import Figlet

def mostrar_figlet():
    figlet = Figlet()
    fuentes = figlet.getFonts()

    fuente_usuario = input("Ingrese una fuente (enter para aleatoria): ")

    if fuente_usuario.strip() == "":
        fuente = random.choice(fuentes)
    elif fuente_usuario in fuentes:
        fuente = fuente_usuario
    else:
        print("Fuente no válida. Se usará una aleatoria.")
        fuente = random.choice(fuentes)

    figlet.setFont(font=fuente)
    texto = input("Ingrese el texto a mostrar: ")
    print(figlet.renderText(texto))

mostrar_figlet()


# problema 8
import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)
        print("Imagen descargada como", nombre_archivo)
    except requests.RequestException:
        print("Error al descargar la imagen")

def comprimir(nombre_archivo, nombre_zip):
    with zipfile.ZipFile(nombre_zip, "w") as zipf:
        zipf.write(nombre_archivo)
    print("Imagen comprimida como", nombre_zip)

def descomprimir(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, "r") as zipf:
        zipf.extractall(carpeta_destino)
    print("Imagen descomprimida en", carpeta_destino)

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop"
imagen = "imagen.jpg"
archivo_zip = "imagen.zip"
carpeta = "extraido"

descargar_imagen(url, imagen)
comprimir(imagen, archivo_zip)
descomprimir(archivo_zip, carpeta)


