import boto3
import json
from utils.user_credential_table_manager import user_credential_table_manager

# class to sign up user to DB
class signup_user:

    def __init__(self, username, password, email):
        # setup
        self.userCredTableManager = user_credential_table_manager(dbConfig.ENDPOINT, dbConfig.USERNAME, dbConfig.PASSWORD, dbConfig.PORT, dbConfig.DBNAME)

        self.run(username, password, email)

    def run(self, username, password, email):
        # check if user exsists
        if self.userCredTableManager.containsUser(username):
            return json.dumps( { "status":"username already exists" } )

        # check if email exsists
        if self.userCredTableManager.containsEmail(email):
            return json.dumps( { "status":"email already exists" } )

        # TODO: May need to do some error handling here to make sure that the record was actually inserted
        self.userCredTableManager.insertNewUser(username, email, password)

        return json.dumps( { "status":"success" } )