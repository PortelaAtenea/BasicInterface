'''

fichero de eventos generales(eventos que no tienen relacion directa con ningun otro archivo(salir del programa, etc))


'''
import os.path
import shutil
import sys, var
import zipfile
from datetime import datetime
from zipfile import ZipFile

import conexion
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

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%M.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
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
        try:
            dirpro = os.getcwd()
            print(dirpro)
            option = QtWidgets.QFileDialog.Options()
            filename=var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '', '*.zip', options=option )

            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall()
                bbdd.close()
                shutil.move('bbdd.sqlite', str(dirpro))
                conexion.Conexion.db_connect(var.filedb)
                conexion.Conexion.listaProvincias()
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('EXITO!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('La base de datos ha sido Exportada con exito!!')
                msg.exec()
        except Exception as error:
            print('Error al restaurar backup de la bbdd ', error)

