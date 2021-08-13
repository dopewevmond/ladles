from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class DishCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64))
    dishes = db.relationship('Dish', backref='category')

    def __repr__(self):
        return self.name


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64))
    description = db.Column(db.String(140))
    category_id = db.Column(db.Integer, db.ForeignKey('dish_category.id'))

    def __repr__(self):
        return '<Dish {}>'.format(self.name)