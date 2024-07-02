""" Module Database 07 Jul 2024 """

# * Importar librerias a utilizar
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt



# * Conectar a la base de datos (en memoria)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor() # Este es un puntero que se mueve por la base de datos. Es el que ejecuta las consultas, no la conexión.



# * Crear tablas ventas y productos
TBL_PRODUCTOS = '''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER,
        nombre TEXT,
        categoria TEXT,
        CONSTRAINT pk_productos_id PRIMARY KEY (id)
    );
'''
cursor.execute(TBL_PRODUCTOS);

TBL_VENTAS = '''
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER,
        producto_id INTEGER,
        precio REAL,
        cantidad_vendida INTEGER,
        CONSTRAINT pk_ventas_id PRIMARY KEY (id),
        CONSTRAINT fk_producto_id FOREIGN KEY (producto_id) REFERENCES productos(id)
    );
'''
cursor.execute(TBL_VENTAS);



# * Insertar datos en las tablas
datos_productos = [
    (1, 'Producto A', 'Categoria 1'),
    (2, 'Producto B', 'Categoria 2'),
    (3, 'Producto C', 'Categoria 3'),
    (4, 'Producto D', 'Categoria 4'),
    (5, 'Producto E', 'Categoria 5')
]
cursor.executemany('''
    INSERT INTO productos(id, nombre, categoria) VALUES(?, ?, ?)
''', datos_productos)

datos_ventas = [
    (1, 1, 100, 50),
    (2, 2, 150, 60),
    (3, 3, 200, 70),
    (4, 4, 250, 80),
    (5, 5, 300, 90)
]
cursor.executemany('''
    INSERT INTO ventas(id, producto_id, precio, cantidad_vendida) VALUES(?, ?, ?, ?)
''', datos_ventas)

conn.commit()



# * Ejecutar consulta SQL para unir las tablas y obtener datos
QUERY = '''
    SELECT v.precio, v.cantidad_vendida, p.categoria 
    FROM ventas v
    INNER JOIN productos p ON v.producto_id = p.id
'''

datos = pd.read_sql(QUERY, conn)
print(datos)



# * Convertir variable categoria a variable dummy
datos_dummy = pd.get_dummies(datos, columns=['categoria'], drop_first=True)
print(datos_dummy)



# * Definir variables independientes [X] y la variable dependiente [Y]
X = datos_dummy[
    ['precio', 'categoria_Categoria 2']
]
Y = datos_dummy[('cantidad_vendida')]



# * Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, Y)



# * Obtener coeficientes e intercepto
coeficientes = modelo.coef_
intercepro = modelo.intercept_

print(f'\nCoeficientes: {coeficientes} and Intercepto: {intercepro}')



# * Hacer predicciones
predicciones = modelo.predict(X)



# * Evaluar el modelo
mse = mean_squared_error(Y, predicciones)
r2 = r2_score(Y, predicciones)

print(f'\nMSE: {mse} and R^2: {r2}')



# * Visualizar los datos
plt.scatter(datos['precio'], Y, color='blue', label='Datos Reales')
plt.plot(datos['precio'], predicciones, color='red', label='Predicciones')
plt.xlabel('Precio')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.show()
