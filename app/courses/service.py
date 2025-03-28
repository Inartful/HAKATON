COURSES = {
    1: {
        "id": 1,
        "title": "Основы безопасности",
        "questions": [
            {"id": 1, "question": "Что делать при пожаре?", "options": ["Бежать", "Звонить 112", "Прятаться"], "answer": 1},
            {"id": 2, "question": "Как пользоваться огнетушителем?", "options": ["Нажать кнопку", "Выдернуть чеку, направить, нажать"], "answer": 1}
        ]
    },
    2: {
        "id": 2,
        "title": "Первая помощь",
        "questions": [
            {"id": 1, "question": "Как проверить дыхание?", "options": ["Посмотреть на грудь", "Приложить ухо к носу", "Ощупать шею"], "answer": 1}
        ]
    }
}

def get_courses():
    """Возвращает список всех курсов"""
    return list(COURSES.values())

def get_course_by_id(course_id):
    """Возвращает курс по ID"""
    return COURSES.get(course_id)

def check_answers(course, user_answers):
    """Проверяет ответы пользователя"""
    score = 0
    total = len(course["questions"])
    
    for question in course["questions"]:
        q_id = str(question["id"])  # Flask передает form как str
        if q_id in user_answers and int(user_answers[q_id]) == question["answer"]:
            score += 1
    
    return score, total
