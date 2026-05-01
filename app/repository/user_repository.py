from app import db
from app.models.user import User


class UserRepository:
    def find_by_id(self, user_id: int):
        return User.query.get(user_id)

    def find_by_username(self, username: str):
        return User.query.filter_by(username=username).first()

    def save(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    def count(self) -> int:
        return User.query.count()
