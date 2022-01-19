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
            fila = var.ui.tabFac.selectedItems()  # seleciona la fila #Busca el resto de los datos de la factura
            if fila:
                row = [dato.text() for dato in fila]
            var.ui.lblNumFac.setText(row[0])
            var.ui.txtFechaFac.setText(row[1])
            numFac = row[0]
            #acceder a los datos de la bbdd de facturas y clientes
            cliente = conexion.Conexion.oneFac(numFac)
            nombre = cliente[0]
            var.ui.lblNombreApel.setText(str(nombre))
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
            conexion.Conexion.cargarCmbproducto(self)
            #productos = (conexion.Conexion.cargarProductos)¡
            #for i in productos:
            #    var.ui.cmbProducto.addItem(i)
            #var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(70,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index +1)
            var.ui.tabVentas.setCellWidget(index,1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index,3, var.txtCantidad)
        except Exception as error:
            print('Error en Cargar la linea de venta(Invoice.Facturas.CargarLineaVenta):   ', error)
            return None

    def processVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            nombrearticulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(nombrearticulo)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row, 2).setTextAligment(QtCore.Qt.AlignCenter)
            precio = dato[1].replace('€','')
            var.precio = precio.replace(',','.')


        except Exception as error:
            print('Error en Cargar la linea de venta(Invoice.Facturas.processVenta):   ', error)
            return None

    def totalLineaVenta(self =None):
     try:
         row = var.ui.tabVentas.currentRow()
         cantidad = round(float(var.txtCantidad.text().replace(',', '.')),2)
         total_ventas= float(var.precio) * float(cantidad)
         round(total_ventas,2)
         var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_ventas) + '€'))
         var.ui.tabVentas.item(row, 4).setTextAligment(QtCore.Qt.AlignRight)
     except Exception as error:
         print('Error en (Invoice.Facturas.totalLineaVenta):   ', error)
         return None