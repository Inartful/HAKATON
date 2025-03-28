from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
import os



# Инициализация Flask
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("templates")  # 👈 Принудительно указываем путь к шаблонам
    )
    app.config.from_object(Config)

    # Подключаем расширения
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Функция загрузки пользователя
    from app.auth.models import User  # Убедись, что путь правильный

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Импортируем блюпринты (модули маршрутов)
    from app.routes import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    return app
