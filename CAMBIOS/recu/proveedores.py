import conexion, var

class Proveedor():
    def altaprov(self):
        try:
            newpro = []
            newpro.append(str(var.ui.txtCif.text()))
            newpro.append(str(var.ui.txtNomprov.text()))
            newpro.append(str(var.ui.lblFechaprov.text()))
            newpro.append(str(var.ui.txtEmail.text()))
            newpro.append(str(var.ui.txtTelefono.text()))

            conexion.Conexion.altaproveedor(newpro)

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
                var.ui.txtAltaCli.setText(str(data))
            elif var.ui.tabPrograma.currentIndex() == 1:
                var.ui.txtFechafac.setText(str(data))
            elif var.ui.tabPrograma.currentIndex() == 3:
                var.ui.lblFechaprov.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def limpiar(self = None):
        try:
            form = [var.ui.txtCif, var.ui.lblFechaprov, var.ui.txtNomprov, var.ui.txtEmail, var.ui.txtTelefono ]
            for dato in form:
                dato.setText('')
        except Exception as error:
            print('Error en limpiar formulario proveedor')

    def cargarProv(self):
        try:
            Proveedor.limpiar(self)
            fila = var.ui.tabProveedores.selectedItems()
            form = [  var.ui.txtNomprov, var.ui.lblFechaprov, var.ui.txtTelefono]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(form):
                dato.setText(row[i])

            form2 = [var.ui.txtCif, var.ui.txtEmail ]
            row2 = conexion.Conexion.datosprov(row[0])
            for i, dato in enumerate(form2):
                dato.setText(row2[i])

        except Exception as error:
            print('Error en cargar dato de un proveedor ', error)



















