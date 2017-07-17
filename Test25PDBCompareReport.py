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

    def test_parseClassification(self):
        print("in parseClassification test")
        myReport = Generate25PDBComapreReport()
        classification = myReport.parseClassification("some html", "1ABV")
        print(classification)
        self.assertFalse(not classification)

    def test_parse25PDBProteinClassification(self):
        print("in parseClassification test")
        myReport = Generate25PDBComapreReport()
        setOfProteinToClass = myReport.parse25PDBProteinClassification()
        
        print(" with set size " + str(len(setOfProteinToClass)))
        self.assertTrue(len(setOfProteinToClass)  == 1673)