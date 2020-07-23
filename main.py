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

userCredTableManager = UserCredentialTableManager(dbConfig.ENDPOINT, dbConfig.USERNAME, dbConfig.PASSWORD, dbConfig.PORT, dbConfig.DBNAME)

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

    if userCredTableManager.containsUser(username):
        return json.dumps( { "status":"username already exists" } )
    elif userCredTableManager.containsEmail(email):
        return json.dumps( { "status":"email already exists" } )

    # TODO:
    # May need to do some error handling here to make sure that the record was actually inserted
    userCredTableManager.insertNewUser(username, email, password)

    return json.dumps( { "status":"success" } )

# signing in user
@app.route('/signin')
def signin_script():
    username = '' # need to parse from frontend
    password = '' # need to parse from frontend

    userId = userCredTableManager.validateLogin(username, password)
    if userId == None:
        return json.dumps( { "status":"Incorrect username or password" } )

    return json.dumps( { "status":"success", "userId":userId } )

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
    if userCredTableManager.containsUser("ethan"):
        return "CONTAINS"

    return "NOPE"