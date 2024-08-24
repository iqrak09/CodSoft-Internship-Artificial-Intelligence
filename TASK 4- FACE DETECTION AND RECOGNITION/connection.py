import mysql.connector
from mysql.connector import errorcode

class MySqlConnection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="PHW#84#jeor",
                database="attendance"
            )
            self.cur = self.conn.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def insert(self, sql_query, values):
        self.cur.execute(sql_query, values)
        self.conn.commit()

    def read(self, sql_query):
        self.cur.execute(sql_query)
        rows = self.cur.fetchall()
        return rows

    def create(self, sql_query):
        self.cur.execute(sql_query)
        self.conn.commit()

    def update(self, sql_query, values):
        self.cur.execute(sql_query, values)
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()

conn = MySqlConnection()
