from FileHandler import FileHandler
from GramaticaLC import GramaticaLC
from Produccion import Produccion
import os
class ModuloGramatica:
    def __init__(self):
        self.listaGramaticas = []

    def menuGramatica(self):
        while (True):
            print("-----MÓDULO GRAMÁTICAS LIBRES DEL CONTEXTO-----\n")
            print("1. Cargar Archivo")
            print("2. Mostrar Información general")
            print("3. Arbol de Derivación")
            print("4. Generar Autómata de Pila Equivalente")
            print("5. Regresar\n")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                os.system("cls")
                self.cargarGramatica()
            elif opcion == "2":
                if(len(self.listaGramaticas) == 0):
                    os.system("cls")
                    print("ERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionGramatica("---MOSTRAR INFORMACIÓN GENERAL---\n")
                    print(usando.toString())
                input()   
                os.system("cls")
            elif opcion == "3":
                if(len(self.listaGramaticas) == 0):
                    os.system("cls")
                    print("\nERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionGramatica("---ÁRBOL DE DERIVACIÓN---\n")
                    usando.generateArbol()
                input()
                os.system("cls")
            elif opcion == "4":
                if(len(self.listaGramaticas) == 0):
                    os.system("cls")
                    print("\nERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionGramatica("---GENERAR AUTÓMATA DE PILA---\n")
                    usando.toAP()
                    print("\nRegresando al menú anterior...")
                input()
                os.system("cls")
            elif opcion == "5":
                os.system("cls")
                return
                
            else:
                print("\nNo se encuentra entre las opciones\n")
                input("Presiona ENTER para continuar...\n")
                os.system("cls")

    def cargarGramatica(self):
        while(True):
            os.system("cls")
            print("---CARGAR GRAMÁTICAS---\n")
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
                        gramatica = self.leerGLC(glc.split("\n"))
                        if(gramatica.validarLC()):
                            if(gramatica.validar()):
                                if(not self.inList(gramatica.nombre,self.nombresGLC())):
                                    self.listaGramaticas.append(gramatica)
                                else:
                                    print("ERROR: La gramática " + gramatica.nombre + " no pudo ser cargada, el nombre ya está registrado")
                            else:
                                print("ERROR: La gramática " + gramatica.nombre + " no pudo ser cargada, posee errores en sus elementos.")
                        else:
                            print("ERROR: La gramática " + gramatica.nombre + " no pudo ser cargada, se trata de una gramática regular.")
                    print("Carga terminada...")
                    break
                else:
                    print("ERROR: No se pudo cargar el archivo, intente nuevamente")
        input()
        os.system("cls")

    def nombresGLC(self):
        lista = []
        for glc in self.listaGramaticas:
            lista.append(glc.nombre)
        return lista

    def armarGLC(self, info):
        glc = ""
        listaCarga = []
        for linea in info:
            if(linea == "%\n" or linea == "%"):
                listaCarga.append(glc)
                glc = ""
            else:
                glc += linea
        return listaCarga

    def leerGLC(self, data):
        producciones = []
        for i in range(4, len(data)-1):
            produccion = data[i].split(">")
            producciones.append(Produccion(produccion[0],produccion[1].split(" ")))
        return GramaticaLC(data[0], data[1].split(","), data[2].split(","), data[3], producciones)

    def inList(self, input, lista):
        for elemento in lista:
            if(elemento == input):
                return True
        return False

    def seleccionGramatica(self, titulo):
        while(True):
            print(titulo)
            print("___LISTADO DE GRAMÁTICAS___\n")
            for glc in self.nombresGLC():
                print("- " + glc)
            seleccion = input("\nSeleccione la Gramática a utilizar: ")
            if(self.inList(seleccion, self.nombresGLC())):
                for glc in self.listaGramaticas:
                    if (glc.nombre == seleccion):
                        return glc
            else:
                print("No se encuentra entre las opciones...")
