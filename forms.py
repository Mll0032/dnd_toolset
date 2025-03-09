from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddWeaponForm(FlaskForm):
    name = StringField('Weapon Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Simple Melee', 'Simple Melee'), 
        ('Simple Ranged', 'Simple Ranged'),
        ('Martial Melee', 'Martial Melee'),
        ('Martial Ranged', 'Martial Ranged')
    ], validators=[DataRequired()])
    cost = StringField('Cost')
    damage = StringField('Damage')
    weight = StringField('Weight')
    properties = StringField('Properties')
    source = StringField('Source Book')
    homebrew = BooleanField('Homebrew')
    submit = SubmitField('Add Weapon')

class AddArmorForm(FlaskForm):
    name = StringField('Armor Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Light Armor', 'Light Armor'), 
        ('Medium Armor', 'Medium Armor'),
        ('Heavy Armor', 'Heavy Armor'),
        ('Shield', 'Shield')
    ], validators=[DataRequired()])
    cost = StringField('Cost')
    armor_class = StringField('Armor Class')
    strength_requirement = StringField('Strength Requirement')
    stealth_disadvantage = BooleanField('Stealth Disadvantage')
    weight = StringField('Weight')
    source = StringField('Source Book')
    homebrew = BooleanField('Homebrew')
    submit = SubmitField('Add Armor')
