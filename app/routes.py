from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import NewGreenCoffee, NewRoastedCoffee

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/new_event')
def new_event():
    return render_template('new_event.html')

@app.route('/new_tasting')
def new_tasting():
    return render_template('new_tasting.html')

@app.route('/green_coffees')
def green_coffees():
    return render_template('green_coffees.html')

@app.route('/new_green_coffee', methods=['GET','POST'])
def new_green_coffee():
    form = NewGreenCoffee()
    if form.validate_on_submit():
        flash('You succesfully added your new coffee from {}'.format(form.source.data))
        return redirect(url_for('green_coffees'))
    return render_template('new_green_coffee.html', title="New Green Coffee", form=form)

@app.route('/new_roast')
def new_roast():
    return render_template('new_roast.html')

@app.route('/new_roasted_coffee', methods=['GET','POST'])
def new_roasted_coffee():
    form = NewRoastedCoffee()
    if form.validate_on_submit():
        flash('You sucessfully added your new coffee from {}'.format(form.roaster.data))
        return redirect(url_for('roasted_coffees'))
    return render_template('new_roasted_coffee.html', title="New Roasted Coffee", form=form)


@app.route('/roasted_coffees')
def roasted_coffees():
    return render_template('roasted_coffees.html')

@app.route('/roasts')
def roasts():
    return render_template('roasts.html')

@app.route('/tastings')
def tastings():
    return render_template('tastings.html')
