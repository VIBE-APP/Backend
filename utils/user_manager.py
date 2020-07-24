from utils.user_credential_table_manager import user_credential_table_manager

class user_manager:
    """Class to manage all interaction with a user. Includes accessing user information, logging in, signing up"""
    userCredTableManager = None

    def __init__(self, endpoint, user, password, port, dbname):
        # Holds an instance of an rdsExecutor to handle all of the query execution
        self.userCredTableManager = user_credential_table_manager(endpoint, user, password, port, dbname)

    def __del__(self):
        del self.userCredTableManager

    def signupUser(self, username, email, password):
        # check if user exsists
        if self.userCredTableManager.containsUser(username):
        return json.dumps( { "status":"username already exists" } )

        # check if email exsists
        if self.userCredTableManager.containsEmail(email):
        return json.dumps( { "status":"email already exists" } )

        # TODO: May need to do some error handling here to make sure that the record was actually inserted
        self.userCredTableManager.insertNewUser(username, email, password)

        return json.dumps( { "status":"success" } )

    def signinUser(self, username, password):
        userId = self.userCredTableManager.validateLogin(username, password)
        # if the record does not exsist in the database
        if userId == None:
            return json.dumps( { "status":"Incorrect username or password" } )

        return json.dumps( { "status":"success", "userId":userId } )