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
