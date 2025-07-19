# problema 1
def procesar_temperaturas():
    try:
        with open("temperaturas.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        temperaturas = []
        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                try:
                    temp = float(partes[1])
                    temperaturas.append(temp)
                except ValueError:
                    pass  # Ignorar si hay un valor inválido

        if temperaturas:
            promedio = sum(temperaturas) / len(temperaturas)
            maximo = max(temperaturas)
            minimo = min(temperaturas)

            with open("resumen_temperaturas.txt", "w") as f_out:
                f_out.write(f"Promedio: {promedio:.2f}\n")
                f_out.write(f"Máximo: {maximo}\n")
                f_out.write(f"Mínimo: {minimo}\n")

            print("Archivo resumen_temperaturas.txt generado con éxito.")
        else:
            print("No se encontraron datos válidos.")

    except FileNotFoundError:
        print("El archivo temperaturas.txt no existe.")

procesar_temperaturas()
