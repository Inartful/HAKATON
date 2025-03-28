from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Загружаем сценарий (создадим файл позже)
with open("static/scenario.json", "r", encoding="utf-8") as f:
    SCENARIO = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", scene=SCENARIO["start"])

@app.route("/choose", methods=["POST"])
def choose():
    data = request.json
    choice = data.get("choice")
    next_scene = SCENARIO.get(choice, {"text": "Ошибка", "choices": {}})
    return jsonify(next_scene)

if __name__ == "__main__":
    app.run(debug=True)
