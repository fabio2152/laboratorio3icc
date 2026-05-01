# Laboratorio 3 — Tienda MVC

Aplicación web con arquitectura **MVC** en **Flask**, incluyendo autenticación por roles y CRUD completo.

---

## ⚡ Inicio rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/fabio2152/laboratorio3icc.git
cd laboratorio3icc
```

### 2. Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar
```bash
python run.py
```

**Abre en el navegador:** http://127.0.0.1:5000/

> ℹ️ La base de datos SQLite se crea **automáticamente** al primer arranque con datos de ejemplo.

---

## 👤 Credenciales de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | 🛡 Admin — acceso total |
| `demo` | `demo123` | 👤 Usuario — solo lectura |

---

## 📋 Rutas principales

| Ruta | Descripción | Requiere |
|---|---|---|
| `/login` | Iniciar sesión | — |
| `/` | Listado de productos | Login |
| `/products/new` | Crear producto | Admin |
| `/products/<id>/edit` | Editar producto | Admin |
| `/users/` | Listado de usuarios | Login |
| `/users/new` | Crear usuario | Admin |
| `/logout` | Cerrar sesión | Login |

---

## 🛠️ Stack tecnológico

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.x |
| Framework | Flask 3.0 |
| BD | SQLite (sin servidor) / MySQL (opcional) |
| ORM | SQLAlchemy |
| Autenticación | Flask-Login + Werkzeug (hash) |
| Frontend | Bootstrap 5.3 + Bootstrap Icons |

---

## 📁 Estructura de carpetas

```
laboratorio3icc/
│
├── app/                          # Aplicación principal
│   ├── models/                   # CAPA MODELO — entidades
│   │   ├── product.py            # Tabla: productos
│   │   └── user.py               # Tabla: usuarios
│   │
│   ├── repository/               # CAPA REPOSITORIO — acceso BD (CRUD)
│   │   ├── product_repository.py
│   │   └── user_repository.py
│   │
│   ├── services/                 # CAPA SERVICIO — lógica de negocio
│   │   ├── product_service.py
│   │   ├── user_service.py
│   │   └── auth_service.py
│   │
│   ├── controllers/              # CAPA CONTROLADOR — rutas Flask
│   │   ├── product_controller.py
│   │   ├── user_controller.py
│   │   └── auth_controller.py
│   │
│   ├── templates/                # CAPA VISTA — plantillas HTML
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── index.html
│   │   ├── form.html
│   │   └── users/
│   │       ├── index.html
│   │       └── form.html
│   │
│   ├── static/css/style.css      # Estilos personalizados
│   └── utils/decorators.py       # Decorador @admin_required
│
├── config.py                     # Configuración de la app
├── run.py                        # Punto de entrada
├── requirements.txt              # Dependencias
├── schema.sql                    # Estructura de BD (referencia)
├── tienda.db                     # Base de datos SQLite
└── .env.example                  # Plantilla de variables de entorno
```

---

## 🗄️ Base de datos

### Tabla `productos`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Identificador único |
| nombre | VARCHAR(120) | Nombre del producto |
| descripcion | TEXT | Descripción opcional |
| precio | DECIMAL(10,2) | Precio |
| stock | INTEGER | Unidades disponibles |

### Tabla `usuarios`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Identificador único |
| nombre | VARCHAR(120) | Nombre completo |
| email | VARCHAR(120) | Correo electrónico (único) |
| username | VARCHAR(80) | Usuario para login (único) |
| password_hash | VARCHAR(256) | Contraseña cifrada |
| rol | VARCHAR(20) | `admin` o `usuario` |

> Ver `schema.sql` para la definición completa.

---

## 🔐 Sistema de roles

| Acción | Admin | Usuario |
|---|---|---|
| Ver productos | ✅ | ✅ |
| Crear/Editar/Eliminar producto | ✅ | ❌ |
| Ver usuarios | ✅ | ✅ |
| Crear/Editar/Eliminar usuario | ✅ | ❌ |

---

## 🏗️ Arquitectura MVC

```
Cliente HTTP
    │
    ▼
Controlador  ──→  Servicio  ──→  Repositorio  ──→  Modelo (SQLAlchemy)
(Ruta)         (Validación)    (CRUD ORM)         (Tabla BD)
    │
    ▼
Plantilla HTML (Jinja2)
    │
    ▼
Respuesta HTTP
```

---

## 📦 Dependencias

```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
PyMySQL==1.1.1
python-dotenv==1.0.1
```

---

*Laboratorio 3 — Ingeniería en Ciencias de la Computación (ICC) — UTEC*
