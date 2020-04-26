from datetime import datetime
from app import db

class GreenCoffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(128), index=True, unique=False)
    date_acquired = db.Column(db.DateTime, index=True, unique=False)
    origin_country = db.Column(db.String(60), index=True, unique=False)
    farm_information = db.Column(db.String(256), index=False, unique=False)
    official_notes = db.Column(db.String(256), index=False, unique=False)

    def __repr__(self):
        return '<{} from {}>'.format(self.origin_country, self.source)

class RoastedCoffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roaster = db.Column(db.String(128), index=True)
    roast_date = db.Column(db.DateTime, index=True)
    coffee_name = db.Column(db.String(60))
    origin_country = db.Column(db.String(60))
    farm_information = db.Column(db.String(256))
    official_notes = db.Column(db.String(256))
    roast_session = db.relationship('RoastSession', backref='roast_info', lazy='dynamic')

    def __repr__(self):
        return '<{} from {}>'.format(self.coffee_name, self.roaster)

class TastingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coffee = db.Column(db.Integer, db.ForeignKey('roastedcoffee.id'))
    prep_method = db.Column(db.String(50), index=True, unique=False)
    coffee_in = db.Column(db.Integer, index=False, unique=False)
    liquid_in = db.Column(db.Integer, index=False, unique=False)
    beverage_out = db.Column(db.Integer, index=False, unique=False)
    tasting_notes = db.Column(db.String(200), index=False, unique=False)
    coffee = db.relationship('RoastedCoffee', backref='coffee', lazy='dynamic')

class RoastSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    green_coffee = db.Column(db.Integer, db.ForeignKey('greencoffee.id'))
    green_weight = db.Column(db.Integer, index=False, unique=False)
    roasted_weight = db.Column(db.Integer, index=False, unique=False)
    roast_time = db.Column(db.Integer, index=False, unique=False)
    fc_time = db.Column(db.Integer, index=False, unique=False)
    temp_data = db.Column(db.String(256), index=False, unique=False)
    green_coffee = db.relationship('GreenCoffee', backref='greens', lazy='dynamic')
