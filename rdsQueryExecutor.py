import mysql.connector

class RdsQueryExecutor:
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
        self.disconnect()

    def executeToRows(self, query):
        cur = self.cnx.cursor()
        cur.execute(query)
        return cur.fetchall()

    def executeToPrettyPrint(self, query):
        query_results = self.executeToRows(query)

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