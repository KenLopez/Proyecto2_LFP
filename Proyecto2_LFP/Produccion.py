class Produccion:
    def __init__(self, noTerminal = "", expresion = []):
        self.noTerminal = noTerminal
        self.expresion = expresion

    def toString(self):
        string = ""
        string += self.noTerminal + " > "
        string += self.expToString()
        return string

    def expToString(self):
        exp = ""
        for i in range(0,len(self.expresion)):
            exp += self.expresion[i]
            if(i != len(self.expresion)-1):
                exp += " "
        return exp


