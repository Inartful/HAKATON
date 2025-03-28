from app.models import db

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

class ScenarioStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scenario_id = db.Column(db.Integer, db.ForeignKey("scenario.id"), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON, nullable=False)  # [{'text': 'Выбор 1', 'next': 2}, ...]

    scenario = db.relationship("Scenario", backref=db.backref("steps", lazy=True))
