import boto3
import json

# this class is made to sign in the user
class signin_user:
    
    def __init__(self, username, password):
        # setup
        self.userCredTableManager = UserCredentialTableManager(dbConfig.ENDPOINT, dbConfig.USERNAME, dbConfig.PASSWORD, dbConfig.PORT, dbConfig.DBNAME)
        
        self.run(username, password)

    def run(self, username, password):

        userId = self.userCredTableManager.validateLogin(username, password)
        # if the record does not exsist in the database
        if userId == None:
            return json.dumps( { "status":"Incorrect username or password" } )

        return json.dumps( { "status":"success", "userId":userId } )