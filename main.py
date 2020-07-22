import dbConfig
from userCredentialTableManager import UserCredentialTableManager

from flask import Flask

import mysql.connector
import sys
import boto3
import os

app = Flask(__name__)

# testing purposes
@app.route('/')
def hello_world(): 
    return "You've hit VIBE backend"

@app.route('/db')
def testUserDbConnection():
	# client = boto3.client('rds', region_name=dbConfig.REGION, aws_access_key_id=dbConfig.ACCESS_KEY, aws_secret_access_key=dbConfig.SECRET_ACCESS_KEY)
	# token = client.generate_db_auth_token(DBHostname=dbConfig.ENDPOINT, Port=dbConfig.PORT, DBUsername=dbConfig.USERNAME, Region=dbConfig.REGION)
	
	userCredTableManager = UserCredentialTableManager(dbConfig.ENDPOINT, dbConfig.USERNAME, dbConfig.PASSWORD, dbConfig.PORT, dbConfig.DBNAME)

	if userCredTableManager.containsUser("ethan"):
		return "CONTAINS"
	
	return "NOPE"

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