from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.auth.service import register_user, authenticate_user

from app.auth import auth  # Импортируем блюпринт

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        success, message = register_user(request.form["username"], request.form["password"])
        flash(message, "success" if success else "danger")
        return redirect(url_for("auth.login") if success else url_for("auth.register"))
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user, message = authenticate_user(request.form["username"], request.form["password"])
        if user:
            login_user(user)
            flash("Вы вошли!", "success")
            return redirect(url_for("main.profile"))
        flash(message, "danger")
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли!", "success")
    return redirect(url_for("auth.login"))
