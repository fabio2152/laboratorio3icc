from app import db
from app.models.product import Product


class ProductRepository:
    def find_all(self):
        return Product.query.order_by(Product.id.desc()).all()

    def find_by_id(self, product_id: int):
        return Product.query.get(product_id)

    def save(self, product: Product) -> Product:
        db.session.add(product)
        db.session.commit()
        return product

    def update(self, product: Product, data: dict) -> Product:
        for key, value in data.items():
            if hasattr(product, key):
                setattr(product, key, value)
        db.session.commit()
        return product

    def delete(self, product: Product) -> None:
        db.session.delete(product)
        db.session.commit()
