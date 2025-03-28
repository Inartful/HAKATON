from flask import render_template, request, redirect, url_for, flash
from app.courses.service import get_courses, get_course_by_id, check_answers
from app.courses import courses  # Импортируем блюпринт

@courses.route("/courses")
def course_list():
    """Показ списка курсов"""
    all_courses = get_courses()
    return render_template("courses/list.html", courses=all_courses)

@courses.route("/courses/<int:course_id>")
def course_detail(course_id):
    """Показ теста по курсу"""
    course = get_course_by_id(course_id)
    if not course:
        flash("Курс не найден!", "danger")
        return redirect(url_for("courses.course_list"))
    return render_template("courses/test.html", course=course)

@courses.route("/courses/<int:course_id>/submit", methods=["POST"])
def submit_test(course_id):
    """Проверка ответов пользователя"""
    course = get_course_by_id(course_id)
    if not course:
        flash("Курс не найден!", "danger")
        return redirect(url_for("courses.course_list"))

    user_answers = request.form
    score, total = check_answers(course, user_answers)
    
    flash(f"Ваш результат: {score}/{total}", "success")
    return redirect(url_for("courses.course_list"))
