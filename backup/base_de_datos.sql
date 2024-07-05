BEGIN TRANSACTION;
CREATE TABLE cliente(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ubicacion TEXT
    );
INSERT INTO "cliente" VALUES(1,'Juan','Lima');
INSERT INTO "cliente" VALUES(2,'Pedro','Cusco');
INSERT INTO "cliente" VALUES(3,'Maria','Arequipa');
INSERT INTO "cliente" VALUES(4,'Ana','Piura');
INSERT INTO "cliente" VALUES(5,'Luis','Ica');
INSERT INTO "cliente" VALUES(6,'Rosa','Tacna');
INSERT INTO "cliente" VALUES(7,'Carlos','Puno');
INSERT INTO "cliente" VALUES(8,'Sofia','Cajamarca');
INSERT INTO "cliente" VALUES(9,'Elena','Loreto');
INSERT INTO "cliente" VALUES(10,'Jorge','Junin');
CREATE TABLE producto(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        categoria TEXT
    );
INSERT INTO "producto" VALUES(1,'Tubos','Cerámica');
INSERT INTO "producto" VALUES(2,'Camisa Caballero','Confección');
INSERT INTO "producto" VALUES(3,'Raqueta Tenis','Deportes');
INSERT INTO "producto" VALUES(4,'Zapatos','Calzado');
INSERT INTO "producto" VALUES(5,'Cartera','Marroquinería');
INSERT INTO "producto" VALUES(6,'Alicates','Ferretería');
INSERT INTO "producto" VALUES(7,'Cepillo','Hogar');
INSERT INTO "producto" VALUES(8,'Pintura','Arte');
INSERT INTO "producto" VALUES(9,'Pantalón Dama','Confección');
INSERT INTO "producto" VALUES(10,'Pelota','Deportes');
INSERT INTO "producto" VALUES(11,'Consola Video','Juguetería');
INSERT INTO "producto" VALUES(12,'Cama','Hogar');
INSERT INTO "producto" VALUES(13,'Pincel','Arte');
INSERT INTO "producto" VALUES(14,'Martillo','Ferretería');
INSERT INTO "producto" VALUES(15,'Billetera','Marroquinería');
CREATE TABLE venta(
        id INTEGER PRIMARY KEY,
        precio REAL,
        cantidad_vendida INTEGER,
        producto_id INTEGER,
        cliente_id INTEGER,
        CONSTRAINT fk_producto_id FOREIGN KEY(producto_id) REFERENCES producto(producto_id),
        CONSTRAINT fk_cliente_id FOREIGN key(cliente_id) REFERENCES cliente(cliente_id)
    );
INSERT INTO "venta" VALUES(1,100.0,10,1,1);
INSERT INTO "venta" VALUES(2,50.0,5,2,2);
INSERT INTO "venta" VALUES(3,200.0,20,3,3);
INSERT INTO "venta" VALUES(4,80.0,8,4,4);
INSERT INTO "venta" VALUES(5,150.0,15,5,5);
INSERT INTO "venta" VALUES(6,300.0,30,6,6);
INSERT INTO "venta" VALUES(7,120.0,12,7,7);
INSERT INTO "venta" VALUES(8,70.0,7,8,8);
INSERT INTO "venta" VALUES(9,250.0,25,9,9);
INSERT INTO "venta" VALUES(10,180.0,18,10,10);
INSERT INTO "venta" VALUES(11,350.0,35,11,1);
INSERT INTO "venta" VALUES(12,130.0,13,12,2);
INSERT INTO "venta" VALUES(13,60.0,6,13,3);
INSERT INTO "venta" VALUES(14,270.0,27,14,4);
INSERT INTO "venta" VALUES(15,190.0,19,15,5);
COMMIT;
