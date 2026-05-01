-- ============================================================
--  Laboratorio 3 ICC — Tienda MVC
--  Base de datos: SQLite (por defecto) o MySQL
--  Para MySQL: ejecutar con  mysql -u root -p < schema.sql
-- ============================================================

-- *** Solo necesario en MySQL ***
-- CREATE DATABASE IF NOT EXISTS tienda
--   CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- USE tienda;

-- ------------------------------------------------------------
--  Tabla: productos
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS productos (
  id          INTEGER      PRIMARY KEY AUTOINCREMENT,
  nombre      VARCHAR(120) NOT NULL,
  descripcion TEXT,
  precio      DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  stock       INTEGER      NOT NULL DEFAULT 0
);

-- ------------------------------------------------------------
--  Tabla: usuarios
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  nombre        VARCHAR(120) NOT NULL,
  email         VARCHAR(120) NOT NULL UNIQUE,
  username      VARCHAR(80)  NOT NULL UNIQUE,
  password_hash VARCHAR(256) NOT NULL,
  rol           VARCHAR(20)  NOT NULL DEFAULT 'usuario'
    CHECK (rol IN ('admin', 'usuario'))
);

-- ------------------------------------------------------------
--  Datos de ejemplo — productos
-- ------------------------------------------------------------
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
  ('Teclado mecanico',  'Switches rojos, RGB',    199.90, 25),
  ('Mouse inalambrico', 'Sensor optico 16000 DPI',  89.50, 40),
  ('Monitor 27"',       'IPS 144Hz QHD',          1299.00, 10);

-- ------------------------------------------------------------
--  Datos de ejemplo — usuarios
--  (contrasenas gestionadas por la app con Werkzeug hash)
--  admin  / admin123  → rol admin
--  demo   / demo123   → rol usuario
-- ------------------------------------------------------------
-- Los registros los crea automaticamente la app al primer arranque.
-- Ver: app/__init__.py  → _seed_initial_data()
