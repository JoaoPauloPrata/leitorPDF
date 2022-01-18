from tkinter import *
from tkinter import filedialog
from ConvertToTxt import ConvertToTxt
import PyPDF2
import re
import fitz
import os
src_pdf = filedialog.askopenfilename()
conversor = ConvertToTxt(src_pdf)
conversor.create_txt_file()


arquivo = open('auxiliar.txt', 'r', encoding='utf-8')
vetArquivo = []

n = re.compile('([0-9]*,[0,9]*)')
p = re.compile('([A-Z]*\s)')
m = re.compile('([0-9]{'+ '4' + '}'  + ')' )

for i in arquivo:
    vetArquivo.append(i)
vetNumeroGuia = []
vetNomesGuias = []
vetGlosas = []
vetValoresGuias = []
vetCodGlosas = []
vetNumeroCarteira = []
aux = 0

for i in range(len(vetArquivo)):
    if(vetArquivo[i] == "Dados da Guia\n"):
        aux = i
        vetNumeroGuia.append(vetArquivo[i+5])
        while(vetArquivo[aux] != "Total da Guia\n" and vetArquivo[aux] != "Dados do Prestador\n"):
            stringMaiusculas = 0
            if(p.match(vetArquivo[aux][:-2]) and vetArquivo[aux]!= "ROSA DE SA ODONTOLOGIA\n" and  vetArquivo[aux]!= "CLINICA ODONTOLOGICA OURODONTO\n"):
                vetNomesGuias.append(vetArquivo[aux])
                vetNumeroCarteira.append(vetArquivo[aux+1])
                break
            aux += 1
        aux = i
        while(vetArquivo[aux+1] != "Dados da Guia\n"  and vetArquivo[aux] != "Caso existam guias revisadas, serão apresentadas no inicio do demonstrativo, ordenadas pelo número da guia.\n"):
            if(m.match(vetArquivo[aux][:-1]) and len(vetArquivo[aux]) == 5):
                vetCodGlosas.append(vetArquivo[aux])
                break
            aux += 1   
        aux = i
        vetValoresAux = []
       
        while(vetArquivo[aux+1] != "Dados da Guia\n" and vetArquivo[aux] != "Caso existam guias revisadas, serão apresentadas no inicio do demonstrativo, ordenadas pelo número da guia.\n" and vetArquivo[aux] != "Total do Protocolo\n"):
            if(n.match(vetArquivo[aux][:-2])):
                vetValoresAux.append(vetArquivo[aux])
            aux+= 1    
     
        if(vetValoresAux[0] != vetValoresAux[1]):
            vetValoresGuias.append(vetValoresAux[len(vetValoresAux)-4][:-1])
        else:
            vetValoresGuias.append("0,00")
arquivo2 = open('saida.txt', 'w', encoding='utf-8')
aux = 0 
arquivo.close()

for i in range(len(vetValoresGuias)):
    if(vetValoresGuias[i] != "0,00"):
        arquivo2.write(vetCodGlosas[aux])
        aux += 1
        arquivo2.write(vetNumeroGuia[i][:-5])
        arquivo2.write("\n")
        arquivo2.write(str(vetValoresGuias[i]))
        arquivo2.write("\n")
        arquivo2.write(vetNomesGuias[i])
        arquivo2.write(vetNumeroCarteira[i])
        arquivo2.write("-----------------------------------------------\n")

arquivo2.write("----------------- NUMEROS GUIAS -------------------")
arquivo2.write("\n")
for i in range(len(vetNumeroGuia)):
    arquivo2.write(vetNumeroGuia[i][:-5])
    arquivo2.write("\n")
    
arquivo2.close()
