import mysql.connector

class RdsQueryExecutor:
    """Helper class to manage access to the the-stronghold database"""
    cnx = None
    endpoint = None
    user = None
    password = None
    port = None
    dbname = None

    def __init__(self, endpoint, user, password, port, dbname):
        self.endpoint = endpoint
        self.user = user
        self.password = password
        self.port = port
        self.dbname = dbname

        self.connect()

    def __del__(self):
        self.disconnect()   # Must disconnect before you go out of scope to drop the connection

    def execute(self, query, data):
        if (self.cnx.is_connected() == False):
            self.connect()

        cur = self.cnx.cursor()
        cur.execute(query, data)

    def executeToRows(self, query, data):
        """Executes any given query and returns the row output"""
        if (self.cnx.is_connected() == False):
            self.connect()
            
        cur = self.cnx.cursor()
        cur.execute(query, data)
        return cur.fetchall()

    def executeToPrettyPrint(self, query, data):
        """Executes any given query and returns a pretty printable version of the row response"""
        query_results = self.executeToRows(query, data)

        outString = ""
        for r in query_results:
            for i in range(len(r)):
                outString += str(r[i])

                if (i != len(r) - 1):
                    outString += ', '
            outString += '\n'

        return outString
    
    def connect(self):
        self.disconnect()
        self.cnx = mysql.connector.connect(host=self.endpoint, user=self.user, passwd=self.password, port=self.port, database=self.dbname)

    def disconnect(self):
        if (self.cnx != None and self.cnx.is_connected() == False):
            self.cnx.close()