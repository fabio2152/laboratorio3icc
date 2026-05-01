from app import db
from app.models.user import User


class UserRepository:
    def find_all(self):
        return User.query.order_by(User.id.asc()).all()

    def find_by_id(self, user_id: int):
        return User.query.get(user_id)

    def find_by_username(self, username: str):
        return User.query.filter_by(username=username).first()

    def find_by_email(self, email: str):
        return User.query.filter_by(email=email).first()

    def save(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user: User, data: dict) -> User:
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        db.session.commit()
        return user

    def delete(self, user: User) -> None:
        db.session.delete(user)
        db.session.commit()

    def count(self) -> int:
        return User.query.count()
