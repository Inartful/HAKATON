from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import db, User
from app import bcrypt
import os

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")

        if User.query.filter_by(username=username).first():
            flash("Имя пользователя уже занято!", "danger")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Регистрация успешна!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            flash("Вы вошли!", "success")
            return redirect(url_for("main.profile"))

        flash("Неверный логин или пароль!", "danger")

    print("Текущий путь:", os.getcwd())  # Посмотрим, откуда Flask ищет файлы
    print("Список файлов в templates:", os.listdir("templates"))  # Что есть в папке
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли!", "success")
    return redirect(url_for("auth.login"))
