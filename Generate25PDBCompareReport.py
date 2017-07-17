"""
   This code will generate a report that calculates the accuracy of the classification 
   in the 25PDB file with that found on the protein data bank scop classification.
   
   Algorithm:
      - Loop through the 25PDB.csv file, 
           - for each line in the file get the protein and classificaiton
           - for each protein construct a url to get the html from protein databank
           - parse the html and find the classification
           - compare the classification with the one found in 25PDB
           - tabulate the results in an output to console
           - % of proteins correctly classified
"""

class Generate25PDBComapreReport:

    def fetchHTML(self, proteinName):
        """ mehtod mimics linux wget with a hard coded url and returns protein classificaiton info """
        return proteinName

    def parseClassification(self, html, proteinName):
        """ takes html and returns classification information """
        return html

    def parse25PDBProteinClassification(self):
        """ loads the 25PDB.csv file and parses it returning a set of proteinNames and classifications """
        mySet = set()
        return mySet