'''

fichero de eventos generales(eventos que no tienen relacion directa con ningun otro archivo(salir del programa, etc))


'''
import os.path
import shutil
import sys, var
import zipfile
from datetime import datetime
from zipfile import ZipFile

from PyQt5 import QtPrintSupport
from PyQt5.QtWidgets import QMessageBox

import conexion
from window import *


class Eventos():


    def Salir(self):
        """

        Metodo qeu se ejecuta cuando el ususario pulca los botones de salida. Este metodo muestra una aviso qeu requiere la confirmacion del usuario para cerrar la aplicaion o no.

        """
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec_():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en modulo salir ', error)

    def abrirCal(self):
        """

        Metodo que abre el calendario cuando es requerido por el ususario

        """
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario', error)


    def resizeTablaCli(self):
        """

        Metodo que cambia el tamaño de la tabla de clientes para que quede mas igualado a los tamaños del contenido

        """
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en al redimensionar la tabla ', error)

    def resizeTablaArti(self):
        """

        Metodo que cambia el tamaño de la tabla de Articulos para que quede mas igualado a los tamaños del contenido


        """
        try:
            header = var.ui.tabArti.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 :
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en al redimensionar la tabla ', error)
    def resizeTablaVentas(self):
        """

        Metodo que cambia el tamaño de la tabla de ventas para que quede mas igualado a los tamaños del contenido


        """
        try:
            header = var.ui.tabArti.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        except Exception as error:
            print('Error en al redimensionar la tabla ', error)

    def resizeTablaProv(self):
        """

        Metodo que cambia el tamaño de la tabla de ventas para que quede mas igualado a los tamaños del contenido


        """
        #Cambiar a la tabla de prov
        try:
            header = var.ui.tabProv.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en al redimensionar la tabla ', error)


    def abrir(self):
        """

        Metodo que abre la ventana de dialogo cuando es requerido por el ususario para abrir algo

        """
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir cuador de dialogo ', error)

    def crearBackup(self):
        """

        Metodo que cera un backup de la bbdd de clientes cuando es requerido por el usuario

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%M.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                #Enviar var.copia al drive

                fichzip.close()
                shutil.move(str(var.copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('EXITO!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('La base de datos ha sido creada con exito!!')
                msg.exec()
        except Exception as error:
            print('Error al crear buckup de la bbdd ', error)

    def restaurarBackup(self):
        """

        Metodo que restaura la bbdd cuando es requerido por el usuario

        """
        try:
            option = QtWidgets.QFileDialog.Options()
            filename=var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '', '*.zip', options=option )

            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                print(file)
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.listaProvincias(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('EXITO!!!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('La base de datos ha sido Exportada con exito!!')
            msg.exec()
            conexion.Conexion.cargaTabCli(self)
        except Exception as error:
            print('Error al restaurar backup de la bbdd ', error)
    def imprimir(self):
        """

        Modulo que abre una ventana de dialogo cuando el usuario pide imprimir los datos de los clientes

        """
        try:
            printDialgo = QtPrintSupport.QPrintDialog()
            if printDialgo.exec():
                printDialgo.show()
        except Exception as error:
            print('Error al imprimir ', error)

    def ExportarDatos(self):
        """

        Metodo que exporta los datos de los clientes de la bbdd a un excel

        """
        try:
            conexion.Conexion.exportExcel(self)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Datos exportados con éxito.")
                msgBox.setWindowTitle("Operación completada")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje generado exportar datos ', error)
        except Exception as error:
            print('Error en evento exportar datos ',error)
