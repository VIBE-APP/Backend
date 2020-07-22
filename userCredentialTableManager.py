from rdsQueryExecutor import RdsQueryExecutor

class UserCredentialTableManager:
    rdsExecutor = None

    def __init__(self, endpoint, user, password, port, dbname):
        self.rdsExecutor = RdsQueryExecutor(endpoint, user, password, port, dbname)

    def __del__(self):
        self.rdsExecutor.disconnect()

    def containsUser(self, user):
        return len(self.rdsExecutor.executeToRows(f"SELECT userId FROM user_credentials WHERE username = '{user}'")) > 0

    def containsEmail(self, email):
        return len(self.rdsExecutor.executeToRows(f"SELECT userId FROM user_credentials WHERE email = '{email}'")) > 0