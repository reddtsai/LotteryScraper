from test.context import lottery
import unittest

class TestLotto649(unittest.TestCase):
    def setUp(self):
        self.lottery = lottery.lotto649()
        self.yyy = 103
        self.mm = 1
        self.term = 103000001
    
    def tearDown(self):
        self.lottery = None
        self.yyy = None
        self.mm = None
        self.term = None

    def test_scrapingByTerm(self):
        result = self.lottery.scrapingByTerm(self.term)
        self.assertIsNotNone(result, "view data is none")
        self.assertDictEqual(result, {'103000001': ['11', '35', '21', '18', '37', '20', '08']})
    
    def test_scrapingByDate(self):
        result = self.lottery.scrapingByDate(self.yyy, self.mm)
        self.assertIsNotNone(result, "view data is none")
        self.assertListEqual(result["103000001"], ['11', '35', '21', '18', '37', '20', '08'])

if __name__ == '__main__':
    unittest.main()