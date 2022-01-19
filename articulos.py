''''
Funciones  gestion de clientes
'''
from idlelib import query
from tkinter import Label

from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import conexion
from window import *
import var


class Articulos():




    def mayus():
        try:
            nombre = var.ui.txtNombreArti.text()
            nombre = nombre.title()
            var.ui.txtNombreArti.setText(nombre)
        except:
            print('Error en la aplicacion')
            return None

    def guardaArti(self):
        try:
            if var.ui.txtNombreArti.text() == '':
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
            else:
                # preparamos el registro
                newArti = []  # para la base de datos
                arti = [var.ui.txtNombreArti]  # para la base de datos
                tabArti = []  # para la tableWidget
                Articulo = [var.ui.txtNombreArti]
                # codigo para cargar en la table
                for i in arti:
                    newArti.append(i.text())
                for i in Articulo:
                    tabArti.append(i.text())

                valor = var.ui.spinPrecio.value()
                newArti.append(valor)
                tabArti.append(valor)
                # Cargamos en la tabla

                conexion.Conexion.altaArti(newArti)  # graba en la tabla de la base de datos
                conexion.Conexion.cargaTabArti(self)  # reacrga la tabla


        except:
            print('Error en Guardar Articulo')
            return None

    def limpiaFormArti(self):
        try:
            var.ui.txtNombreArti.setText("")
            var.ui.lblCodigoArti.setText("")
            var.ui.spinPrecio.setValue(0.00)
        except:
            print('Error en Limpiar Formato')
            return None

    def bajaArti(self):
        try:
            fila = var.ui.tabArti.selectedItems()  # seleciona la fila
            if fila:
                row = [dato.text() for dato in fila]
            codigo = row[0]
            conexion.Conexion.bajaArti(codigo)
            conexion.Conexion.cargaTabArti(self)

        except Exception as error:
            print('Error en dar de baja un Articulo', error)
    def buscarArti(self):
        try:
            nombre = var.ui.txtBusqueda.text()
            conexion.Conexion.buscaArti(nombre)



        except Exception as error:
            print('Error en buscar un articulo', error)

    def cargaArti(self):

        try:
            valor = 0
            Articulos.limpiaFormArti(self)
            fila = var.ui.tabArti.selectedItems()# seleciona la fila
            if fila:
                row = [dato.text() for dato in fila]
            var.ui.lblCodigoArti.setText(row[0])
            var.ui.txtNombreArti.setText(row[1])
            var.ui.spinPrecio.setValue(float(row[2]))
        except Exception as error:
            print('Error en Cargar datos de un Articulo- Articulos', error)
            return None


    def modifArti(self):
        try:
            modArti = []
            modArti.append(var.ui.lblCodigoArti.text())
            modArti.append(var.ui.txtNombreArti.text())
            modArti.append(var.ui.spinPrecio.text())
            conexion.Conexion.modifArti(modArti)
            conexion.Conexion.cargaTabArti(self)
            Articulos.limpiaFormArti(self)
        except Exception as error:
            print('Error en Modificar un Articulo', error)

