import boto3
import json

# this class is made to sign in the user
class signin_user:
    def __init__(self, username, password):

        user = self.check_user_exsists(username, password)

        # if user does not exsist, tell frontend about it
        if (user == None):
            return json.dumps({
                "status":"user does not exsist"
                })

        # to do: add logic to check db for username + password combination
        # if successful, we return session token
        # if !successful

    def check_user_exsists(self, username, password):
        pass

        # we need to query the DB for this username
        # to do: SQL team needs to write query for checking for the exsistence of this username in DB
        # return NONE if user does not exsist, return username and password as an object if user exsists