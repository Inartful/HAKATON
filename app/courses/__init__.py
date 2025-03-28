from flask import Blueprint

courses = Blueprint("courses", __name__)

from app.courses import routes  # Импортируем маршруты
