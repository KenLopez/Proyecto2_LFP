from Produccion import Produccion
class GramaticaLC:
    def __init__(self, nombre = "", noTerminales = [], terminales = [], inicial = "", producciones = []):
        self.nombre = nombre
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.inicial = inicial
        self.producciones = producciones

    def validar(self):
        if(self.nombre == "" or self.nombre == " "):
            return False
        for noTerminal in self.noTerminales:
            validados = []
            if(noTerminal == self.nombre):
                return False
            elif(self.inList(noTerminal, validados)):
                return False
            else:
                validados.append(noTerminal)
        for terminal in self.terminales:
            validados = []
            if(terminal == self.nombre):
                return False
            elif(self.inList(terminal, self.noTerminales)):
                return False
            elif(self.inList(terminal, validados)):
                return False
            else:
                validados.append(terminal)
        if(not self.inList(self.inicial, self.noTerminales)):
            return False
        if(len(self.producciones) == 0):
            return False
        for produccion in self.producciones:
            fin = False
            if(not self.inList(produccion.noTerminal, self.noTerminales)):
                return False
            if(len(produccion.expresion) == 0):
                return False
            elif(len(produccion.expresion) == 1):
                if(self.inList(produccion.expresion[0], self.terminales) or produccion.expresion[0] == "$"):
                    fin = True
            for elemento in produccion.expresion:
                if(not self.inList(elemento, self.noTerminales) and not self.inList(elemento, self.terminales)):
                    return False;
        if(not fin):
            return False
        return True

    def validarLC(self):
        produccionLC = 0
        for produccion in self.producciones:
            countNoTerminal = 0
            if(len(produccion.expresion) == 1):
                if(self.inList(produccion.expresion[0],self.noTerminales)):
                   produccionLC += 1
            else:
                for elemento in produccion.expresion:
                    if(self.inList(elemento, self.noTerminales)):
                        countNoTerminal += 1
            if(len(produccion.expresion)>2 and countNoTerminal > 0):
                produccionLC += 1
            elif(len(produccion.expresion) == 2 and countNoTerminal > 1):
                produccionLC += 1
        if(produccionLC > 0):
            return True
        else:
            return False
            
    def inList(self, input, lista):
        for elemento in lista:
            if(elemento == input):
                return True
        return False

    def toString(self):
        string = "\n"
        string += "Nombre: " + self.nombre + "\nNo terminales: " + self.listaToString(self.noTerminales) + "\nTerminales: " + self.listaToString(self.terminales) + "\nNo terminal inicial: " + self.inicial + "\nProducciones:\n" + self.produccionesToString()
        return string

    def produccionesToString(self):
        string = ""
        for noTerminal in self.noTerminales:
            prod = ""
            for produccion in self.producciones:
                if(produccion.noTerminal == noTerminal):
                    if(prod == ""):
                        prod += produccion.toString() + "\n"
                    else:
                        espacio = ""
                        for i in range(0,len(produccion.noTerminal)+1):
                            espacio += " "
                        prod += espacio + "| " + produccion.expToString() + "\n"
            string += prod
        return string


    def listaToString(self, lista):
        string = ""
        for i in range(0,len(lista)):
            string = string + lista[i]
            if(i<len(lista)-1):
                string = string + ","
        return string

