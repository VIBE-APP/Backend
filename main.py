import dbConfig
from utils.user_manager import user_manager

from flask import Flask

from scripts.get_user_profile import get_user_profile

import mysql.connector
import sys
import boto3
import os

app = Flask(__name__)

# testing purposes
@app.route('/')
def hello_world(): 
    return "You've hit VIBE backend"

# signing up a user
@app.route('/signup')
def signup_script():
    username = '' # need to parse from frontend
    email = ''
    password = '' # need to parse from frontend
    return user_manager.signup_user(username, email, password)

# signing in user
@app.route('/signin')
def signin_script():
    username = '' # need to parse from frontend
    password = '' # need to parse from frontend
    return user_manager.signin_user(username, password)

# get using profile info - for user profile page
@app.route('/get_user_profile_info')
def get_user_profile_info():
    user_id = ''
    return get_user_profile(user_id=user_id)