from flask import jsonify, request
from flask_login import login_required, current_user
from app.scenario import scenario_bp
from app.scenario.service import get_first_step, process_answer

@scenario_bp.route("/scenario/<int:scenario_id>/start", methods=["GET"])
@login_required
def start_scenario(scenario_id):
    step, error = get_first_step(scenario_id, current_user.id)
    if error:
        return jsonify({"error": error}), 404

    return jsonify({"step_id": step.id, "text": step.text, "options": step.options})

@scenario_bp.route("/scenario/<int:scenario_id>/step/<int:step_id>", methods=["POST"])
@login_required
def next_step(scenario_id, step_id):
    data = request.get_json()
    selected_option = data.get("option")

    step, error = process_answer(scenario_id, current_user.id, step_id, selected_option)
    if error:
        return jsonify({"error": error}), 400

    if step:
        return jsonify({"step_id": step.id, "text": step.text, "options": step.options})
    return jsonify({"message": "Тест завершен"})
