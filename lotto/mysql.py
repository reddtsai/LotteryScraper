import pymysql

class mysqlDbContext:
    def __init__(self):
        # TODO(redd): config this value
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "0oibDF67wafbqNkF"
        self.db = "TaiwanLottery"
        self.charset = "utf8"

    def connect(self):
        conn = pymysql.connect(
            host = self.host, 
            user = self.user, 
            password = self.password, 
            db = self.db, 
            charset = self.charset, 
            cursorclass = pymysql.cursors.DictCursor
        )
        return conn