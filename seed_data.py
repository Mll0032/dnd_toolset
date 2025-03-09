from models import db, Weapon

def seed_database():
    longsword = Weapon(name="Longsword", category="Martial Melee", cost="15 gp", damage="1d8 slashing", weight=3, properties="Versatile (1d10)", source="Player's Handbook")
    db.session.add(longsword)
    db.session.commit()

if __name__ == '__main__':
    seed_database()
