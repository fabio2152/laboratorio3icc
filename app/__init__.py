from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.controllers.product_controller import product_bp
    app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()
        _seed_initial_data()

    return app


def _seed_initial_data():
    from app.models.product import Product
    if Product.query.count() > 0:
        return
    db.session.add_all([
        Product(nombre="Teclado mecanico", descripcion="Switches rojos, RGB", precio=199.90, stock=25),
        Product(nombre="Mouse inalambrico", descripcion="Sensor optico 16000 DPI", precio=89.50, stock=40),
        Product(nombre='Monitor 27"', descripcion="IPS 144Hz QHD", precio=1299.00, stock=10),
    ])
    db.session.commit()
