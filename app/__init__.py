from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

# Инициализация Flask
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Подключаем расширения
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Импортируем блюпринты (модули маршрутов)
    from app.routes import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    return app
