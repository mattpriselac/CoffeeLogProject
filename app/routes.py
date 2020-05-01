from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, NewGreenCoffee, NewRoastSession
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, GreenCoffee, RoastSession
from sqlalchemy import desc

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
    gcs = GreenCoffee.query.order_by(desc('id')).all()

    return render_template('green_coffees.html', gcs=gcs)

@app.route('/new_green_coffee', methods=['GET','POST'])
@login_required
def new_green_coffee():
    form = NewGreenCoffee()
    if form.validate_on_submit():
        gc = GreenCoffee(source=form.source.data, date_acquired=form.date_acquired.data, origin_country=form.origin_country.data, farm_information=form.farm_information.data, official_notes=form.official_notes.data, user_id=current_user.id)
        db.session.add(gc)
        db.session.commit()
        flash("Your new coffee has been added!")
        return redirect(url_for('green_coffees'))

    return render_template('new_green_coffee.html', title="New Green Coffee", form=form)

@app.route('/green/<id>')
@login_required
def green_profile(id):
    g = GreenCoffee.query.filter_by(id=int(id)).first_or_404()
    return render_template('green.html', g=g)


@app.route('/new_roast', methods=['GET','POST'])
@login_required
def new_roast():
    form = NewRoastSession()
    gc_list = GreenCoffee.query.order_by(desc('id')).all()
    gc_name_id_pairs = []
    for coffee in gc_list:
        source_origin = coffee.source + ", " + coffee.origin_country
        gc_name_id_pairs.append((coffee.id, source_origin))
    form.green_coffee.choices = gc_name_id_pairs

    if form.validate_on_submit():
        rs = RoastSession(green_coffee_id=form.green_coffee.data, green_weight=form.green_grams.data, roasted_weight=form.roasted_grams.data, fc_time=form.fc_time.data, roast_time=form.roast_time.data, roast_date=form.roast_date.data, temp_data=form.temp_data.data)
        db.session.add(rs)
        db.session.commit()
        flash("Your new roast session has been added!")
        return redirect(url_for('roasts'))

    return render_template('new_roast.html', title="New Roast Session", form=form)

@app.route('/roast/<id>')
@login_required
def roast_profile(id):
    r = RoastSession.query.filter_by(id=int(id)).first_or_404()
    roast_no = r.green_coffee.roasts.index(r) + 1
    w_l = str(100*round((r.green_weight-r.roasted_weight)/r.green_weight, 2))+"%"
    clean_roast_time = str(r.roast_time//60)+":"+str(r.roast_time%60)
    dev_time = str(100*round((r.roast_time-r.fc_time)/r.roast_time, 2))+"%"
    clean_fc_time = str(r.fc_time//60)+":"+str(r.fc_time%60)
    return render_template('roast.html', r=r, w_l=w_l, clean_roast_time=clean_roast_time, dev_time=dev_time, clean_fc_time=clean_fc_time, roast_no=roast_no)



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
    rs = RoastSession.query.order_by(desc('id')).all()

    return render_template('roasts.html', rs=rs)

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
