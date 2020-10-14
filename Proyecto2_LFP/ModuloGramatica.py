from FileHandler import FileHandler
class ModuloGramatica:
    def __init__(self):
        self.listaGramaticas = []

    def menuGramatica(self):
        while True:
            print("-----MÓDULO GRAMÁTICAS LIBRES DEL CONTEXTO-----\n")
            print("1. Cargar Archivo")
            print("2. Mostrar Información general")
            print("3. Arbol de Derivación")
            print("4. Generar Autómata de Pila Equivalente")
            print("5. Regresar\n")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                print("\n")
                self.crearGramatica()
            elif opcion == "2":
                print("\n---CARGAR GRAMÁTICAS---\n")
                pass   
            elif opcion == "3":
                print("\n---EVALUACIÓN DE CADENAS---")
                pass
                if(len(self.listaGramaticas) == 0):
                    print("ERROR: No existen GRE cargadas en memoria...\n")
                else:
                    usando = self.mostrarGramatica(self.listaGramaticas)
                    self.evaluacion(usando)
            elif opcion == "4":
                print("\n\n---ELIMINAR RECURSIVIDAD POR LA IZQUIERDA---\n")
                lista = []
                lista = self.cargarGramatica(False)
                usando = self.mostrarGRE(lista)
                usando.elimRec()
                input("\n\n")
            elif opcion == "5":
                print("\n\n")
                return
                
            else:
                print("\nNo se encuentra entre las opciones\n")
                input("Presiona ENTER para continuar...\n")

    def cargarGramatica(self, guardar):
        lista = []
        while(True):
            ruta = input("Ingrese la dirección del archivo: ")
            if(len(ruta)<4):
                print("ERROR: No se pudo cargar el archivo, intente nuevamente")
            else:
                archivo = FileHandler(ruta, "glc")
                info = []
                if(archivo.leerArchivo()):
                    info = archivo.extraerInfo()
                    listaCarga = self.armarGLC(info)
                    for glc in listaCarga:
                        if(guardar):
                            self.leerGLC(glc, guardar)
                        else:
                            lista.append(self.leerGRE(gre,guardar))
                    if(guardar):
                        print("Archivo cargado correctamente, las gramáticas han sido guardadas...\n")
                        break
                    else:
                        return lista
                else:
                    print("ERROR: No se pudo cargar el archivo, intente nuevamente")
        input()

    def mostrarGramatica(self, lista):
        print("\n____LISTADO DE GRAMÁTICAS___\n")
        for glc in lista:
            print("- ")
        while(True):
            seleccion = input("\nSeleccione la Gramática a utilizar: ")
            usando = False
            if(self.nombreInList(seleccion, self.listaGramaticas)):
                for glc in lista:
                    if (gre.nombre == seleccion):
                        usando = gre
                        break
