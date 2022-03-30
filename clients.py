''''
Funciones  gestion de clientes
'''
from tkinter import Label

from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox

import conexion
from window import *
import var


class Clientes():

    def validarDNI(dni):
        """

        Modulo que se encarga de comprobar que el dni introducido es valido. Si eso se cumple, aparaecera en la interfaz una V en verde para señalizarlo. En
        caso contrario, Aparecera una X roja y el cajon de texto tendra un fondo rojo

        :return:None
        :rtype: Object

        """
        try:
            global validodni
            validodni = False
            #dni = var.ui.txtDni.text()  # Sea lo que sea que hayya en una caja de texto de la interfaz(float, int String) el lo va a cojer siempre como un string
            #var.ui.txtDni.setText(dni)
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # lETRAS DEL DNI
            dig_ext = 'XYZ'  # Letra Dni extrangero
            reemp_dig_ext = {'X': '0', 'Y': '1',
                             'Z': '2'}  # rEEMPLAZAR EL IGITO POR LA LETRA EXTRANGERA. #ES UN  DICCIONARIO
            numeros = '1234567890'
            dni = dni.upper()  # convierte la letra en mayuscula
            if len(dni) == 9:  # si la longitud es igual a 9
                dig_control = dni[8]  #
                dni = dni[:8]  # Tomo elnumero de los 8 primeros
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    print('Correcto')
                    validodni = True  # lo pongo a true

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValidoDni.setText('V')

                    print('Correcto')
                    validodni = True
                    return validodni
                    var.ui.txtDni.setStyleSheet('background-color: white;')
                else:
                    print('Incorrecto')

                    validodni = False
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValidoDni.setText('X')
                    var.ui.txtDni.setStyleSheet('background-color: pink;')
            else:
                print('Incorrecto')

                validodni = False
                var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidoDni.setText('X')
                var.ui.txtDni.setStyleSheet('background-color: pink;')

            return validodni
        except:
            print('Error en la aplicacion')
            return False

    # def selSex(self):
    #     try:
    #         if var.ui.rbtFem.isChecked():
    #             print('Marcado Femenino :)')
    #         if var.ui.rbtHom.isChecked():
    #             print('Marcado Masculino :(')
    #     except Exception as error:
    #         print('Error en Modulo Sex')
    #
    # def selPago(self):
    #     try:
    #         if var.ui.chkEfectivo.isChecked():
    #             print('Ha Selecionado efectivo')
    #         if var.ui.chkTargeta.isChecked():
    #             print('Ha Selecionado Targeta')
    #         if var.ui.chkTransfe.isChecked():
    #             print('Ha Selecionado Transferencia')
    #         if var.ui.chkCargoCuenta.isChecked():
    #             print('Ha Selecionado Cargo a cuenta')
    #
    #     except Exception as error:
    #         print('Error en modulo Seleccionar modo de pago')

    def cargaProv(self):
        """

        Modulo que carga la lista de provincias en la interfaz. Para conseguir la lista de provincias llama al metodo listaProvincia que
        devuelve un array con las provincias

        """
        try:
            var.ui.cmbProv.clear()
            prov = conexion.Conexion.listaProvincias(self)
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en módulos al cargar provinvia, ', error)

    def cargaMun(self):
        """
        Modulo que se encarga de colocar en el cmb de la interfaz la lista de mucnicipios correspondiente a la provincia seleccionada.
        Para conseguir el array, llama al metodo listaMunicipios pasandole la provincia que fue seleccionada

        """
        try:
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            mun = conexion.Conexion.listaMunicipios(self,prov)
            for i in mun:
                var.ui.cmbMuni.addItem(i)
        except Exception as error:
            print('Error en módulo de cargar municipio, ', error)

    # def selMuni(muni):
    #     try:
    #         print('Has seleccionado el municipio: ', muni)
    #         return muni;
    #     except Exception as error:
    #         print('Error en seleccion municipio', error)

    def cargarFecha(self, qDate):
        """
        Metodo que carga la fecha selecionada en el calendario, en la caja de texto correspondiente en la interfaz

        :param qDate: Metodo necesario para pasrsear la fecha de tipo Date a tipo String
        :type qDate: Libreria
        """
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))

            if var.ui.tabPrograma.currentIndex() == 0:
                var.ui.txtAltaCli.setText(str(data))

            elif var.ui.tabPrograma.currentIndex() == 1:
                var.ui.txtFechaFac.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en cargar fecha del calendario', error)
    def cargarFechaFactura(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaFactura.setText(str(data))
            var.dlgcalendarFac.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def mayus():
        """

        Metodo que convierte las iniciales del nombre y apellidos a mayuscula

        :return: None
        :rtype: Object
        """
        try:
            apellido = var.ui.txtApel.text()
            apellido = apellido.title()
            var.ui.txtApel.setText(apellido)
            nombre = var.ui.txtNome.text()
            nombre = nombre.title()
            var.ui.txtNome.setText(nombre)
            dir = var.ui.txtDir.text()
            dir = dir.title()
            var.ui.txtDir.setText(dir)
        except:
            print('Error en la aplicacion')
            return None

    def guardaCli(self):
        """

        Metodo qeu recoje los datos de un nuevo cliente  y los envia a altaCli en caso de que el dni sea valido (siendo esto comprobado por la funcion validoDni de Clientes)

        :return: None
        :rtype: Object
        """
        try:
            # preparamos el registro
            newcli = []  # para la base de datos
            cliente = [var.ui.txtDni, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome,
                       var.ui.txtDir]  # para la base de datos
            tabClie = []  # para la tableWidget
            client = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            # codigo para cargar en la table
            for i in cliente:
                newcli.append(i.text())
            for i in client:
                tabClie.append(i.text())

            # cargar los radiobuttons
            newcli.append(var.ui.cmbProv.currentText())
            newcli.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHom.isChecked():
                newcli.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                newcli.append('Mujer')
            else:
                newcli.append('No especificado')
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTargeta.isChecked():
                pagos.append('Targeta')
            pagos = set(pagos)  # evita duplicados
            newcli.append(' ; '.join(pagos))
            tabClie.append(' ; '.join(pagos))
            valor = var.ui.spinEnvio.value()
            if valor == 0:
                newcli.append('Recojida por cliente')
                tabClie.append('Recojida por cliente')
            if valor == 1:
                newcli.append('Envio nacional Paqueteria Expres urgente')
                tabClie.append('Envio nacional Paqueteria Expres urgente')
            if valor == 2:
                newcli.append('Envio nacional con paqueteria ordinario')
                tabClie.append('Envio nacional con paqueteria ordinario')
            if valor == 3:
                newcli.append('Envio internacional')
                tabClie.append('Envio internacional')
            # Cargamos en la tabla

            if validodni:  # la global
                # row = 0
                # column = 0
                # var.ui.tabClientes.insertRow(row)
                # for campo in tabClie:
                #     cell = QtWidgets.QTableWidgetItem(str(campo))
                #     var.ui.tabClientes.setItem(row, column, cell)
                #     column += 1
                conexion.Conexion.altaCli(newcli)  # graba en la tabla de la base de datos
                conexion.Conexion.cargaTabCli(self)  # reacrga la tabla

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI NO VALIDO!!!!')
                msg.exec()
                # colocar ventana de aviso por codigo --> qtwidgets.qmessagebox python
        except:
            print('Error en Guardar clientes')
            return None

    def limpiaFormcli(self):
        """

        Metodo que se encarga de limpiar los datos de la interfaz para poder volver a introducirlos

        :return: None
        :rtype: Object
        """
        try:
            var.ui.txtApel.setText("")
            var.ui.txtDni.setText("")
            var.ui.txtAltaCli.setText("")
            var.ui.txtNome.setText("")
            var.ui.txtDir.setText("")
            cajas = [var.ui.txtApel, var.ui.txtNome, var.ui.txtDni, var.ui.txtAltaCli, var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.chkTargeta.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMuni.setCurrentIndex(0)
        except:
            print('Error en Limpiar Formato')
            return None

    def bajaCli(self):
        """

        Metodo que se ejecuta cuando el ususario quiere dar de baja a un cliente. Este llama al metodo bajaCli de Conexxion que recibe el dni del cliente a eliminar. Por
        ultimo, se llama al metodo cargaTabCli para recargar la tabla y que el cliente eliminado no aparezca mas en esta

        """
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargaTabCli(self)

        except Exception as error:
            print('Error en dar de baja un clientes', error)

    def cargaCli(self):
        """

        Metodo que carga los datos de un cliente determinado al seleccioarlo en la tabla de la interfaz

        :return: None
        :rtype: Object
        """
        try:
            valor = 0
            Clientes.limpiaFormcli(self)
            fila = var.ui.tabClientes.selectedItems()  # seleciona la fila
            datos = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Targeta' in row[4]:
                var.ui.chkTargeta.setChecked(True)
            if 'Transferencia' in row[4]:
                var.ui.chkTransfe.setChecked(True)
            if 'Cargo' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)

            registro = conexion.Conexion.oneClie(self,row[0])  # row[0] es el dni
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMuni.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Mujer':
                var.ui.rbtFem.setChecked(True)
            elif str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)


            if str(registro[4]) == 'Envio nacional Paqueteria Expres urgente':
                valor = 1
            if str(registro[4]) == 'Recojida por cliente':
                valor = 0
            if str(registro[4]) == 'Envio nacional con paqueteria ordinario':
                valor = 2
            if str(registro[4]) == 'Envio internacional':
                valor = 3
            var.ui.spinEnvio.setValue(valor)

            #En el modulo Facturacion

            nombre = row[1] + ', ' + row[2]
            print(nombre)
            var.ui.lblNombreApel.setText(nombre)
            var.ui.txtDniFac.setText(row[0])
        except Exception as error:
            print('Error en Cargar datos de un cliente en clientes.Clientes.CargaCli', error)
            return None


    def modifCli(self):
        """

        Metodo que se ejecuta cuando se quiere modificar a un cliente. Este metodo recoje todos los datos introducidos por el usuario y los envia al metod modifCli de conexion
        para que e modifiqeu el la bbdd. Por ultimo se llama al metrodo cargarTabCli para actualizar los datos de la interfaz.

        """
        try:
            modcliente = []
            cliente = [var.ui.txtDni, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]  # para recorrerlo
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbProv.currentText())
            modcliente.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHom.isChecked():
                modcliente.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                modcliente.append('Mujer')
            else:
                modcliente.append('No especificado')
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTargeta.isChecked():
                pagos.append('Targeta')
            pagos = set(pagos)  # evita duplicados
            modcliente.append(' ; '.join(pagos))
            valor = var.ui.spinEnvio.value()
            if valor == 0:
                modcliente.append('Recojida por cliente')
            if valor == 1:
                modcliente.append('Envio nacional Paqueteria Expres urgente')
            if valor == 2:
                modcliente.append('Envio nacional con paqueteria ordinario')
            if valor == 3:
                modcliente.append('Envio internacional')
            conexion.Conexion.modifCli(modcliente)
            conexion.Conexion.cargaTabCli(self)
        except Exception as error:
            print('Error en Modificar un cliente', error)
    def envio(self):
        """

        Modulo que muestra el tipo de envio segun el valor seleccionado en el spinEnvio

        """
        try:
          valor = var.ui.spinEnvio.value()
          if valor == 0:
              var.ui.lblEnvio.setText('Recojida por cliente')
          if valor == 1:
              var.ui.lblEnvio.setText('Envio nacional Paqueteria Expres urgente')
          if valor == 2:
            var.ui.lblEnvio.setText('Envio nacional con paqueteria ordinario')
          if valor == 3:
            var.ui.lblEnvio.setText('Envio internacional')

        except Exception as error:
            print('Error al imprimir ', error)