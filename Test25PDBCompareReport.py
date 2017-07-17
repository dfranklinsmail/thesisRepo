import unittest
from Generate25PDBCompareReport import Generate25PDBComapreReport

class Test25PDBCompareReport(unittest.TestCase):

    def test_helloworld(self):
        print("new hello world")

    def test_fetchHTML(self):
        print("in fetchHML test")
        myReport = Generate25PDBComapreReport()
        html = myReport.fetchHTML("1ABV")
        print(html)
        self.assertFalse(not html)