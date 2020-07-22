import dbConfig

from flask import Flask
import pymysql

app = Flask(__name__)

# testing purposes
@app.route('/')
<<<<<<< HEAD
def hello_world(): 
    return "You've hit VIBE backend"
=======
def hello_world():
    return 'You\'ve hit VIBE backend'

@app.route('/db')
def testUserDbConnection():
	result = []
	conn = pymysql.connect(dbConfig.ENDPOINT, user=dbConfig.USERNAME, passwd=dbConfig.PASSWORD, db=dbConfig.DBNAME, connect_timeout=5)
	with conn.cursor() as cur:
		cur.execute("""select * from user_credentials""")
		conn.commit()
		cur.close()
		for row in cur:
			result.append(list(row))
		print("Data from RDS...")
		print(result)

	outString = ""
	for r in result:
		for i in range(len(r)):
			outString += str(r[i])

			if (i != len(r) - 1):
				outString += ', '
		outString += '\n'

	return outString
>>>>>>> 90fa5ea3f0a925b274ca34e64be50fadbed22063

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