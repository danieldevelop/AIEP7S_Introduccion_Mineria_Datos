
    SELECT v.precio, v.cantidad_vendida, p.categoria, c.ubicacion
    FROM venta v
    JOIN producto p ON v.producto_id = p.id
    JOIN cliente c ON v.cliente_id = c.id
    ORDER BY v.precio DESC;
