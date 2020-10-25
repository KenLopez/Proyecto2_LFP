from ModuloGramatica import ModuloGramatica
from ModuloAutomatas import ModuloAutomatas
import os
class Menu:
    def __init__(self):
        self.archivo = 0
        self.modulo = ModuloAutomatas()
        self.moduloG = ModuloGramatica()

    def mostrarTitulo(self):
        print("----------SPARK STACK-----------\n\n")
        print("Lenguajes Formales y de Programación")
        print("Sección: B")
        print("Nombre: Kenneth Haroldo López López")
        print("Carné: 201906570\n")
        input()
        os.system("cls")
        self.menuPrincipal()
        

    def menuPrincipal(self):
        while True:
            print("-----MENÚ PRINCIPAL-----\n")
            print("1. Módulo Gramáticas Libres del Contexto")
            print("2. Módulo Autómatas de Pila")
            print("3. Salir\n")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                os.system("cls")
                self.moduloG.menuGramatica()
            elif opcion == "2":
                os.system("cls")
                self.modulo.menuAutomata()  
            elif opcion == "3":
                print("Saliendo del programa...")
                return  
            else:
                print("\nNo se encuentra entre las opciones\n")
                input("Presiona ENTER para continuar...\n")
                os.system("cls")
