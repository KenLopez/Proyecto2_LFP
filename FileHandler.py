class FileHandler:
    def __init__(self, direccion, ext):
        self.direccion = direccion
        self.info = []
        self.ext = ext

    def leerArchivo(self):
        if(len(self.direccion.split("."))==2):
            ext = self.direccion.split(".",-(len(self.ext)))[1]
            if (ext == self.ext):
                try:
                    archivoCurso = open(self.direccion, "r", encoding="utf-8")
                    if archivoCurso.readable():
                        self.archivo = archivoCurso.readlines()
                    archivoCurso.close
                    return True
                except:
                    input("Ruta de archivo ingresada es incorrecta...")
                    print("\n")
            else:
                input("El archivo debe ser " + self.ext + "...")
                print("\n")
        else:
            input("El archivo debe ser " + self.ext + "...")
            print("\n")

    def extraerInfo(self):
        for linea in self.archivo:
            self.info.append(linea)
        return self.info

