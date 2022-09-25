import pymysql
import os
import pandas as pd

class coinDB():
    def __init__(self, host, exchange='upbit'):
        self.db = pymysql.connect(host=host,
                                  port=3306,
                                  user='root',
                                  password=os.environ['MYSQL_PASSWORD'],
                                  db=exchange,
                                  charset='utf8',
                                  autocommit=True,
                                  cursorclass=pymysql.cursors.DictCursor)
            
        self.cursor = self.db.cursor()
        
    def execute(self, query):
        self.cursor.execute(query)
        return pd.DataFrame(self.cursor.fetchall())

    def rollback(self):
        self.db.rollback()
    
    def close(self):
        self.db.close()

if __name__ == '__main__':
    host = '52.79.239.69'
    upbitDB = coinDB(host)
    query = """SHOW DATABASES;"""
    result = upbitDB.execute(query)
    print(result)
    upbitDB.close()


