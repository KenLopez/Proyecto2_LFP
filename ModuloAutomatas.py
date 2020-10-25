from FileHandler import FileHandler
from AutomataPila import AutomataPila
from Transicion import Transicion
from Graphviz import Graphviz
import os
class ModuloAutomatas:
    def __init__(self):
        self.listaAutomatas = []

    def menuAutomata(self):
        while (True):
            print("-----MÓDULO AUTÓMATAS DE PILA-----\n")
            print("1. Cargar Archivo")
            print("2. Mostrar Información de Autómata")
            print("3. Validar Cadena")
            print("4. Ruta de Evaluación")
            print("5. Recorrido Paso a Paso")
            print("6. Validar Cadena en una Pasada")
            print("7. Regresar\n")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                os.system("cls")
                self.cargarAutomata()
            elif opcion == "2":
                if(len(self.listaAutomatas) == 0):
                    os.system("cls")
                    print("ERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionAutomata("---MOSTRAR INFORMACIÓN DEL AUTÓMATA---\n")
                    usando.toPDF()
                    print("Volviendo al menú principal...")
                input()   
                os.system("cls")
            elif opcion == "3":
                if(len(self.listaAutomatas) == 0):
                    os.system("cls")
                    print("\nERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionAutomata("---VALIDAR CADENA---\n")
                    if(usando.validarCadena(input("Ingrese cadena a validar: "))[0]):
                        print("\nCadena Válida")
                    else:
                        print("\nCadena No Válida")
                input()
                os.system("cls")
            elif opcion == "4":
                if(len(self.listaAutomatas) == 0):
                    os.system("cls")
                    print("\nERROR: No existen GLC cargadas en memoria...\n")
                else:
                    os.system("cls")
                    usando = self.seleccionAutomata("---RUTA DE EVALUACIÓN---\n")
                    datos = usando.validarCadena(input("Ingrese cadena a validar: "))
                    if(datos[0]):
                        print("\nLa cadena fue reconocida exitosamente: \n")
                        for elemento in datos[1]:
                            print(elemento.toString())
                    else:
                        print("\nNo fue posible reconocer la cadena ingresada")
                input("\nPresione ENTER para continuar")
                os.system("cls")
            elif opcion == "7":
                os.system("cls")
                return
                
            else:
                print("\nNo se encuentra entre las opciones\n")
                input("Presiona ENTER para continuar...\n")
                os.system("cls")
            
    def cargarAutomata(self):
        while(True):
            os.system("cls")
            print("---CARGAR AUTÓMATAS---\n")
            ruta = input("Ingrese la dirección del archivo: ")
            if(len(ruta)<4):
                print("ERROR: No se pudo cargar el archivo, intente nuevamente")
            else:
                archivo = FileHandler(ruta, "ap")
                info = []
                if(archivo.leerArchivo()):
                    info = archivo.extraerInfo()
                    listaCarga = self.armarAP(info)
                    for automata in listaCarga:
                        automata = self.leerAP(automata.split("\n"))
                        if(automata.validar()):
                            if(not self.inList(automata.nombre,self.nombresAP())):
                                self.listaAutomatas.append(automata)
                            else:
                                print("ERROR: El autómata " + automata.nombre + " no pudo ser cargada, el nombre ya está registrado")
                        else:
                            print("ERROR: El autómata " + automata.nombre + " no pudo ser cargada, posee errores en sus elementos.")
                    print("Carga terminada...")
                    break
                else:
                    print("ERROR: No se pudo cargar el archivo, intente nuevamente")
        input()
        os.system("cls")
    
    def nombresAP(self):
        lista = []
        for ap in self.listaAutomatas:
            lista.append(ap.nombre)
        return lista

    def armarAP(self, info):
        ap = ""
        listaCarga = []
        for linea in info:
            if(linea == "%\n" or linea == "%"):
                listaCarga.append(ap)
                ap = ""
            else:
                ap += linea
        return listaCarga

    def leerAP(self, data):
        transiciones = []
        for i in range(6, len(data)-1):
            transiciones.append(Transicion(data[i].split(";")[0].split(",")[0],
            data[i].split(";")[0].split(",")[1], data[i].split(";")[0].split(",")[2], 
            data[i].split(";")[1].split(",")[0], data[i].split(";")[1].split(",")[1]))
        return AutomataPila(data[0], data[3].split(","), data[1].split(","), data[2].split(","), 
        data[4], data[5].split(","), transiciones)

    def inList(self, input, lista):
        for elemento in lista:
            if(elemento == input):
                return True
        return False

    def seleccionAutomata(self, titulo):
        while(True):
            print(titulo)
            print("___LISTADO DE AUTÓMATAS___\n")
            for ap in self.nombresAP():
                print("- " + ap)
            seleccion = input("\nSeleccione la Gramática a utilizar: ")
            if(self.inList(seleccion, self.nombresAP())):
                for ap in self.listaAutomatas:
                    if (ap.nombre == seleccion):
                        return ap
            else:
                print("No se encuentra entre las opciones...")
