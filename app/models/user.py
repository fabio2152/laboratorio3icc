from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

ROL_ADMIN = "admin"
ROL_USUARIO = "usuario"
ROLES = [ROL_ADMIN, ROL_USUARIO]


class User(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default=ROL_USUARIO)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self) -> bool:
        return self.rol == ROL_ADMIN

    def __repr__(self):
        return f"<User {self.username} ({self.rol})>"
