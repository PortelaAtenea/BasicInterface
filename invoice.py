'''Gestion de facturas'''
from PyQt5 import QtWidgets, QtCore

import conexion
import var
import window
class Facturas:
    def buscaCli(self):
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
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ', error)


    def altaFac(self):
        try:
            registro = []
            dni = var.ui.txtDniFac.text().upper()
            registro.append(str(dni))
            var.ui.txtDniFac.setText(dni)
            fecha = var.ui.txtFechaFac.text()
            registro.append(str(fecha))
            print(registro)
            registro = conexion.Conexion.AltaFac(registro)


        except Exception as error:
            print('Error al dar de alta un calendario ', error)


    def cargaFac(self):
        try:
            valor = 0
            #Facturas.limpiaFormFac(self)
            fila = var.ui.tabFac.selectedItems()  # seleciona la fila
            print(fila) #Busca el resto de los datos de la factura

            #cuando yo marque en una linea de la table, me lo prepara ya tambien en la tabla ventas


        except Exception as error:
            print('Error en Cargar datos de Facturas', error)
            return None

    def cargarLineaVenta(self):
        try:
            print('cargar linea de venta')
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(180,25)
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(80,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)

            var.ui.tabVentas.setRowCount(index +1)
            var.ui.tabVentas.setCellWidget(index,1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index,3, var.txtCantidad)
        except Exception as error:
            print('Error en Cargar la linea de venta(Invoice.Facturas.CargarLineaVenta):   ', error)
            return None