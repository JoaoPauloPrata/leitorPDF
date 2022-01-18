from tkinter import *
from tkinter import filedialog
from ConvertToTxt import ConvertToTxt
from SearchInFile import SearchInFile
import PyPDF2
import re
import fitz
import os
src_pdf = filedialog.askopenfilename()
conversor = ConvertToTxt(src_pdf)
conversor.create_txt_file()

vetArquivo = []


searcher = SearchInFile()

vetNumeroGuia = searcher.getGuideIds()
vetNomesGuias, vetNumeroCarteira = searcher.getPatientInfos()
vetValoresGuias = searcher.getGlosasValues()
vetCodGlosas = searcher.getCodGlosas()


aux = 0

arquivo2 = open('saida.txt', 'w', encoding='utf-8')
aux = 0 


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
