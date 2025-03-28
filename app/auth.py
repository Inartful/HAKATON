from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import db, User
from app import bcrypt

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        # Проверяем длину пароля
        if len(password) < 6:
            flash("Пароль должен быть минимум 6 символов!", "danger")
            return redirect(url_for("auth.register"))

        # Проверяем, существует ли пользователь (игнорируем регистр)
        existing_user = User.query.filter(User.username.ilike(username)).first()
        if existing_user:
            flash("Имя пользователя уже занято!", "danger")
            return redirect(url_for("auth.register"))

        # Хешируем пароль и создаем пользователя
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Автоматически входим после регистрации
        login_user(new_user)
        flash("Регистрация успешна!", "success")
        return redirect(url_for("main.profile"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        user = User.query.filter(User.username.ilike(username)).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)

            # Если пользователь попал на логин со страницы, требующей входа
            next_page = request.args.get("next")
            flash("Вы вошли!", "success")
            return redirect(next_page) if next_page else redirect(url_for("main.profile"))

        flash("Неверный логин или пароль!", "danger")

    return render_template("login.html") 

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли!", "success")
    return redirect(url_for("auth.login"))
