from .mysql import mysqlDbContext
from datetime import datetime

class lotto649Repo:
    def __init__(self):
        dbContext = mysqlDbContext()
        self.db = dbContext.connect()
        self._result = None

    def add(self, term, no1, no2, no3, no4, no5, no6, nos):
        sql = (
            "INSERT INTO Lotto649 "
            "(term, No1, No2, No3, No4, No5, No6, NoS, Creater, CreateDate) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        with self.db.cursor() as cursor:
            cursor.execute(
                sql, 
                (term, no1, no2, no3, no4, no5, no6, nos, "Redd", datetime.now()))
        self.db.commit()

    def first(self):
        self._clear_result()
        sql = "SELECT Term FROM TaiwanLottery.Lotto649 ORDER BY Term DESC LIMIT 1"
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            self._result  = cursor.fetchone()
        return self._result 

    def find(self, key):
        self._clear_result()
        sql = "SELECT * FROM Lotto649 WHERE Term = %s"
        with self.db.cursor() as cursor:
            cursor.execute(sql, (key))
            self._result  = cursor.fetchone()
        return self._result 

    def exists(self, p):
        self._clear_result()
        sql = "SELECT Term FROM Lotto649 WHERE Term = %s"
        with self.db.cursor() as cursor:
            cursor.execute(sql, (p))
            self._result  = cursor.fetchone()
        return self._result is None

    def _clear_result(self):
        self._result = None

    def __del__(self):
        if self.db is not None:
            self.db.close()