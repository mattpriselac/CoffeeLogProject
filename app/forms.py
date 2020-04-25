from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class NewRoastedCoffee(FlaskForm):
    roaster = StringField('Roaster', validators=[DataRequired()])
    roast_date = DateField('Roast Date', validators=[DataRequired()])
    coffee_name = StringField('Name of Coffee')
    origin_country = StringField('Origin')
    official_notes = StringField("Roaster's Tasting Notes")
    farm_information = TextAreaField('Regional or Farm information')
    submit = SubmitField('Submit your new Roasted Coffee')

class NewGreenCoffee(FlaskForm):
    source = StringField('Source', validators=[DataRequired()])
    date_acquired = DateField('Date Acquired', validators=[DataRequired()])
    tasting_notes = StringField("Supplier's Tasting Notes")
    origin_country = StringField('Country of Origin', validators=[DataRequired()])
    farm_information = TextAreaField('Regional or Farm information')
    submit = SubmitField('Submit your new Green Coffee')

class NewTastingSession(FlaskForm):
    taster = StringField('Participant', validators=[DataRequired()])
    coffee = StringField('Roasted Coffee', validators=[DataRequired()])
    tasting_date = DateField('Date of Tasting', validators=[DataRequired()])
    prep_method = StringField('Method of Preparation', validators=[DataRequired()])
    coffee_in = IntegerField('Coffee in (grams)', validators=[DataRequired()])
    liquid_in = IntegerField('Water added (for non-espresso methods)')
    beverage_out = IntegerField('Beverage weight out (for espresso)')
    tasting_notes = StringField('Tasting Notes', validators=[DataRequired()])
    submit = SubmitField('Submit your new Tasting Session')

#class NewRoastSession(FlaskForm):
#i need a selection method here to require a green coffee in.