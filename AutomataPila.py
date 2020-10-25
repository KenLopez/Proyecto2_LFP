from Transicion import Transicion
from Graphviz import Graphviz
class AutomataPila:
    def __init__(self, nombre = "", estados = [], alfabeto = [], simbolosPila = [], inicial = "", aceptacion = [], transiciones = []):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.simbolosPila = simbolosPila
        self.inicial = inicial
        self.aceptacion = aceptacion
        self.transiciones = transiciones
        self.pila = []
    
    def toPDF(self):
        string = "digraph " + self.nombre + "{\n" + "rankdir=LR\n" + self.toGraphviz()
        grafo = Graphviz(self.nombre, string)
        grafo.generarArchivo()
        grafo.generarPDF()

    def toGraphviz(self):
        string = ""
        string += str(self.generateNodes())
        string += str(self.joinNodes())
        string += str(self.tablaResumen())
        return string

    def tablaResumen(self):
        string = ""
        string += "tabla[shape=plaintext, fontsize=10, label=<\n"
        string += "  <TABLE BORDER=\"0\">\n"
        string += "      <TR><TD>Nombre: </TD><TD>" + self.nombre + "</TD></TR>\n"
        string += "      <TR><TD>Alfabeto: </TD><TD>" + str(self.listaToString(self.alfabeto)) + "</TD></TR>\n"
        string += "      <TR><TD>Alfabeto de pila: </TD><TD>" + str(self.listaToString(self.simbolosPila)) + "</TD></TR>\n"
        string += "      <TR><TD>Estados: </TD><TD>" + str(self.listaToString(self.estados)) + "</TD></TR>\n"
        string += "      <TR><TD>Estado Inicial: </TD><TD>" + self.inicial + "</TD></TR>\n"
        string += "      <TR><TD>Estados de Aceptación: </TD><TD>" + str(self.listaToString(self.aceptacion)) + "</TD></TR>\n"
        string += "  </TABLE>\n>]\n}"
        return string

    def listaToString(self, lista):
        string = ""
        for i in range(0,len(lista)):
            string = string + lista[i]
            if(i<len(lista)-1):
                string = string + ","
        return string

    def joinNodes(self):
        string = "Inicio->" + self.inicial + "\n"
        counter = 0
        group = []
        usadas = []
        for estado in self.estados:
            grupo = False
            group = []
            for item in self.transiciones:
                if(item.inicial == item.destino and item.inicial == estado):
                    grupo = True
                    group.append(item)
                    usadas.append(item) 
            label = ""
            if(grupo):
                label += "<"
                for item in group:
                    label += "<font>" + item.toStringGraph() + "</font><br/>"
                label += ">"
                string += "T" + str(counter) + "[shape=none label=" + label + "]\n"
                string += "T" + str(counter) + "->" + estado + "\n"
                string += estado + "->" + "T" + str(counter) + "[dir=none]\n"
                string += "{rank=same; " + "T" + str(counter) + ", " + estado + "}\n"
                counter += 1
        for item in self.transiciones:
            if(not self.inList(item, usadas)):
                string += item.inicial + "->" + item.destino + "[label=\"" + item.toStringGraph() + "\"]\n"
        return string

    def inList(self, input, lista):
        for elemento in lista:
            if(elemento == input):
                return True
        return False
    
    def generateNodes(self):
        string = ""
        shape = ""
        for item in self.estados:
            big = False
            accept = False
            counter = 0
            for transicion in self.transiciones:
                if(transicion.inicial == item or transicion.destino == item):
                    counter += 1
            for estado in self.aceptacion:
                if(estado == item):
                    accept = True
                    break
            if(accept):
                shape = "doublecircle"
            else:
                shape = "circle"
            if(counter > 5):
                big = True
            string += item + "[shape=" + shape 
            if(big):
                string += " height=2 width=2 " 
            string += " label=\"" + item + "\"]\n"
        string +=  "Inicio[shape=none label=\" \"]\n"
        return string
    
    def validar(self):
        if(self.nombre == "" or self.nombre == " "):
            return False
        for estado in self.estados:
            validados = []
            if(estado == self.nombre):
                return False
            elif(self.inList(estado, validados)):
                return False
            else:
                validados.append(estado)
        for simbolo in self.alfabeto:
            validados = []
            if(simbolo == self.nombre):
                return False
            elif(self.inList(simbolo, self.estados)):
                return False
            elif(self.inList(simbolo, validados)):
                return False
            else:
                validados.append(simbolo)
        if(not self.inList("#", self.simbolosPila)):
            return False
        if(not self.inList(self.inicial, self.estados)):
            return False
        if(len(self.transiciones) == 0):
            return False
        for transicion in self.transiciones:
            if(not self.inList(transicion.inicial, self.estados)):
                return False
            if(not self.inList(transicion.destino, self.estados)):
                return False
            if(transicion.leido != "$"):
                if(not self.inList(transicion.leido, self.alfabeto)):
                    return False
            if(transicion.extraido != "$"):
                if(not self.inList(transicion.extraido, self.simbolosPila)):
                    return False
            if(transicion.insertado != "$"):
                if(not self.inList(transicion.insertado, self.simbolosPila)):
                    return False
        if(len(self.aceptacion) == 0):
            return False
        return True
    
    def validarCadena(self, cadena):
        usadas = []
        estadoActual = self.inicial
        self.vaciarPila()
        for transicion in self.transiciones:
            if(transicion.inicial == estadoActual and transicion.destino != estadoActual and
            transicion.extraido == "$" and transicion.leido == "$" and transicion.insertado == "#"):
                estadoActual = transicion.destino
                self.pila.append("#")
                usadas.append(transicion)
        for letra in cadena:
            cambio = False
            for transicion in self.transiciones:
                if(transicion.inicial == estadoActual):
                    if(transicion.leido == letra or transicion.leido == "$"):
                        if(self.pila[len(self.pila)-1]==transicion.extraido or transicion.extraido == "$"):
                            if(transicion.extraido != "$"):
                                self.pila.pop()
                            estadoActual = transicion.destino
                            if(transicion.insertado != "$"):
                                self.pila.append(transicion.insertado)
                            cambio = True
                            if(transicion.extraido != "#"):
                                usadas.append(transicion)
                            break
            if(not cambio):
                self.vaciarPila()
                return [False, usadas]
        if(len(self.pila)==0):
            return [False, usadas]
        for transicion in self.transiciones:
            if(transicion.inicial == estadoActual):
                    if(transicion.leido == "$"):
                        if(self.pila[len(self.pila)-1]==transicion.extraido):
                            self.pila.pop()
                            estadoActual = transicion.destino
                            usadas.append(transicion)
                            break
        for estado in self.aceptacion:
            if(estado == estadoActual):
                self.vaciarPila()
                return [True, usadas]
        self.vaciarPila()
        return [False, usadas]

    def vaciarPila(self):
        while len(self.pila) > 0:
            self.pila.pop()
            
