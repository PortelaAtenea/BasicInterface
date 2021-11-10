'''

fichero de eventos generales(eventos que no tienen relacion directa con ningun otro archivo(salir del programa, etc))


'''
import sys, var

from window import *


class Eventos():


    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec_():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en modulo salir ', error)

    def abrirCal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ', error)


    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en al redimensionar la tabla ', error)


    def abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir cuador de dialogo ', error)
