# Laboratorio 3 — Tienda MVC

Aplicación web desarrollada en **Python + Flask** con arquitectura **MVC** (Model-View-Controller), siguiendo el patrón de capas **Repository** y **Services**.  
Incluye sistema de autenticación con roles y CRUD completo de Productos y Usuarios.

---

## Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.x |
| Framework web | Flask 3.0 |
| ORM | Flask-SQLAlchemy |
| Autenticación | Flask-Login + Werkzeug (hash de contraseñas) |
| Base de datos | SQLite (por defecto, sin servidor) / MySQL (opcional) |
| Frontend | Bootstrap 5.3 + Bootstrap Icons |
| Gestor de entorno | Python venv |

---

## Estructura de carpetas

```
laboratorio3icc/
│
├── app/                          # Paquete principal de la aplicación
│   ├── __init__.py               # App factory: inicializa Flask, SQLAlchemy, LoginManager
│   │
│   ├── models/                   # CAPA MODELO — entidades de base de datos
│   │   ├── product.py            # Modelo Product  (tabla: productos)
│   │   └── user.py               # Modelo User     (tabla: usuarios)
│   │
│   ├── repository/               # CAPA REPOSITORIO — acceso directo a BD (CRUD ORM)
│   │   ├── product_repository.py
│   │   └── user_repository.py
│   │
│   ├── services/                 # CAPA SERVICIO — lógica de negocio y validaciones
│   │   ├── product_service.py
│   │   ├── user_service.py
│   │   └── auth_service.py
│   │
│   ├── controllers/              # CAPA CONTROLADOR — rutas y blueprints Flask
│   │   ├── product_controller.py # Rutas CRUD /products
│   │   ├── user_controller.py    # Rutas CRUD /users
│   │   └── auth_controller.py    # Rutas /login  /logout
│   │
│   ├── templates/                # CAPA VISTA — plantillas HTML (Jinja2)
│   │   ├── base.html             # Layout base con navbar
│   │   ├── login.html            # Pantalla de inicio de sesión
│   │   ├── index.html            # Listado de productos
│   │   ├── form.html             # Formulario crear/editar producto
│   │   ├── detail.html           # Detalle de producto
│   │   ├── 403.html              # Página acceso denegado
│   │   └── users/
│   │       ├── index.html        # Listado de usuarios
│   │       └── form.html         # Formulario crear/editar usuario
│   │
│   ├── static/
│   │   └── css/style.css         # Estilos personalizados
│   │
│   └── utils/
│       └── decorators.py         # Decorador @admin_required
│
├── config.py                     # Configuración (lee variables de .env)
├── run.py                        # Punto de entrada: python run.py
├── requirements.txt              # Dependencias Python
├── schema.sql                    # Estructura de la base de datos (referencia)
├── tienda.db                     # Base de datos SQLite (generada automáticamente)
└── .env.example                  # Plantilla de variables de entorno
```

---

## Estructura de la Base de Datos

### Tabla `productos`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Identificador único (autoincremental) |
| nombre | VARCHAR(120) | Nombre del producto — obligatorio |
| descripcion | TEXT | Descripción opcional |
| precio | DECIMAL(10,2) | Precio del producto |
| stock | INTEGER | Unidades disponibles |

### Tabla `usuarios`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Identificador único (autoincremental) |
| nombre | VARCHAR(120) | Nombre completo — obligatorio |
| email | VARCHAR(120) UNIQUE | Correo electrónico — obligatorio |
| username | VARCHAR(80) UNIQUE | Nombre de usuario para login |
| password_hash | VARCHAR(256) | Contraseña cifrada con Werkzeug |
| rol | VARCHAR(20) | `admin` o `usuario` |

> El archivo `schema.sql` contiene la definición completa de ambas tablas.

---

## Flujo de Arquitectura MVC

```
Solicitud HTTP
      │
      ▼
 Controller  →  Service  →  Repository  →  Model (SQLAlchemy)
 (Blueprint)    (lógica)    (acceso BD)     (tabla BD)
      │
      ▼
  Template (Jinja2) → Respuesta HTML
```

---

## Sistema de Roles y Permisos

| Acción | Rol `admin` | Rol `usuario` |
|---|---|---|
| Ver lista de productos | ✅ | ✅ |
| Ver detalle de producto | ✅ | ✅ |
| Crear / Editar / Eliminar producto | ✅ | ❌ (403) |
| Ver lista de usuarios | ✅ | ✅ |
| Crear / Editar / Eliminar usuario | ✅ | ❌ (403) |

---

## Instalación y ejecución

### Prerrequisitos
- Python 3.9 o superior
- Git

### Pasos

**1. Clonar el repositorio**
```bash
git clone https://github.com/fabio2152/laboratorio3icc.git
cd laboratorio3icc
```

**2. Crear y activar el entorno virtual**
```bash
# Crear
python -m venv venv

# Activar en Windows (CMD)
venv\Scripts\activate

# Activar en Windows (Git Bash) / Linux / Mac
source venv/Scripts/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Configurar variables de entorno**
```bash
# Windows CMD
copy .env.example .env

# Git Bash / Linux / Mac
cp .env.example .env
```
> El archivo `.env` ya viene configurado para SQLite. No necesitas instalar ningún servidor de base de datos.

**5. Ejecutar la aplicación**
```bash
python run.py
```

**6. Abrir en el navegador**
```
http://127.0.0.1:5000/
```

> La base de datos (`tienda.db`) y los datos de ejemplo se crean **automáticamente** al primer arranque.

---

## Credenciales de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | 🛡 Admin — acceso total |
| `demo` | `demo123` | 👤 Usuario — solo lectura |

---

## Rutas disponibles

| Método | Ruta | Descripción | Requiere |
|---|---|---|---|
| GET | `/login` | Pantalla de inicio de sesión | — |
| POST | `/login` | Procesar login | — |
| GET | `/logout` | Cerrar sesión | Login |
| GET | `/` | Listado de productos | Login |
| GET | `/products/<id>` | Detalle de producto | Login |
| GET/POST | `/products/new` | Crear producto | Admin |
| GET/POST | `/products/<id>/edit` | Editar producto | Admin |
| POST | `/products/<id>/delete` | Eliminar producto | Admin |
| GET | `/users/` | Listado de usuarios | Login |
| GET/POST | `/users/new` | Crear usuario | Admin |
| GET/POST | `/users/<id>/edit` | Editar usuario | Admin |
| POST | `/users/<id>/delete` | Eliminar usuario | Admin |

---

## Dependencias principales

```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
PyMySQL==1.1.1
python-dotenv==1.0.1
```

---

*Laboratorio 3 — Ingeniería en Ciencias de la Computación (ICC) — UTEC*
