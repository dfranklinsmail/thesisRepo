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
from urllib.error import HTTPError
from urllib.error import URLError
import re
from socket import timeout

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
        print("the protein " + proteinName)
        url = "http://www.rcsb.org/pdb/explore/macroMoleculeData.do?structureId="+proteinName
        #print("fetching html for url ")
        #print(url)
        
        try:
            html = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
        except (HTTPError, URLError) as error:
            print('Data for protein %s not retrieved because %s\nURL: %s', proteinName, error, url)
        except timeout:
            print('socket timed out - URL %s', url)
        
        return html

    def parseClassification(self, html, proteinName):
        """ takes html and returns classification information """
        print("looking for protein name "+proteinName)
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
        index = html.find(self.SCOP_TITLE)

        if index >= 0 :
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
        else :
            print('could not find scop string in html')
        return nameToClass

    def formatChainPostFix(self, chainName):
        if len(chainName) == 1 :
                result = ''
        elif len(chainName) > 1 :
            result = chainName[:1] + ':' + chainName[1:]
        else:
            result = chainName[:1]

        return result

    def parse25PDBProteinClassification(self, filename):
        """ loads the 25PDB.csv file and parses it returning a set of proteinNames and classifications """
        listOfProteinAndClass = list()
        f = open(os.path.join(sys.path[0], filename), 'r')
        line = f.readline()
        line = f.readline()
        while line :
            values = line.split(',')
            protein = values[3].replace('\n', '')
            listOfProteinAndClass.append((values[0], protein))
            line = f.readline()
        
        return listOfProteinAndClass


    def classificationMatches(self, scopClass, htmlClass) :
        print('matching scopClass '+scopClass+' with htmlClass '+htmlClass)
        if scopClass == 'a' and htmlClass == 'Allalphaproteins' :
            result = True
        elif scopClass == 'b' and htmlClass == 'Allbetaproteins' :
            result = True
        elif scopClass == 'c' and htmlClass == 'Alphaandbetaproteins(a/b)' :
            result = True
        elif scopClass == 'd' and htmlClass == 'Alphaandbetaproteins(a+b)' :
            result = True
        else :
            result = False
        return result

    def run(self):
        """ main app logic """
        print("in the main")
        proteinAndClasses = self.parse25PDBProteinClassification('25PDB.csv')
        for  proteinAndClass in proteinAndClasses :
            print(proteinAndClass[0])
            print(proteinAndClass[1])
            print('fetching raw html for protein '+proteinAndClass[0])
            html = self.fetchHTML(proteinAndClass[0])
            if len(html) > 0  :
                classification = self.parseClassification(html, proteinAndClass[0])
                if self.classificationMatches(proteinAndClass[1], classification) :
                    print("True")
                else :
                    print("False")
            else :
                print("could not get html for protein "+proteinAndClass[0])

if __name__ == "__main__":
    app = Generate25PDBComapreReport()
    app.run()