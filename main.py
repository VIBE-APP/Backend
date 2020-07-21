from flask import Flask
app = Flask(__name__)

# testing purposes
@app.route('/')
def hello_world():
    return 'You've hit VIBE backend'

@app.route('/signup')
def signup_script():
	pass
	return 'OK'

