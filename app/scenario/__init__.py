from flask import Blueprint

scenario_bp = Blueprint("scenario", __name__)

from app.scenario import routes  # Импортируем маршруты
