import os
class Graphviz:
    def __init__(self, objeto, texto):
        self.objeto = objeto
        self.texto = texto

    def generarArchivo(self):
        archivo = open(self.objeto + ".dot", "w", encoding="utf-8")
        archivo.write(self.texto)
        archivo.close()
    
    def generarPNG(self):
        if os.path.isfile(self.objeto + ".png"):
            os.remove(self.objeto + ".png")
        os.system("dot -Tpng " + self.objeto + ".dot -o " + self.objeto + ".png")
        os.system(self.objeto + ".png")

    def generarPDF(self):
        if os.path.isfile(self.objeto + ".pdf"):
            os.remove(self.objeto + ".pdf")
        os.system("dot -Tpdf " + self.objeto + ".dot -o " + self.objeto + ".pdf")
        os.system(self.objeto + ".pdf")


