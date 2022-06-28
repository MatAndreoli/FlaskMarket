from flask import render_template

from src import app


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/test')
def t():
    return {
        'name': 'andreoli', 'age': 18, 'zero': 0,
        'address': {
            'city': 'SomeCity',
            'state': 'SP'
        }
    }
