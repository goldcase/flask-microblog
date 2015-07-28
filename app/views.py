from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Mock user
    user = {'nickname': 'Johnny'}
    # Mock posts
    posts = [
    	{
    		'author': {'nickname': 'Babel'},
    		'body': 'Working at kCura'
    	},
    	{
    		'author': {'nickname': 'Dave'},
    		'body': 'Jim Cramer is Wrong'
    	}
    ]
    # Render template with binding to title and user
    return render_template('index.html', 
    						title='Home', 
    						user=user,
    						posts=posts)