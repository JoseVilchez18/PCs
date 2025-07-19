# problema 3
def contar_lineas_codigo(ruta):
    try:
        if not ruta.endswith(".py"):
            print("Archivo inválido.")
            return

        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        contador = 0
        for linea in lineas:
            linea_strip = linea.strip()
            if linea_strip != "" and not linea_strip.startswith("#"):
                contador += 1

        print(f"Número de líneas de código: {contador}")

    except FileNotFoundError:
        print("Archivo no encontrado.")

ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
