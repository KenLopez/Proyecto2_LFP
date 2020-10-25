class Arbol:
    def __init__(self, raiz = ""):
        self.raiz = raiz
        self.hijos = []

    def addHijo(self, hijo):
        self.hijos.append(Arbol(hijo))

    def toDot(self):
        strNodos = self.raiz + "[label=\"" + self.raiz + "\"]\n"
        strUniones = ""
        nodos = []
        nodos.append(self.raiz)
        datos = []
        datos.append(strNodos)
        datos.append(strUniones)
        datos.append(nodos)
        datos.append(self.raiz)
        datos = self.nodosHijo(self, datos)
        string = datos[0] + datos[1]
        return string

    def nodosHijo(self, arbol, datos):
        padre = datos[3] + ""
        for hijo in arbol.hijos:
            counter = 1
            contar = True
            while contar:
                if(self.inList(hijo.raiz + str(counter), datos[2])):
                    counter += 1
                else:
                    datos[0] += hijo.raiz + str(counter) + "[label=\"" + hijo.raiz + "\"]\n"
                    datos[1] += padre + "--" + hijo.raiz + str(counter) + "\n"
                    datos[2].append(hijo.raiz + str(counter))
                    if(len(hijo.hijos)>0):
                        datos[3] = hijo.raiz + str(counter)
                        datos = self.nodosHijo(hijo, datos)
                    contar = False
        return datos

    def inList(self, input, lista):
        for elemento in lista:
            if(elemento == input):
                return True
        return False