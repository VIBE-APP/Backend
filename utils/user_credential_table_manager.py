from RDS_query_executor import RDS_query_executor

class user_credential_table_manager:
    """Helper class to manage access to user_credential table in the-stronghold"""
    rdsExecutor = None

    def __init__(self, endpoint, user, password, port, dbname):
        # Holds an instance of an rdsExecutor to handle all of the query execution
        self.rdsExecutor = RDS_query_executor(endpoint, user, password, port, dbname)

    def __del__(self):
        self.rdsExecutor.disconnect()   # Must disconnect before you go out of scope to drop the connection

    def containsUser(self, username):
        return len(self.rdsExecutor.execute(f"SELECT userId FROM user_credentials WHERE username = %s", (username,))) > 0

    def containsEmail(self, email):
        return len(self.rdsExecutor.execute(f"SELECT userId FROM user_credentials WHERE email = %s", (email,))) > 0

    def insertNewUser(self, username, email, password):
        self.rdsExecutor.execute(f"INSERT INTO user_credentials(username, email, password) VALUES (%s, %s, %s)", (username, email, password))

    def updateUserPasswordByUsername(self, username, password):
        self.rdsExecutor.execute(f"UPDATE user_credentials SET password = %s WHERE username = %s", (password, username))

    def updateUserPasswordByEmail(self, email, password):
        self.rdsExecutor.execute(f"UPDATE user_credentials SET password = %s WHERE email = %s", (password, email))

    def findUserIdByUsername(self, username):
        # TODO:
        # Return None when no entries exist
        return self.rdsExecutor.execute(f"SELECT userId from user_credentials WHERE username = %s", (username,))[0][0]

    def findUserIdByEmail(self, email):
        # TODO:
        # Return None when no entries exist
        return self.rdsExecutor.execute(f"SELECT userId from user_credentials WHERE email = %s", (email,))[0][0]

    def validateLogin(self, username, password):
        # TODO:
        # Return None when no entries exist
        return self.rdsExecutor.execute(f"SELECT userId FROM user_credentials WHERE username = %s and password = %s", (username, password))[0][0]