from flask import Flask, render_template, request, redirect, url_for
from models import db, Weapon, Armor
from forms import AddWeaponForm, AddArmorForm

import os

app = Flask(__name__)

# Database configuration with absolute path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "db", "dnd_items.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in production

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weapons', methods=['GET', 'POST'])
def list_weapons():
    form = AddWeaponForm()
    
    if form.validate_on_submit():
        weight_value = ''.join(c for c in form.weight.data if c.isdigit() or c == '.')
        weight = float(weight_value) if weight_value else None

        new_weapon = Weapon(
            name=form.name.data,
            category=form.category.data,
            cost=form.cost.data,
            damage=form.damage.data,
            weight=weight,
            properties=form.properties.data,
            source=form.source.data,
            homebrew=form.homebrew.data
        )
        db.session.add(new_weapon)
        db.session.commit()
        return redirect(url_for('list_weapons'))

    # Retrieve filter values from request
    category_filter = request.args.get('category', '').strip()
    source_filter = request.args.get('source', '').strip()

    print(f"Category Filter: {category_filter}, Source Filter: {source_filter}")  # Debugging output

    query = Weapon.query
    if category_filter:
        query = query.filter(Weapon.category == category_filter)
    if source_filter:
        query = query.filter(Weapon.source == source_filter)

    weapons = query.all()

    categories = [c[0] for c in db.session.query(Weapon.category).distinct().all()]
    sources = [s[0] for s in db.session.query(Weapon.source).distinct().all()]

    return render_template('weapons.html', weapons=weapons, form=form, categories=categories, sources=sources)

@app.route('/weapons/edit/<int:weapon_id>', methods=['GET', 'POST'])
def edit_weapon(weapon_id):
    weapon = Weapon.query.get_or_404(weapon_id)
    form = AddWeaponForm(obj=weapon)  # Pre-fill form with existing data

    if form.validate_on_submit():
        weapon.name = form.name.data
        weapon.category = form.category.data
        weapon.cost = form.cost.data
        weapon.damage = form.damage.data

        # Extract numerical weight
        weight_value = ''.join(c for c in form.weight.data if c.isdigit() or c == '.')
        weapon.weight = float(weight_value) if weight_value else None

        weapon.properties = form.properties.data
        weapon.source = form.source.data
        weapon.homebrew = form.homebrew.data

        db.session.commit()
        return redirect(url_for('list_weapons'))

    return render_template('edit_weapon.html', form=form, weapon=weapon)

@app.route('/armor', methods=['GET', 'POST'])
def list_armor():
    form = AddArmorForm()
    
    if form.validate_on_submit():
        weight_value = ''.join(c for c in form.weight.data if c.isdigit() or c == '.')
        weight = float(weight_value) if weight_value else None

        new_armor = Armor(
            name=form.name.data,
            category=form.category.data,
            cost=form.cost.data,
            armor_class=form.armor_class.data,
            strength_requirement=form.strength_requirement.data,
            stealth_disadvantage=form.stealth_disadvantage.data,
            weight=weight,
            source=form.source.data,
            homebrew=form.homebrew.data
        )
        db.session.add(new_armor)
        db.session.commit()
        return redirect(url_for('list_armor'))

    # Retrieve filter values from request
    category_filter = request.args.get('category', '').strip()
    source_filter = request.args.get('source', '').strip()

    print(f"Category Filter: {category_filter}, Source Filter: {source_filter}")  # Debugging output

    query = Armor.query
    if category_filter:
        query = query.filter(Armor.category == category_filter)
    if source_filter:
        query = query.filter(Armor.source == source_filter)

    armors = query.all()

    categories = [c[0] for c in db.session.query(Armor.category).distinct().all()]
    sources = [s[0] for s in db.session.query(Armor.source).distinct().all()]

    return render_template('armor.html', armors=armors, form=form, categories=categories, sources=sources)


@app.route('/armor/edit/<int:armor_id>', methods=['GET', 'POST'])
def edit_armor(armor_id):
    armor = Armor.query.get_or_404(armor_id)
    form = AddArmorForm(obj=armor)  # Pre-fill form with existing data

    if form.validate_on_submit():
        armor.name = form.name.data
        armor.category = form.category.data
        armor.cost = form.cost.data
        armor.armor_class = form.armor_class.data
        armor.strength_requirement = form.strength_requirement.data
        armor.stealth_disadvantage = form.stealth_disadvantage.data

        # Extract numerical weight
        weight_value = ''.join(c for c in form.weight.data if c.isdigit() or c == '.')
        armor.weight = float(weight_value) if weight_value else None

        armor.source = form.source.data
        armor.homebrew = form.homebrew.data

        db.session.commit()
        return redirect(url_for('list_armor'))

    return render_template('edit_armor.html', form=form, armor=armor)

    # Filtering logic
    category_filter = request.args.get('category', '')
    source_filter = request.args.get('source', '')

    query = Armor.query
    if category_filter:
        query = query.filter(Armor.category == category_filter)
    if source_filter:
        query = query.filter(Armor.source == source_filter)

    armors = query.all()

    # Get distinct categories and sources for dropdowns
    categories = db.session.query(Armor.category).distinct().all()
    sources = db.session.query(Armor.source).distinct().all()

    return render_template('armor.html', armors=armors, form=form, categories=categories, sources=sources)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
