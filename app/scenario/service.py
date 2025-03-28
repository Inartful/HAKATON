from app.scenario.models import ScenarioStep
from app.models import db, UserProgress

def get_first_step(scenario_id, user_id):
    first_step = ScenarioStep.query.filter_by(scenario_id=scenario_id, step_number=1).first()
    if not first_step:
        return None, "Сценарий не найден"

    # Проверяем, есть ли у пользователя сохраненный прогресс
    progress = UserProgress.query.filter_by(user_id=user_id, scenario_id=scenario_id).first()
    if not progress:
        progress = UserProgress(user_id=user_id, scenario_id=scenario_id, current_step=first_step.id)
        db.session.add(progress)
        db.session.commit()

    return first_step, None

def process_answer(scenario_id, user_id, step_id, selected_option):
    current_step = ScenarioStep.query.get(step_id)
    if not current_step:
        return None, "Шаг не найден"

    next_step_id = None
    for option in current_step.options:
        if option["text"] == selected_option:
            next_step_id = option["next"]
            break

    if not next_step_id:
        return None, "Неверный ответ"

    next_step = ScenarioStep.query.get(next_step_id)
    
    # Обновляем прогресс
    progress = UserProgress.query.filter_by(user_id=user_id, scenario_id=scenario_id).first()
    progress.current_step = next_step.id if next_step else None
    db.session.commit()

    return next_step, None
