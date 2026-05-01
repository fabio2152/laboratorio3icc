from app.models.product import Product
from app.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def list_products(self):
        return self.repository.find_all()

    def get_product(self, product_id: int):
        return self.repository.find_by_id(product_id)

    def create_product(self, data: dict) -> Product:
        self._validate(data)
        product = Product(
            nombre=data["nombre"].strip(),
            descripcion=(data.get("descripcion") or "").strip(),
            precio=float(data["precio"]),
            stock=int(data["stock"]),
        )
        return self.repository.save(product)

    def update_product(self, product_id: int, data: dict):
        product = self.repository.find_by_id(product_id)
        if product is None:
            return None
        self._validate(data)
        clean = {
            "nombre": data["nombre"].strip(),
            "descripcion": (data.get("descripcion") or "").strip(),
            "precio": float(data["precio"]),
            "stock": int(data["stock"]),
        }
        return self.repository.update(product, clean)

    def delete_product(self, product_id: int) -> bool:
        product = self.repository.find_by_id(product_id)
        if product is None:
            return False
        self.repository.delete(product)
        return True

    @staticmethod
    def _validate(data: dict) -> None:
        if not data.get("nombre") or not str(data["nombre"]).strip():
            raise ValueError("El nombre es obligatorio.")
        try:
            precio = float(data.get("precio"))
            if precio < 0:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un numero mayor o igual a 0.")
        try:
            stock = int(data.get("stock"))
            if stock < 0:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un entero mayor o igual a 0.")
