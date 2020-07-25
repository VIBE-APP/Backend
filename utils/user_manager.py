from utils.user_credential_table_manager import user_credential_table_manager

# this class is made to handle signing up and signing in

class user_manager:
    """Class to manage all interaction with a user. Includes accessing user information, logging in, signing up"""

    def __init__(self, endpoint, user, password, port, dbname):
        # Holds an instance of an rdsExecutor to handle all of the query execution
        self.user_cred_table_manager = user_credential_table_manager(endpoint, user, password, port, dbname)

    def __del__(self):
        del self.user_cred_table_manager

    def signup_user(self, username, email, password):
        # check if user exsists
        if self.user_cred_table_manager.contains_user(username):
            return json.dumps( { "status":"username already exists" } )

        # check if email exsists
        if self.user_cred_table_manager.contains_email(email):
            return json.dumps( { "status":"email already exists" } )

        # TODO: May need to do some error handling here to make sure that the record was actually inserted
        self.user_cred_table_manager.insert_new_user(username, email, password)

        return json.dumps( { "status":"success" } )

    def signin_user(self, username, password):
        userId = self.user_cred_table_manager.validate_login(username, password)
        # if the record does not exsist in the database
        if userId == None:
            return json.dumps( { "status":"Incorrect username or password" } )

        return json.dumps( { "status":"success", "userId":userId } )