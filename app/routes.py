from operator import pos
from flask_login.utils import login_required
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, PostDishForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Dish, DishCategory
from werkzeug.urls import url_parse
from sqlalchemy import exc

@app.route('/')
@app.route('/index')
def index():
    title='Home'
    try:
        special = DishCategory.query.filter_by(name='specials').first().id
    except AttributeError:
        special = '#'
    return render_template('index.html', title=title, special_id=special)

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
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page=url_for('menu')
        # return redirect(next_page)
        return redirect(url_for('menu'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('menu'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    title='Admin'
    form = PostDishForm()
    if form.validate_on_submit():
        try:
            dish = Dish(name=form.name.data, image=form.image.data, description=form.description.data, category=form.category.data, price=form.price.data)
            db.session.add(dish)
            db.session.commit()
            flash('The post was made successfully')
        except exc.IntegrityError:
            db.session.rollback()
            flash('The dish could not be created. This may be because it already exists in the system')
        return redirect(url_for('menu'))

    return render_template('admin.html', title=title, form=form)


@app.route('/admin/confirm-delete/<id>')
@login_required
def confirm_delete(id):
    dish = Dish.query.filter_by(id=id).first()
    return render_template('delete.html', title='Confirm Delete', dish=dish)


@app.route('/admin/delete/<id>')
@login_required
def delete(id):
    dish = Dish.query.filter_by(id=id).first()
    if dish:
        db.session.delete(dish)
        db.session.commit()
        flash('The dish has been successfully deleted')
    posts = DishCategory.query.all()
    return render_template('category.html', title='Menu', posts=posts)


@app.route('/menu/')
def menu():
    posts = DishCategory.query.all()
    return render_template('category.html', title='Menu', posts=posts)

@app.route('/about')
def aboutus():
    return render_template('coming_soon.html', title='About', message='About Us')


@app.route('/gallery')
def gallery():
    return render_template('coming_soon.html', title='Gallery', message='Gallery')


@app.route('/menu/<id>')
def dishes(id):
    posts = list(Dish.query.filter_by(category_id=id))
    num_posts = len(posts)
    category = DishCategory.query.filter_by(id=id).first()
    return render_template('dish.html', title=category, posts=posts, number=num_posts)
