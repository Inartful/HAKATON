from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Главная страница. <a href='/auth/login'>Войти</a>"

@main.route("/profile")
@login_required
def profile():
    return f"Привет, {current_user.username}! <a href='/auth/logout'>Выйти</a>"