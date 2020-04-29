@app.route('/new_green_coffee', methods=['GET','POST'])
@login_required
def new_green_coffee():
    form = NewGreenCoffee()
    if form.validate_on_submit():
        gc = GreenCoffee(source=form.source.data, date_acquired=form.date_acquired.data, origin_country=form.origin_country.data, farm_information=form.farm_information.data, official_notes=form.official_notes.data, user_id=current_user.id)
        db.add(gc)
        db.commit()
        flash("Your new coffee has been added!")
        return redirect(url_for('green_coffees'))

    return render_template('new_green_coffee.html', title="New Green Coffee", form=form)

    class NewGreenCoffee(FlaskForm):
        source = StringField('Source', validators=[DataRequired()])
        date_acquired = DateField('Date Acquired', validators=[DataRequired()])
        official_notes = StringField("Supplier's Tasting Notes")
        origin_country = StringField('Country of Origin', validators=[DataRequired()])
        farm_information = TextAreaField('Regional or Farm information')
        submit = SubmitField('Submit your new Green Coffee')

    class GreenCoffee(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        source = db.Column(db.String)
        date_acquired = db.Column(db.String(10))
        origin_country = db.Column(db.String(30))
        farm_information = db.Column(db.String(140))
        official_notes = db.Column(db.String(140))
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



@app.route('/green_coffees')
@login_required
def green_coffees():
    gcs = GreenCoffee.query.order_by.(desc('id')).all()

    return render_template('green_coffees.html')
