
# ENLACE DE GIT
# https://github.com/DiegoSolorzano9/Inteligencia_Artificial_I/tree/5dcfa68fba0f5b93ca2d3123088618fa3276fea5/Practica%201%20-%20peso%20y%20estatura


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Función para generar los datos
def generar_datos(n=100):
    estaturas = np.random.uniform(1.4, 2.0, n)  # Estatura entre 1.40 y 2.0 metros
    pesos = []
    
    for estatura in estaturas:
        if estatura < 1.5:
            peso = np.random.uniform(40, 60)
        elif 1.5 <= estatura < 1.7:
            peso = np.random.uniform(50, 70)
        elif 1.7 <= estatura < 1.9:
            peso = np.random.uniform(60, 90)
        else:
            peso = np.random.uniform(70, 100)
        
        pesos.append(peso)
    
    return np.array(pesos), estaturas


# Generar los datos sin fijar una semilla, para que los valores cambien en cada ejecución
pesos, estaturas = generar_datos()
# Crear un DataFrame con los datos, ajustando el índice para que vaya de 1 a 100
df = pd.DataFrame({'Peso (kg)': pesos, 'Estatura (m)': estaturas}, index=np.arange(1, 101))
# Muestra todos los valores generados en la terminal
print(df)



# Calcular la línea de tendencia (regresión lineal simple)
slope, intercept, r_value, p_value, std_err = linregress(df['Estatura (m)'], df['Peso (kg)'])
# Imprimir la ecuación de la recta
print(f"\nLa ecuación de la recta es: Peso = {slope:.2f} * Estatura + {intercept:.2f}")


# Graficar los puntos y la curva de regresión
plt.scatter(df['Estatura (m)'], df['Peso (kg)'], label='Datos')
# Para asegurar que la línea de tendencia cubra el rango de los datos, utilizamos los valores mínimo y máximo de estatura
x = np.linspace(df['Estatura (m)'].min(), df['Estatura (m)'].max(), 100)
y = slope * x + intercept
plt.plot(x, y, 'r', label='Línea de Tendencia')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.title('Distribución de Peso vs Estatura')
plt.grid(True)
plt.legend()
plt.show()
