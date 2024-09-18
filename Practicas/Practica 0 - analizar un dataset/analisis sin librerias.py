import csv
from typing import Counter

# Abre el archivo CSV
with open('Tarea1/fifa_players.csv', newline='', encoding='utf-8') as csvfile:
    # Lee el contenido del archivo
    reader = csv.reader(csvfile)
    
    # Inicializa una lista para almacenar los datos
    datos = []
    
    # Itera sobre las filas del archivo
    for fila in reader:
        # Agrega cada fila a la lista de datos
        datos.append(fila)

# Imprime los datos para ver cómo lucen
for fila in datos:
    print(fila)

print("---------------------------------------------------Analisis del dataset------------------------------------------------------------------")

#cuenta el número de filas y columnas
num_filas = len(datos)
num_columnas = len(datos[0]) if num_filas > 0 else 0

# Imprime el número de filas y columnas
print(f"Número de filas: {num_filas}")
print(f"Número de columnas: {num_columnas}")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Obtener la lista de nombres de las columnas    
print("Nombres de las columnas:")
nombres_columnas = datos[0]
print(nombres_columnas)

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")


from datetime import datetime

# Supongamos que la columna de fecha de nacimiento es la columna 2
indice_columna_fecha_nacimiento = 2

# Función para calcular la edad a partir de la fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%m/%d/%Y')  # Formato MM/DD/YYYY
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Calcula las edades basándose en las fechas de nacimiento
edades = [calcular_edad(fila[indice_columna_fecha_nacimiento]) for fila in datos[1:] if fila[indice_columna_fecha_nacimiento]]

# Calcula la edad promedio
edad_promedio = sum(edades) / len(edades)
print(f"La edad promedio de los jugadores es {edad_promedio:.2f}")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

edad_minima = min(edades)
edad_maxima = max(edades)

print(f"La edad mínima es {edad_minima}")
print(f"La edad máxima es {edad_maxima}")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

indice_columna_nombre = 0
indice_columna_valoracion = 8

mejor_jugador = max(datos[1:], key=lambda fila: int(fila[indice_columna_valoracion]))
nombre_mejor_jugador = mejor_jugador[indice_columna_nombre]
mejor_valoracion = mejor_jugador[indice_columna_valoracion]

print(f"El mejor jugador es {nombre_mejor_jugador} con una valoración general de {mejor_valoracion}.")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

indice_columna_potencial = 9

# Ordena los jugadores por potencial
jugadores_ordenados = sorted(datos[1:], key=lambda fila: int(fila[indice_columna_potencial]), reverse=True)

# Imprime los 5 jugadores con mayor potencial
print("Top 5 Jugadores con Mayor Potencial:")
for jugador in jugadores_ordenados[:5]:
    nombre = jugador[indice_columna_nombre]
    potencial = jugador[indice_columna_potencial]
    print(f"* {nombre}: Potencial de {potencial}")













