from rdsQueryExecutor import RdsQueryExecutor

class UserCredentialTableManager:
    rdsExecutor = None

    def __init__(self, endpoint, user, password, port, dbname):
        self.rdsExecutor = RdsQueryExecutor(endpoint, user, password, port, dbname)

    def __del__(self):
        self.rdsExecutor.disconnect()

    def containsUser(self, username):
        return len(self.rdsExecutor.executeToRows(f"SELECT userId FROM user_credentials WHERE username = '{username}'")) > 0

    def containsEmail(self, email):
        return len(self.rdsExecutor.executeToRows(f"SELECT userId FROM user_credentials WHERE email = '{email}'")) > 0

    def insertNewUser(self, username, email, password):
        self.rdsExecutor.execute(f"INSERT INTO user_credentials(username, email, password) VALUES ('{username}', '{email}', '{password}')")

    def updateUserPasswordByUsername(self, username, password):
        self.rdsExecutor.execute(f"UPDATE user_credentials SET password = '{password}' WHERE username = '{username}'")

    def updateUserPasswordByEmail(self, email, password):
        self.rdsExecutor.execute(f"UPDATE user_credentials SET password = '{password}' WHERE email = '{email}'")

    def findUserIdByUsername(self, username):
        return self.rdsExecutor.executeToRows(f"SELECT userId from user_credentials WHERE username = '{username}'")[0][0]

    def findUserIdByEmail(self, email):
        return self.rdsExecutor.executeToRows(f"SELECT userId from user_credentials WHERE email = '{email}'")[0][0]