from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug.debug import get_current_traceback
from flask.ext.bcrypt import Bcrypt
from flask.ext.csrf import csrf
from flask.ext.sqlalchemy import SQLAlchemy
import logging
import os

app = Flask(__name__)
app.config.from_object('settings.Config')
bcrypt = Bcrypt(app)
csrf(app)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    roles = AssessmentRoles.query.all()
    return render_template('index.html', roles=roles)

@app.route('/record/<id>/')
def record(id):
    post = Post.objects.get(id=id)
    return render_template('record.html', p=post)

@app.route('/users/')
def users():
    users = User.objects.all()
    return render_template('users.html', u=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    error = None
    if request.method == 'POST':
        try:
            this_user = User.objects.get(email=request.form['username'])
            if request.form['username'] != this_user.email:
                error = 'Invalid username'
            elif bcrypt.check_password_hash(this_user.password, request.form['password']) == False:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                session['this_user'] = {'first_name':this_user.first_name}

                flash('You were logged in')
                return redirect(url_for('index'))
        except:
            flash('User does not exist')
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

if __name__ == '__main__':
    #app.debug = app.config['DEBUG']
    app.run(host = '127.0.0.1', port = 5000)
