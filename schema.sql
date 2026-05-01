CREATE DATABASE IF NOT EXISTS tienda
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE tienda;

CREATE TABLE IF NOT EXISTS productos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL,
  descripcion TEXT,
  precio DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  stock INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
  ('Teclado mecanico', 'Switches rojos, RGB', 199.90, 25),
  ('Mouse inalambrico', 'Sensor optico 16000 DPI', 89.50, 40),
  ('Monitor 27"', 'IPS 144Hz QHD', 1299.00, 10);
