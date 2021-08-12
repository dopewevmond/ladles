from flask_login.utils import login_required
from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, ReservationForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    title='Home'
    return render_template('index.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page=url_for('admin')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    title='Admin'
    return render_template('admin.html', title=title)


@app.route('/reserve-table', methods=['GET', 'POST'])
def reserve():
    reserve_form = ReservationForm()
    if reserve_form.validate_on_submit():
        flash('Reserved table')
        return '''
            <h1>Successfully reserved table</h1>
        '''
    return render_template('reservation.html', form=reserve_form)