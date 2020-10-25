class Transicion:
    def __init__(self, inicial="", leido="", extraido="", destino="", insertado=""):
        self.inicial = inicial
        self.leido = leido
        self.extraido = extraido
        self.destino = destino
        self.insertado = insertado

    def toStringGraph(self):
        string = self.leido + "," + self.extraido + ";" + self.insertado
        return string

    def toJointString(self):
        string = self.inicial + self.leido + self.extraido + self.destino + self.insertado
        return string
    
    def toString(self):
        string = self.inicial + "," + self.leido + "," + self.extraido + ";" + self.extraido + "," + self.destino
        return string
