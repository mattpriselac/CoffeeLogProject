from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/new_event')
@login_required
def new_event():
    return render_template('new_event.html')

@app.route('/new_tasting')
@login_required
def new_tasting():
    return render_template('new_tasting.html')

@app.route('/green_coffees')
@login_required
def green_coffees():
    return render_template('green_coffees.html')

@app.route('/new_green_coffee', methods=['GET','POST'])
@login_required
def new_green_coffee():
    form = NewGreenCoffee()
    if form.validate_on_submit():
        flash('You succesfully added your new coffee from {}'.format(form.source.data))
        return redirect(url_for('green_coffees'))
    return render_template('new_green_coffee.html', title="New Green Coffee", form=form)

@app.route('/new_roast')
@login_required
def new_roast():
    return render_template('new_roast.html')

@app.route('/new_roasted_coffee', methods=['GET','POST'])
@login_required
def new_roasted_coffee():
    form = NewRoastedCoffee()
    if form.validate_on_submit():
        flash('You sucessfully added your new coffee from {}'.format(form.roaster.data))
        return redirect(url_for('roasted_coffees'))
    return render_template('new_roasted_coffee.html', title="New Roasted Coffee", form=form)


@app.route('/roasted_coffees')
@login_required
def roasted_coffees():
    return render_template('roasted_coffees.html')

@app.route('/roasts')
@login_required
def roasts():
    return render_template('roasts.html')

@app.route('/tastings')
@login_required
def tastings():
    return render_template('tastings.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
