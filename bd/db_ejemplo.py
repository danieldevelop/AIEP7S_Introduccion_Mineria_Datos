""" Module Database 26 Jun 2024 """

#!importar librerias a utilizar
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


#!Conectar con la base de Datos (en memoria)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


#!Crear tabla ventas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY,
        precio REAL,
        gastos_publicidad REAL,
        cantidad_vendida INTEGER
    )
''')


#!Insertar datos en la tabla
datos_ventas = [
    (100, 200, 50),
    (150, 250, 60),
    (200, 300, 70),
    (250, 350, 80),
    (300, 400, 90)
]

cursor.executemany('''
    INSERT INTO ventas(precio, gastos_publicidad, cantidad_vendida) VALUES(?, ?, ?)
    ''', datos_ventas
)

conn.commit()


#!Ejecutar la consulta SQL
query = "SELECT precio, gastos_publicidad, cantidad_vendida FROM ventas"
datos = pd.read_sql(query, conn)
print(datos)


#!Definir variable independiente (X) y variable dependiente (Y)
X = datos[
        ['precio', 'gastos_publicidad']
    ]
Y = datos['cantidad_vendida']


#!Crear y entrena el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, Y)


#!Obtener los coeficientes e interceptos
coeficientes = modelo.coef_
intercepto = modelo.intercept_
print(f'\nCoeficientes: {coeficientes} and Intercepto: {intercepto}')


#!Hacer predicciones
predicciones = modelo.predict(X)


#!Evaluar modelo
mse = mean_squared_error(Y, predicciones)
r2 = r2_score(Y, predicciones)

print(f'\nMSE: {mse} and R^2 {r2}')


#!Visualizar los resultados
plt.scatter(datos['precio'], Y, color='blue', label='Datos reales')
plt.plot(datos['precio'], predicciones, color='red', label='Predicciones')
plt.xlabel('Precio')
plt.ylabel('Cantidad vendida')
plt.legend()
plt.show()
