from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_has = db.Column(db.String(128))
    greens_added = db.relationship("GreenCoffee", backref="added_by", lazy="dynamic")

    def set_password(self, password):
        self.password_has = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_has, password)



    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class GreenCoffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)
    date_acquired = db.Column(db.String(10))
    origin_country = db.Column(db.String(30))
    farm_information = db.Column(db.String(140))
    official_notes = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<GreenCoffee {}, {}, {}>'.format(self.source, self.date_acquired, self.origin_country)

class RoastSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    green_coffee_id = db.Column(db.Integer, db.ForeignKey('green_coffee.id'))
    green_coffee = db.relationship("GreenCoffee", backref="roasts")
    green_weight = db.Column(db.Integer)
    roasted_weight = db.Column(db.Integer)
    roast_time = db.Column(db.Integer)
    fc_time = db.Column(db.Integer)
    roast_date = db.Column(db.String(20))
    temp_data = db.Column(db.String(140))

    def __repr__(self):
        return '<RoastSession {} roast number {}>'.format(self.green_coffee, self.id)
