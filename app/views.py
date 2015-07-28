from app import app

@app.route('/')
@app.route('/index')
def index():
    # Fake user
    user = {'nickname': 'Johnny'}
    return '''
    <html>
        <head>
            <title>Test Page</title>
        </head>
        <body>
            <h1>Welcome, ''' + user['nickname'] + '''!</h1>
        </body>
    </html>
    '''
