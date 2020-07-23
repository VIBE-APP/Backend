import dbConfig
from scripts.userCredentialTableManager import UserCredentialTableManager

from flask import Flask

from scripts.signin_user import signin_user
from scripts.signup_user import signup_user

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
    password = '' # need to parse from frontend
    return signup_user(username, password)

# signing in user
@app.route('/signin')
def signin_script():
    username = '' # need to parse from frontend
    password = '' # need to parse from frontend
    return signin_user(username, password)

# get using profile info - for user profile page
@app.route('/get_user_profile_info')
def get_user_profile_info():
    pass

# ------------------------------------------------------------------------------------------------------------------------------------------
# temp function for ethan to test sql db connection
@app.route('/db')
def testUserDbConnection():
    # client = boto3.client('rds', region_name=dbConfig.REGION, aws_access_key_id=dbConfig.ACCESS_KEY, aws_secret_access_key=dbConfig.SECRET_ACCESS_KEY)
    # token = client.generate_db_auth_token(DBHostname=dbConfig.ENDPOINT, Port=dbConfig.PORT, DBUsername=dbConfig.USERNAME, Region=dbConfig.REGION)

    userCredTableManager = UserCredentialTableManager(dbConfig.ENDPOINT, dbConfig.USERNAME, dbConfig.PASSWORD, dbConfig.PORT, dbConfig.DBNAME)

    if userCredTableManager.containsUser("ethan"):
        return "CONTAINS"

    return "NOPE"