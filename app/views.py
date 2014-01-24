from flask import render_template, url_for, redirect
from app import app, models, db
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = getName()
    location = getLocation()
    #name = "Robert"
    return render_template("index.html",
        name = name, location = location)

@app.route('/history')
def history():
    name = getName()
    locationHistory = getHistory()
    return render_template("history.html",
        name = name, locationHistory = locationHistory)

def getName():
    return models.User.query.get(1).name

def getLocation():
    return models.Location.query.order_by('id desc').first()

def getHistory():
    return models.Location.query.order_by('id desc')

@app.route('/set/<location>')
def setLocation(location=None):
    newLocation = models.Location(location=location, timestamp=datetime.utcnow())
    db.session.add(newLocation)
    db.session.commit()
    return redirect(url_for('index'))

"""
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods= ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return
"""
