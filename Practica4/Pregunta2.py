# problema 2
def guardar_tabla(n):
    try:
        if 1 <= n <= 10:
            with open(f"tabla-{n}.txt", "w") as f:
                for i in range(1, 11):
                    f.write(f"{n} x {i} = {n*i}\n")
            print(f"Tabla de {n} guardada en tabla-{n}.txt")
        else:
            print("Número fuera de rango.")
    except Exception as e:
        print("Error:", e)

def leer_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"No existe el archivo tabla-{n}.txt")

def leer_linea(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m-1])
            else:
                print("Número de línea fuera de rango.")
    except FileNotFoundError:
        print(f"No existe el archivo tabla-{n}.txt")

# Menú básico
while True:
    print("\nMenú:")
    print("1. Guardar tabla")
    print("2. Leer tabla")
    print("3. Leer línea de tabla")
    print("4. Salir")

    opcion = input("Seleccione opción: ")
    if opcion == "1":
        n = int(input("Ingrese número (1-10): "))
        guardar_tabla(n)
    elif opcion == "2":
        n = int(input("Ingrese número (1-10): "))
        leer_tabla(n)
    elif opcion == "3":
        n = int(input("Ingrese número (1-10): "))
        m = int(input("Ingrese número de línea (1-10): "))
        leer_linea(n, m)
    elif opcion == "4":
        break
