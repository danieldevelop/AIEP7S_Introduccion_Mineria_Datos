""" Module export database 03/07/2024 """

import sqlite3
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


#Conectar a la base de datos
conn = sqlite3.connect(':memory:');
cursor = conn.cursor();


#Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS producto(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        categoria TEXT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ubicacion TEXT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS venta(
        id INTEGER PRIMARY KEY,
        precio REAL,
        cantidad_vendida INTEGER,
        producto_id INTEGER,
        cliente_id INTEGER,
        CONSTRAINT fk_producto_id FOREIGN KEY(producto_id) REFERENCES producto(producto_id),
        CONSTRAINT fk_cliente_id FOREIGN key(cliente_id) REFERENCES cliente(cliente_id)
    );
''')


#Insertar datos
datos_producto = [
    (1, 'Tubos', 'Cerámica'),
    (2, 'Camisa Caballero', 'Confección'),
    (3, 'Raqueta Tenis', 'Deportes'),
    (4, 'Zapatos', 'Calzado'),
    (5, 'Cartera', 'Marroquinería'),
    (6, 'Alicates', 'Ferretería'),
    (7, 'Cepillo', 'Hogar'),
    (8, 'Pintura', 'Arte'),
    (9, 'Pantalón Dama', 'Confección'),
    (10, 'Pelota', 'Deportes'),
    (11, 'Consola Video', 'Juguetería'),
    (12, 'Cama', 'Hogar'),
    (13, 'Pincel', 'Arte'),
    (14, 'Martillo', 'Ferretería'),
    (15, 'Billetera', 'Marroquinería')
]

cursor.executemany('''
    INSERT INTO producto(id, nombre, categoria) VALUES(?, ?, ?)
''', datos_producto)

datos_cliente = [
    (1, 'Juan', 'Lima'),
    (2, 'Pedro', 'Cusco'),
    (3, 'Maria', 'Arequipa'),
    (4, 'Ana', 'Piura'),
    (5, 'Luis', 'Ica'),
    (6, 'Rosa', 'Tacna'),
    (7, 'Carlos', 'Puno'),
    (8, 'Sofia', 'Cajamarca'),
    (9, 'Elena', 'Loreto'),
    (10, 'Jorge', 'Junin')
]

cursor.executemany('''
    INSERT INTO cliente(id, nombre, ubicacion) VALUES(?, ?, ?)
''', datos_cliente)

datos_venta = [
    (1, 100, 10, 1, 1),
    (2, 50, 5, 2, 2),
    (3, 200, 20, 3, 3),
    (4, 80, 8, 4, 4),
    (5, 150, 15, 5, 5),
    (6, 300, 30, 6, 6),
    (7, 120, 12, 7, 7),
    (8, 70, 7, 8, 8),
    (9, 250, 25, 9, 9),
    (10, 180, 18, 10, 10),
    (11, 350, 35, 11, 1),
    (12, 130, 13, 12, 2),
    (13, 60, 6, 13, 3),
    (14, 270, 27, 14, 4),
    (15, 190, 19, 15, 5)
]

cursor.executemany('''
    INSERT INTO venta(id, precio, cantidad_vendida, producto_id, cliente_id) VALUES(?, ?, ?, ?, ?)
''', datos_venta)

conn.commit()


#Ejecutar consulta para unir y mostrar datos
# QUERY = '''
#     SELECT producto.nombre, SUM(venta.precio * venta.cantidad_vendida) AS total
#     FROM producto
#     JOIN venta ON producto.id = venta.producto_id
#     GROUP BY producto.nombre
#     ORDER BY total DESC
# '''
QUERY = '''
    SELECT v.precio, v.cantidad_vendida, p.categoria, c.ubicacion
    FROM venta v
    JOIN producto p ON v.producto_id = p.id
    JOIN cliente c ON v.cliente_id = c.id
    ORDER BY v.precio DESC;
'''

datos = pd.read_sql(QUERY, conn)
# print(datos)


#Exportar BD completa a un .sql
with open('../backup/base_de_datos.sql', 'w') as f:
    for linea in conn.iterdump():
        f.write('%s\n' % linea)

#Exportar BD a un archivo .sqlite
db_join_sqlite = sqlite3.connect('../backup/base_de_datos.sqlite')
conn.backup(db_join_sqlite)
db_join_sqlite.close()


#Cerrar conexion
conn.close()


# Exportar consulta sql (join)
with open('../backup/consulta_union.sql', 'w') as file:
    file.write(QUERY)


#Convertir columnas a variables dummy
datos_dummies = pd.get_dummies(datos, columns=['categoria', 'ubicacion'], drop_first=True)
print(datos_dummies)


#Definir variables X e Y
X = datos_dummies.drop(columns=['cantidad_vendida'])
Y = datos_dummies['cantidad_vendida']


#Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, Y)


#Obtener coeficientes e interceptos
coeficientes = modelo.coef_
intercepto = modelo.intercept_

print(f'Coeficientes : {coeficientes}')
print(f'Intercepto: {intercepto}')


#Predicciones
predicciones = modelo.predict(X)


#Evaluacion del modelo
mse = mean_squared_error(Y, predicciones)
r2 = r2_score(Y, predicciones)

print(f'MSE: {mse}')
print(f'R^2: {r2}')


plt.scatter(datos['precio'], Y, color='blue', label='Datos Reales')
plt.plot(datos['precio'], predicciones, color='red', label='Predicciones')
plt.xlabel('Precio')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.show()
