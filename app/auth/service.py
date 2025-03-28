from app.models import db, User
from app import bcrypt

def register_user(username, password):
    username = username.strip()
    password = password.strip()

    if len(password) < 6:
        return False, "Пароль должен быть минимум 6 символов!"

    existing_user = User.query.filter(User.username.ilike(username)).first()
    if existing_user:
        return False, "Имя пользователя уже занято!"

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return True, "Регистрация успешна!"

def authenticate_user(username, password):
    user = User.query.filter(User.username.ilike(username)).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user, None
    return None, "Неверный логин или пароль!"
