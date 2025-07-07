# -----------------------------
# PRACTICA 2 - Estructuras básicas
# -----------------------------

# Problema 1: Divisibles por 7 y múltiplos de 5 entre 1500 y 2700
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        print(numero)

# Problema 2: Patrón de asteriscos
for i in range(1, 6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)

# Problema 3: Contar pares e impares
numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta == "NO":
        break
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

pares = 0
impares = 0
for n in numeros:
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

# Problema 4: Registro de alumnos
alumnos = []
cantidad = int(input("¿Cuántos alumnos desea registrar? "))

for i in range(cantidad):
    nombre = input("Nombre del alumno: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    
    alumno = {
        "Alumno": nombre,
        "Notas": [nota1, nota2, nota3]
    }
    alumnos.append(alumno)

print("Listado de alumnos:")
for a in alumnos:
    print(a)

# Problema 5: Contar repeticiones de un dígito
def contar_digito(numero, digito):
    numero = str(numero)
    digito = str(digito)
    contador = 0
    for caracter in numero:
        if caracter == digito:
            contador = contador + 1
    print("Cantidad de veces", digito, "en el número:", contador)

n = input("Ingrese un número: ")
d = input("Ingrese el dígito a buscar: ")
contar_digito(n, d)

# Problema 6: Serie de Fibonacci hasta 50
a = 0
b = 1
while a <= 50:
    print(a)
    siguiente = a + b
    a = b
    b = siguiente

# Problema 7: Verificar número primo
def es_primo(numero):
    if numero < 2:
        print("No es primo")
        return
    divisor = 2
    primo = True
    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor = divisor + 1
    if primo:
        print("Es primo")
    else:
        print("No es primo")

n = int(input("Ingrese un número: "))
es_primo(n)

# Problema 8: Calcular factorial
def factorial(numero):
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado = resultado * contador
        contador = contador + 1
    print("El factorial es:", resultado)

n = int(input("Ingrese un número entero positivo: "))
factorial(n)

# Problema 9: Eliminar vocales de un texto
texto = input("Ingresa una cadena de texto: ")
resultado = ""
for letra in texto:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and \
       letra != "A" and letra != "E" and letra != "I" and letra != "O" and letra != "U":
        resultado = resultado + letra
print("Texto sin vocales:", resultado)

# Problema 10: Formatear fechas a AAAA-MM-DD
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

entrada = input("Ingresa una fecha (MM/DD/AAAA): ")

if "/" in entrada:
    partes = entrada.split("/")
    mes = int(partes[0])
    dia = int(partes[1])
    anio = int(partes[2])
else:
    partes = entrada.split(" ")
    nombre_mes = partes[0]
    dia = int(partes[1].replace(",", ""))
    anio = int(partes[2])
    mes = 0
    for i in range(len(meses)):
        if meses[i] == nombre_mes:
            mes = i + 1

if mes < 10:
    mes_str = "0" + str(mes)
else:
    mes_str = str(mes)

if dia < 10:
    dia_str = "0" + str(dia)
else:
    dia_str = str(dia)

print(str(anio) + "-" + mes_str + "-" + dia_str)
