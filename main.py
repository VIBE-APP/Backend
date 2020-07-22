from flask import Flask
app = Flask(__name__)

# testing purposes
@app.route('/')
def hello_world(): 
    return "You've hit VIBE backend"

# signing up a user
@app.route('/signup')
def signup_script():
    pass

# signing in user
@app.route('/signin')
def signin_script():
    pass

# get using profile info - for user profile page
@app.route('/get_user_profile_info')
def get_user_profile_info():
    pass