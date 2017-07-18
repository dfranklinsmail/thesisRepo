import unittest
from Generate25PDBCompareReport import Generate25PDBComapreReport

class Test25PDBCompareReport(unittest.TestCase):

    def test_helloworld(self):
        print("new hello world!!!")

    def test_fetchHTML(self):
        print("in fetchHML test")
        myReport = Generate25PDBComapreReport()
        html = myReport.fetchHTML("1ABV_")
        self.assertFalse(not html)

    def test_parseClassification(self):
        print("in parseClassification test")
        testHTML = 'Domain Annotation: SCOP Classification <small class="pull-right"><a href="http://scop.mrc-lmb.cam.ac.uk/scop/" target="_blank">SCOP Database (version: 1.75) Homepage</a></small></h4>\n\n<div class="table-responsive">\n<table class="table table-bordered">\n  <thead>\n  <tr class="externalannotation">\n    <th>Chains</th>\n    <th>Domain Info</th>\n    <th>Class</th>\n    <th>Fold</th>\n    <th>Superfamily</th>\n    <th>Family</th>\n    <th>Domain</th>\n    <th>Species</th>\n  </tr>\n  </thead>\n  <tbody>\n  \n  \n\n  \n\n  <tr class="chainA">\n    <td>A</td>\n\n    \n    <td>d1abva_</td>\n\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeQuery&amp;t=11&amp;n=46456">\n        All alpha proteins\n      </a>\n    </td>\n\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeQuery&amp;t=11&amp;n=47927">\n        ATPD N-terminal domain-like\n      </a>\n    </td>\n\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeQuery&amp;t=11&amp;n=47928">\n        N-terminal domain of the delta subunit of the F1F0- ATP synthase\n      </a>\n    </td>\n\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeQuery&amp;t=11&amp;n=47929">\n        N-terminal domain of the delta subunit of the F1F0- ATP synthase\n      </a>\n    </td>\n\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeQuery&amp;t=11&amp;n=47930">\n        N-terminal domain of the delta subunit of the F1F0- ATP synthase\n      </a>\n    </td>\n    \n    \n    <td>\n      <a class="querySearchLink" href="/pdb/search/smartSubquery.do?smartSearchSubtype=TreeEntityQuery&amp;t=1&amp;n=562">Escherichia coli [TaxId: 562]</a>\n    </td>\n    \n\n  </tr>\n  \n  \n  \n  </tbody>\n</table>\n\n</div>'
        myReport = Generate25PDBComapreReport()
        classification = myReport.parseClassification(testHTML, "1ABV")
        print(classification)
        self.assertFalse(not classification)

    def test_parse25PDBProteinClassification(self):
        print("in parseClassification test")
        myReport = Generate25PDBComapreReport()
        setOfProteinToClass = myReport.parse25PDBProteinClassification()
        
        print(" with set size " + str(len(setOfProteinToClass)))
        self.assertTrue(len(setOfProteinToClass)  == 1673)