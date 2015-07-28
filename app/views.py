from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Fake user
    user = {'nickname': 'Johnny'}
    # render template with binding to title and user
    return render_template('index.html', title='Home', user=user)