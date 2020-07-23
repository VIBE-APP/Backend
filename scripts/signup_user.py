import boto3
import json

# class to sign up user to DB
class signup_user:
	def __init__(self, username, password, email):
		# Encript Username and Password, check if username exsists 

		if self.user_exsists(username):
			# if user exsists, tell frontend
			return json.dumps({
				"status":"user already exsists"
				})
		else:
			pass
			# now we can sign up the user since this user does not exsist


    def check_user_exsists(self, username):
    	pass
        # we need to query the DB for this username
        # to do: SQL team needs to write query for checking for the exsistence of this username in DB
        # return true if user exsists, false otherwise