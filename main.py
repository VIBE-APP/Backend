import dbConfig

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
	try:
		conn =  mysql.connector.connect(host=dbConfig.ENDPOINT, user=dbConfig.USERNAME, passwd=dbConfig.PASSWORD, port=dbConfig.PORT, database=dbConfig.DBNAME)
		cur = conn.cursor()
		cur.execute("""SELECT * FROM user_credentials""")
		query_results = cur.fetchall()
		print(query_results)
		
		outString = ""
		for r in query_results:
			for i in range(len(r)):
				outString += str(r[i])

				if (i != len(r) - 1):
					outString += ', '
			outString += '\n'

		return outString
	except Exception as e:
		print("Database connection failed due to {}".format(e))
		return "Error"

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