# Problema 1
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}!")

# Problema 2
consumo = float(input("¿Cuál fue el total de tu consumo? $"))
porcentaje = float(input("¿Qué porcentaje de propina deseas dejar? "))
propina = consumo * (porcentaje / 100)
print(f"Debes dejar una propina de: S/ {propina:.2f}")

# Problema 3
peso_payaso = 112  # gramos
peso_muneca = 75   # gramos

num_payasos = int(input("¿Cuántos payasos se vendieron? "))
num_munecas = int(input("¿Cuántas muñecas se vendieron? "))

peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)
print(f"El peso total del paquete es {peso_total} gramos.")

# Problema 4
N = int(input("Introduce un número entero positivo: "))
suma = N * (N + 1) / 2
print(f"La suma de los primeros {N} números es: {suma}")

# Problema 5
shows = int(input("¿Cuántos shows musicales viste el último año? "))
visto_mas_de_3 = shows > 3
print(visto_mas_de_3)


# Problema 6
edad = int(input("¿Cuál es tu edad? "))

if edad < 4:
    print("Entrada gratis")
elif 4 <= edad <= 18:
    print("Debes pagar $5")
else:
    print("Debes pagar $10")
   

# Problema 7
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("¿Qué deseas hacer?")
print("1. Sumar")
print("2. Restar (primer número menos el segundo)")
print("3. Multiplicar")

opcion = input("Elige una opción (1, 2 o 3): ")

if opcion == "1":
    print(f"La suma es: {num1 + num2}")
elif opcion == "2":
    print(f"La resta es: {num1 - num2}")
elif opcion == "3":
    print(f"La multiplicación es: {num1 * num2}")
else:
    print("Opción inválida")

# Problema 8

tiempo = input("Qué hora es? ")
tiempo = tiempo.lower().strip()

hora, minuto = tiempo.split(':')

horario = float(hora) + int(minuto)/60

if 7 <= horario <= 8:
    print("Es hora de desayunar")
elif 12 <= horario <= 13:
    print("Es hora de almorzar")
elif 18 <= horario <= 19:
    print("Es hora de cenar")


# Problema 9

lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_original[::-1]
print(lista_invertida)

# Problema 10

lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Eliminamos del final al inicio para no cambiar los índices
del lista[5]
del lista[4]
del lista[0]
print(lista)

# Problema 11

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = list(set(lista_original))
lista_sin_duplicados.sort()
print(lista_sin_duplicados)

# Problema 12
archivo = input("Nombre del archivo: ").lower().strip()

# Diccionario de tipos MIME
tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Buscar la extensión
if "." in archivo:
    extension = "." + archivo.split(".")[-1]
    tipo = tipos_mime.get(extension, "application/octet-stream")
else:
    tipo = "application/octet-stream"

print(tipo)

