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

class MagicItem(db.Model):
    __tablename__ = 'magic_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    rarity = db.Column(db.Enum('Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary', 'Artifact', name="rarity_enum"), nullable=False)
    attunement = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))

class Gear(db.Model):
    __tablename__ = 'gear'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Numeric(10,2), nullable=False)
    weight = db.Column(db.Numeric(5,2), nullable=False)

class Tool(db.Model):
    __tablename__ = 'tools'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Numeric(10,2), nullable=False)
    weight = db.Column(db.Numeric(5,2), nullable=False)
