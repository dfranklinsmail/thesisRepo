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
import os
import sys
import urllib.request
import re

class Generate25PDBComapreReport:
    SCOP_TITLE = "Domain Annotation: SCOP Classification"
    SCOP_Class_A = "All alpha proteins"
    SCOP_Class_B = "All beta proteins"
    SCOP_Class_AorB = "Alpha and beta proteins (a/b)"
    SCOP_Class_AandB = "Alpha and beta proteins (a+b)"

    def fetchHTML(self, proteinName):
        """ mehtod mimics linux wget with a hard coded url 
        and returns protein classificaiton info """
        
        if (len(proteinName) > 4):
            proteinName = proteinName[: (4 - len(proteinName))]
        
        #print("the length of protein " + str(len(proteinName)))
        #print("the protein" + proteinName)
        url = "http://www.rcsb.org/pdb/explore/macroMoleculeData.do?structureId="+proteinName
        #print("fetching html for url ")
        #print(url)
        
        response = urllib.request.urlopen(url)
        html = response.read()
        
        return html

    def parseClassification(self, html, proteinName):
        """ takes html and returns classification information """
        classification = ''
        nameToClass = self.parseProteinAndClass(html, proteinName)
        print(nameToClass)
        if proteinName in nameToClass:
            classification = nameToClass[proteinName]
        
        return classification

    def parseProteinAndClass(self, html, proteinName):
        """ """
        nameToClass = {}
        tableStartTag = "<tbody>"
        tableEndTag = "</tbody>"
        index = html.index(self.SCOP_TITLE)

        if (index >= 0):
            start = html.index(tableStartTag, index+ len(self.SCOP_TITLE))
            end = html.index(tableEndTag, start+ len(tableStartTag))
        
            html = html[start + len(tableStartTag) :end - len(tableEndTag)]
            html = html.replace(' ', '')
            html = html.replace('\n', '')
            trs = html.split("<tr")

            for row in trs :
                if (len(row) > 0) :
                    tdData = re.findall(r'<td.*?>(.*?)<\/td>', row)
                    chainPostFix = self.formatChainPostFix(tdData[0])
                    classification = re.findall(r'<a.*?>(.*?)<\/a>', tdData[2])[0]
                    nameToClass[proteinName+chainPostFix] = classification

        return nameToClass

    def formatChainPostFix(self, chainName):
        if (len(chainName) > 1) :
            chainName = chainName[0:1] + ':' + chainName[1:]

        return chainName

    def parse25PDBProteinClassification(self):
        """ loads the 25PDB.csv file and parses it returning a set of proteinNames and classifications """
        listOfProteinAndClass = list()
        f = open(os.path.join(sys.path[0], '25PDB.csv'), 'r')
        line = f.readline()
        line = f.readline()
        while line :
            values = line.split(',')
            listOfProteinAndClass.append((values[0], values[3]))
            line = f.readline()
        
        return listOfProteinAndClass

    def run(self):
        """ main app logic """


if __name__ == "__main__":
    app = Generate25PDBComapreReport()
    app.run()