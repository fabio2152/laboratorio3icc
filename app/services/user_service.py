from app.models.user import User, ROLES
from app.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def list_users(self):
        return self.repository.find_all()

    def get_user(self, user_id: int):
        return self.repository.find_by_id(user_id)

    def create_user(self, data: dict) -> User:
        self._validate(data, user_id=None)
        user = User(
            nombre=data["nombre"].strip(),
            email=data["email"].strip().lower(),
            username=data["username"].strip(),
            rol=data.get("rol", "usuario"),
        )
        user.set_password(data["password"])
        return self.repository.save(user)

    def update_user(self, user_id: int, data: dict) -> User:
        user = self.repository.find_by_id(user_id)
        if user is None:
            return None
        self._validate(data, user_id=user_id)
        user.nombre = data["nombre"].strip()
        user.email = data["email"].strip().lower()
        user.username = data["username"].strip()
        user.rol = data.get("rol", user.rol)
        # Solo actualiza contraseña si se envió una nueva
        if data.get("password", "").strip():
            user.set_password(data["password"].strip())
        from app import db
        db.session.commit()
        return user

    def delete_user(self, user_id: int, current_user_id: int) -> bool:
        user = self.repository.find_by_id(user_id)
        if user is None:
            return False
        if user.id == current_user_id:
            raise ValueError("No puedes eliminar tu propio usuario.")
        self.repository.delete(user)
        return True

    def _validate(self, data: dict, user_id) -> None:
        if not data.get("nombre", "").strip():
            raise ValueError("El nombre es obligatorio.")
        if not data.get("email", "").strip():
            raise ValueError("El email es obligatorio.")
        if not data.get("username", "").strip():
            raise ValueError("El usuario es obligatorio.")
        if data.get("rol") not in ROLES:
            raise ValueError(f"El rol debe ser: {', '.join(ROLES)}.")

        # Email único
        existing = self.repository.find_by_email(data["email"].strip().lower())
        if existing and existing.id != user_id:
            raise ValueError("Ya existe un usuario con ese email.")

        # Username único
        existing = self.repository.find_by_username(data["username"].strip())
        if existing and existing.id != user_id:
            raise ValueError("Ya existe un usuario con ese nombre de usuario.")

        # Contraseña obligatoria solo al crear
        if user_id is None and not data.get("password", "").strip():
            raise ValueError("La contrasena es obligatoria.")
