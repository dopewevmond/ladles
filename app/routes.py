from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title='Home'
    return render_template('index.html', title=title)