'''Gestion de facturas'''
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

import conexion
import var
import window
class Facturas:
    def buscaCli(self):
        """

        Modulo que busca el nombre y apellidos de un cliente segun el dni de una factura

        """
        try:
            dni = var.ui.txtDniFac.text().upper()
            print(dni)
            registro = conexion.Conexion.BuscaCliFac(dni)
            nombre = registro[0] + ', ' +registro[1]
            var.ui.lblNombreApel.setText(nombre)
            var.ui.txtDniFac.setText(dni)
        except Exception as e:
            print('Eror en Buascar cliente en facturas.:    ',e)


    def fecha(self):
        """

        Modulo que abre el calendario para elegir una fecha

        """
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ', error)


    def cargaFac(self):
         """

        Modulo que carga en la interfaz la factura que se ha selecionado en la tabla

         """
         try:
             fila = var.ui.tabFac.selectedItems()  # seleccionamos la fila
             datos = [var.ui.lblNumFac, var.ui.txtFechaFac]
             if fila:  # cargamos en row todos los datos de la fila
                 row = [dato.text() for dato in fila]
             for i, dato in enumerate(datos):
                 dato.setText(row[i])
             dni = conexion.Conexion.buscaDNIFac(row[0])
             var.ui.txtDniFac.setText(dni)
             registro = conexion.Conexion.buscaClifac(dni)
             if registro:
                 nombre = registro[0] + ', ' + registro[1]
                 var.ui.lblNombreApel.setText(nombre)
             #Para cargar las ventsas en la tabla de ventas
             conexion.Conexion.cargarLineasVenta(str(var.ui.lblNumFac.text()))

         except Exception as error:
             print('error alta en factura', error)



    def altaFac(self):
        """

        Modulo que se encarga de dar de alta a una factura. Este recoje todos los datos introducidos(dni del facturado y fecha de la factura) y los envia a AltaFac en conexion para qu8e este
        lo añada en al bbdd. Por ultimo se reocoje el codigo de la factura mediante el metodo buscaCodFac de Conexion

        """
        try:
            registro = []
            dni = var.ui.txtDniFac.text().upper()
            registro.append(str(dni))
            var.ui.txtDniFac.setText(dni)
            fecha = var.ui.txtFechaFac.text()
            registro.append(str(fecha))
            print(registro)
            registro = conexion.Conexion.AltaFac(registro)
            codfac = conexion.Conexion.buscaCodFac(self)
            var.ui.lblNumFac.setText(codfac)


        except Exception as error:
            print('Error al dar de alta un factura(invoice.altaFac) ', error)


    def cargarLineaVenta(self):
        """

        Metodo que carga las lineas de venta de una determinada factura en la tabla ventas

        :return: None

        :rtype: Object

        """
        try:
            suma = 0.0
            productos = []
            index = 0
            var.cmbProducto = QtWidgets.QComboBox
            var.cmbProducto.setFixedSize(150, 25)
            # Hay que cargar el combo
            conexion.Conexion.cargarCmbProducto()
            articulo = var.cmbProducto.currentText()

            var.cmbProducto.currentIndexChanged.connect(Facturas.procesoVenta)
            var.cmbProducto.setFixedSize(170, 25)
            conexion.Conexion.cargarCmbProducto(self=None)
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta)

            var.txtCantidad.setFixedSize(60, 25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error en Cargar la linea de venta(Invoice.Facturas.CargarLineaVenta):   ', error)
            return None


    def procesoVenta(self):
        """

        Metodo que suma y muestra los resultaos de las fentas de una determinada factura.

        """
        try:
            var.precio=""
            row = var.ui.tabVentas.currentRow()
            print(row)
            articulo = var.cmbProducto.currentText()
            conexion.Conexion.CargarPrecioProd(articulo)

            print(articulo)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            # Adecuamos el campo de precio para pasarlo a float y operar con el
            var.precio = articulo[1].replace('€', '')
            var.precio = var.precio.replace(',', '.')
            var.precio = var.precio.replace(' ', '')

            cantidad=round(float(var.txtCantidad.text().replace(',', '.')), 2)
            print('cantidad')
            total_venta = float(articulo) * float(cantidad)
            total_venta = round(total_venta, 2)
            total_linea=Facturas.totalLineaVenta(articulo)


        except Exception as error:
            print('Error en Cargar la linea de venta(Invoice.Facturas.procesoVenta):   ', error)


    def totalLineaVenta(self =None):
         """

        Metodo que calcula el total de la linea de venta.

         """
         try:
             row = var.ui.tabVentas.currentRow()
             cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)

             total_linea = round(float(var.precio) * float(cantidad), 2)
             var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_linea)+'€'))
             var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
         except Exception as error:
             print('Error en (Invoice.Facturas.totalLineaVenta):   ', error)

'''


         '''