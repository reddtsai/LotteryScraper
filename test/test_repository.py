from test.context import repository, mysql
import pymysql
import unittest
from unittest import TestCase, mock

class TestLotto649Repo(TestCase):
    def setUp(self):
        self.patcher = mock.patch.object(repository.lotto649Repo, "__init__", return_value = None)
        self.patcher.start()
        self.repo = repository.lotto649Repo()
        self.repo.db = unittest.mock.MagicMock()
    
    def termDown(self):
        self.patcher.stop()
    
    def test_first(self):
        mock_cur = unittest.mock.MagicMock()
        mock_cur.fetchone.return_value = "first"
        self.repo.db.cursor.return_value.__enter__.return_value = mock_cur
        result = self.repo.first()
        self.assertEqual(result, "first")

    def test_find(self):
        mock_cur = unittest.mock.MagicMock()
        mock_cur.fetchone.return_value = "find"
        self.repo.db.cursor.return_value.__enter__.return_value = mock_cur
        result = self.repo.find("key")
        self.assertEqual(result, "find")
    
    def test_exists(self):
        mock_cur = unittest.mock.MagicMock()
        mock_cur.fetchone.return_value = 1
        self.repo.db.cursor.return_value.__enter__.return_value = mock_cur
        result = self.repo.exists("p")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()