from PyQt5 import QtWidgets

import conexion, var

class Proveedor():
    def altaprov(self):
        try:
            newpro = []
            newpro.append(str(var.ui.txtCif.text()))
            newpro.append(str(var.ui.txtRazonSocial.text()))
            newpro.append(str(var.ui.lblAltaProv.text()))
            newpro.append(str(var.ui.txtEmail.text()))
            newpro.append(str(var.ui.txtTelefono.text()))
            newpro.append(var.ui.cmbPago.currentText())

            conexion.Conexion.altaproveedor(newpro)
            conexion.Conexion.cargaTabProv(self)

        except Exception as error:
            print ("error en alta proveedor ", error)

    def calendarpro(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print("Abrir calendario ", error)

    def cargarFecha(qDate):
        """

        Carga la fecha elegida en el widget Calendar
        :param qDate:
        :type qDate:

        """
        try:
            data = (str(qDate.day()).zfill(2) + '/' + str(qDate.month()).zfill(2) + '/' + str(qDate.year()))
            if var.ui.tabPrograma.currentIndex() == 0:
                var.ui.lblAltaProv.setText(str(data))
            elif var.ui.tabPrograma.currentIndex() == 1:
                var.ui.lblAltaProv.setText(str(data))
            elif var.ui.tabPrograma.currentIndex() == 3:
                var.ui.lblAltaProv.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def limpiar(self = None):
        try:
            form = [var.ui.txtCif, var.ui.lblAltaProv, var.ui.txtRazonSocial, var.ui.txtEmail, var.ui.txtTelefono]
            for dato in form:
                dato.setText('')

            var.ui.cmbPago.setCurrentIndex(0)
        except Exception as error:
            print('Error en cargarfecha del  proveedor')

    def cargarProv(self):
        try:
            Proveedor.limpiar(self)
            fila = var.ui.tabProv.selectedItems()
            form = [  var.ui.txtRazonSocial, var.ui.lblAltaProv, var.ui.txtTelefono]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(form):
                dato.setText(row[i])

            form2 = [var.ui.txtCif, var.ui.txtEmail, var.ui.cmbPago ]
            row2 = conexion.Conexion.datosprov(row[0])
            for i, dato in enumerate(form2):
                if i == 2:
                    dato.setCurrentText(str(row2[2]))
                else:
                    dato.setText(row2[i])

        except Exception as error:
            print('Error en cargar datos de un proveedor ', error)

    def bajaProv(self):
        """

        Metodo que se ejecuta cuando el ususario quiere dar de baja a un proveedor. Este llama al metodo bajaProv de Conexxion que recibe el cif del proveedor a eliminar. Por
        ultimo, se llama al metodo cargaTabProv para recargar la tabla y que el proveedor eliminado no aparezca mas en esta

        """
        try:
            cif = var.ui.txtCif.text()
            nombre = var.ui.txtRazonSocial.text()
            conexion.Conexion.bajaProv(self,cif,nombre)
            conexion.Conexion.cargaTabProv(self)

        except Exception as error:
            print('Error en dar de baja un provedor', error)

    def modifProv(self):
        """

        Metodo que se ejecuta cuando se quiere modificar a un cliente. Este metodo recoje todos los datos introducidos por el usuario y los envia al metod modifCli de conexion
        para que e modifiqeu el la bbdd. Por ultimo se llama al metrodo cargarTabCli para actualizar los datos de la interfaz.

        """

        try:

            fila = var.ui.tabProv.selectedItems()
            if fila:
                row = [dato.text() for dato in fila]

            row2 = conexion.Conexion.datosprov(row[0])
            modprov = []
            modprov.append(str(var.ui.txtCif.text()))
            modprov.append(str(var.ui.txtRazonSocial.text()))
            modprov.append(str(var.ui.lblAltaProv.text()))
            modprov.append(str(var.ui.txtEmail.text()))
            modprov.append(str(var.ui.txtTelefono.text()))
            modprov.append(var.ui.cmbPago.currentText())

            if  row2[0] == modprov[0]:
                conexion.Conexion.modifProv(self, modprov)
                conexion.Conexion.cargaTabProv(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Operacion no realizada. No se puede modificar el cif')
                msg.exec()
        except Exception as error:
            print('Error en Modificar un proovedor', error)

    def cargaPago(self):
        """

        Modulo que carga la lista de provincias en la interfaz. Para conseguir la lista de provincias llama al metodo listaProvincia que
        devuelve un array con las provincias

        """
        try:
            var.ui.cmbPago.clear()
            pagos = var.pago
            for i in pagos:
                var.ui.cmbPago.addItem(i)
        except Exception as error:
            print('Error en módulos al cargar pagos, ', error)















