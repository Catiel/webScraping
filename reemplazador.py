import csv
import random

def remplazar_valores_faltantes(ruta_archivo_entrada, ruta_archivo_salida):
    with open(ruta_archivo_entrada, 'r', newline='') as archivo_entrada:
        # Crear un lector CSV
        lector_csv = csv.reader(archivo_entrada)
        # Crear una lista para almacenar los datos actualizados
        datos_actualizados = []
        # Iterar sobre cada fila en el archivo CSV de entrada
        for fila in lector_csv:
            # Iterar sobre cada valor en la fila
            fila_actualizada = []
            for valor in fila:
                # Si el valor es "--", reemplazarlo con un número aleatorio 
                if valor == "--":
                    valor = str(random.randint(1200000, 100000))
                # Agregar el valor a la fila actualizada
                fila_actualizada.append(valor)
            # Agregar la fila actualizada a la lista de datos actualizados
            datos_actualizados.append(fila_actualizada)

    # Escribir los datos actualizados en el archivo CSV de salida
    with open(ruta_archivo_salida, 'w', newline='') as archivo_salida:
        # Crear un escritor CSV
        escritor_csv = csv.writer(archivo_salida)
        # Escribir los datos actualizados en el archivo CSV de salida
        for fila in datos_actualizados:
            escritor_csv.writerow(fila)


ruta_archivo_entrada = 'property-listing-2024-04-09-12-52-11.csv'  
ruta_archivo_salida = 'datos_modificados.csv' 
remplazar_valores_faltantes(ruta_archivo_entrada, ruta_archivo_salida)
print("Valores faltantes reemplazados correctamente con números aleatorios entre 100 y 999. Los datos modificados se han guardado en el archivo 'datos_modificados.csv'.")