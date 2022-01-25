import re

class SearchInFile:
    def __init__(self):
        
        self.vetFileContent = []
        self.file = open('auxiliar.txt', 'r', encoding='utf-8')
        self.guidesPositions = []
        for i in (self.file):
            self.vetFileContent.append(i)
        self.fileSize = len(self.vetFileContent)
        for i in range(self.fileSize):
            if(self.vetFileContent[i] == "Dados da Guia\n"):
                self.guidesPositions.append(i)
        self.file.close()
    def getGuideIds(self):
        guideNumbers = []
        for i in range(len(self.guidesPositions)):
            guideNumbers.append(self.vetFileContent[self.guidesPositions[i]+5])
        return guideNumbers
    
    def getPatientInfos(self):
        p = re.compile('([A-Z]*\s)')
        patientsNames = []
        patientsId =[]
        for i in range(len(self.guidesPositions)):
            aux = self.guidesPositions[i]
            while(self.vetFileContent[aux] != "Total da Guia\n" and self.vetFileContent[aux] != "Dados do Prestador\n"):
                if(p.match(self.vetFileContent[aux][:-2]) and self.vetFileContent[aux]!= "ROSA DE SA ODONTOLOGIA\n" and  self.vetFileContent[aux]!= "CLINICA ODONTOLOGICA OURODONTO\n"):
                    patientsNames.append(self.vetFileContent[aux])
                    patientsId.append(self.vetFileContent[aux+1])
                    break
                aux += 1
            aux = i
        return patientsNames, patientsId

    def getCodGlosas(self):
        m = re.compile('([0-9]{'+ '4' + '}'  + ')' )
        codGlosas = []
        for i in range(len(self.guidesPositions)):
            aux = self.guidesPositions[i]
            while(self.vetFileContent[aux+1] != "Dados da Guia\n"  and self.vetFileContent[aux] != "Caso existam guias revisadas, serão apresentadas no inicio do demonstrativo, ordenadas pelo número da guia.\n"):
                if(m.match(self.vetFileContent[aux][:-1]) and len(self.vetFileContent[aux]) == 5):
                    codGlosas.append(self.vetFileContent[aux])
                   
                    break
                aux += 1   
            
        return codGlosas
    
    def getGlosasValues(self):
        n = re.compile('([0-9]*,[0,9]*)')
        glosasValues = []
   
        for i in range(len(self.guidesPositions)):
            vetValuesAux = []
            aux = self.guidesPositions[i]
            while(self.vetFileContent[aux+1] != "Dados da Guia\n" and self.vetFileContent[aux] != "Caso existam guias revisadas, serão apresentadas no inicio do demonstrativo, ordenadas pelo número da guia.\n" and self.vetFileContent[aux] != "Total do Protocolo\n"):
                if(n.match(self.vetFileContent[aux][:-2])):
                    vetValuesAux.append(self.vetFileContent[aux])
                aux+= 1    
            if(vetValuesAux[0] != vetValuesAux[1]):
                glosasValues.append(vetValuesAux[len(vetValuesAux)-4][:-1])
            else:
                glosasValues.append("0,00")
        return glosasValues