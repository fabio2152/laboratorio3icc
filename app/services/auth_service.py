from app.models.user import User
from app.repository.user_repository import UserRepository


class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    def authenticate(self, username: str, password: str):
        """Retorna el User si las credenciales son correctas, None si no."""
        if not username or not password:
            return None
        user = self.repository.find_by_username(username.strip())
        if user and user.check_password(password):
            return user
        return None

    def get_user_by_id(self, user_id: int):
        return self.repository.find_by_id(user_id)

    def create_user(self, username: str, password: str) -> User:
        user = User(username=username)
        user.set_password(password)
        return self.repository.save(user)

    def has_any_user(self) -> bool:
        return self.repository.count() > 0
