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
        """

        Modulo que convierte la inicial de un articulo en una mayuscula

        :return: None
        :rtype: Object

        """
        try:
            nombre = var.ui.txtNombreArti.text()
            nombre = nombre.title()
            var.ui.txtNombreArti.setText(nombre)
        except:
            print('Error en la aplicacion')
            return None

    def guardaArti(self):
        """

        modulo que se ejecuta cuando se intenta insertar un nuevo Articulo , este comprueba que el esapcio del nombre no esta vacio y conecta con la bbdd para añadir un
        nuevo articulo mediante el metodo altaArti en conexion y con el metodo cargaTabArti en conexion para añadir este a la tabla

        :return: None
        :rtype: Object
        """
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
        """

        Modulo que limpia los datos de la interfaz para poder volvel a introducir datos

        :return: None
        :rtype: Object

        """
        try:
            var.ui.txtNombreArti.setText("")
            var.ui.lblCodigoArti.setText("")
            var.ui.spinPrecio.setValue(0.00)
        except:
            print('Error en Limpiar Formato')
            return None

    def bajaArti(self):
        """

        Modulo que se ejcuta cuando el usuario qeuire dar de baja a un articulo. Para hacer eso recoje el codigo del articulo que se ha marcado en la tabla antes de clicar en en btnBorrar
        Este metodo llama al modulo de bajaArti y cargaTabArti en Conexion para poder, respectivamente, eliminar al articulo de la bbdd segun el codigo enviado y poder recargar la tabla del la interfaz para que no
        se visualice mas ese articulo.

        """
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
            nombre = var.ui.txtNombreArti.text()
            conexion.Conexion.buscaArti(nombre)



        except Exception as error:
            print('Error en buscar un articulo', error)

    def cargaArti(self):
        """

        Este metodo se ejecuta caundo se selecciona a un articulo en la tabla para poder visualizar el nombre, el codigo y el precio del articulo seleccionado en la interfaz y poder asi modificarlo

        :return: None
        :rtype: Object
        """
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
        """

        Modulo que se ejecua cuando se pulsa el btn de modificar un articulo. Este recoje los datos introducidos en la interfaz y modifica al articulo enviando en codigo(que no se puede cambiar)
        al metodo de modifArti en Conexion. Por ultimo se recarga la tabla con el metodo cargaTabArti en conexion

        """
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

