from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.String(50))
    damage = db.Column(db.String(50))
    weight = db.Column(db.Float)
    properties = db.Column(db.String(200))
    source = db.Column(db.String(100))
    homebrew = db.Column(db.Boolean, default=False)

class Armor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.String(50))
    armor_class = db.Column(db.String(50))
    strength_requirement = db.Column(db.String(50))
    stealth_disadvantage = db.Column(db.Boolean, default=False)
    weight = db.Column(db.Float)
    source = db.Column(db.String(100))
    homebrew = db.Column(db.Boolean, default=False)
