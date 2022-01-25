import fitz

class ConvertToTxt:
    def __init__(self, src_pdf):
        self.src_pdf = src_pdf
    
    def create_txt_file(self):
        conteudo = ""
        with fitz.open(self.src_pdf) as pdf:
            for pagina in pdf:
                conteudo += pagina.get_text()

        arquivo = open('auxiliar.txt', 'w', encoding='utf-8')
        arquivo.write(conteudo)
        arquivo.close()
        