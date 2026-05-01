from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Debes iniciar sesion para acceder."
login_manager.login_message_category = "warning"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.controllers.auth_controller import auth_bp
    from app.controllers.product_controller import product_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()
        _seed_initial_data()

    return app


@login_manager.user_loader
def load_user(user_id: int):
    from app.models.user import User
    return User.query.get(int(user_id))


def _seed_initial_data():
    from app.models.product import Product
    from app.models.user import User

    # Productos de ejemplo
    if Product.query.count() == 0:
        db.session.add_all([
            Product(nombre="Teclado mecanico", descripcion="Switches rojos, RGB", precio=199.90, stock=25),
            Product(nombre="Mouse inalambrico", descripcion="Sensor optico 16000 DPI", precio=89.50, stock=40),
            Product(nombre='Monitor 27"', descripcion="IPS 144Hz QHD", precio=1299.00, stock=10),
        ])

    # Usuario admin por defecto (solo si no existe ninguno)
    if User.query.count() == 0:
        admin = User(username="admin")
        admin.set_password("admin123")
        db.session.add(admin)

    db.session.commit()
