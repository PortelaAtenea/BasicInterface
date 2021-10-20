''''
Funciones  gestion de clientes
'''
from tkinter import Label

from PyQt5.QtWidgets import QMessageBox

from window import *
import var

class Clientes():
    def validarDNI():
        try:
            global validodni
            validodni = False
            dni = var.ui.txtDni.text()              #Sea lo que sea que hayya en una caja de texto de la interfaz(float, int String) el lo va a cojer siempre como un string
            var.ui.txtDni.setText(dni)
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'       #lETRAS DEL DNI
            dig_ext = 'XYZ'                         #Letra Dni extrangero
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'} #rEEMPLAZAR EL IGITO POR LA LETRA EXTRANGERA. #ES UN  DICCIONARIO
            numeros= '1234567890'
            dni = dni.upper()                        #convierte la letra en mayuscula
            if len(dni) == 9:                       # si la longitud es igual a 9
                dig_control = dni[8]                 #
                dni = dni[:8]                       #Tomo elnumero de los 8 primeros
                if dni[0] in dig_ext:
                    dni = dni.remplace(dni[0], reemp_dig_ext[dni[0]])
                    print('Correcto')
                    validodni = True # lo pongo a true

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValidoDni.setText('Valido')

                    print('Correcto')
                    validodni = True

                    var.ui.txtDni.setStyleSheet('background-color: green;')
                else:
                    print('Incorrecto')

                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValidoDni.setText('X')
                    var.ui.txtDni.setStyleSheet('background-color: pink;')
            else:
                print('Incorrecto')

                var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidoDni.setText('X')
                var.ui.txtDni.setStyleSheet('background-color: pink;')

        except:
            print('Error en la aplicacion')
            return None
    def selSex(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado Femenino :)')
            if var.ui.rbtHom.isChecked():
                print('Marcado Masculino :(')
        except Exception as error:
            print('Error en Modulo Sex')
    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Ha Selecionado efectivo')
            if var.ui.chkTargeta.isChecked():
                print('Ha Selecionado Targeta')
            if var.ui.chkTransfe.isChecked():
                print('Ha Selecionado Transferencia')
            if var.ui.chkCargoCuenta.isChecked():
                print('Ha Selecionado Cargo a cuenta')

        except Exception as error:
            print('Error en modulo Seleccionar modo de pago')
    def cargaProv_(self):
        try:
            var.ui.cmbProv.clear()
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en cargar la lista', error)
    def selProv(prov):
        try:
            print('Has seleccionado la provincia: ', prov)
            return prov;
        except Exception as error:
            print('Error en seleccion provincia', error)
    def cargaMuni_(self):
        try:
            var.ui.cmbProv.clear()
            muniPonte = ['', 'Moaña', 'Vigo', 'Redondela', 'Cangas', 'Bueu']
            muniCoru = ['', 'Moaña', 'Vigo', 'Redondela', 'Cangas', 'Bueu']
            muniOu = ['', 'Moaña', 'Vigo', 'Redondela', 'Cangas', 'Bueu']
            muniLugo = ['', 'Moaña', 'Vigo', 'Redondela', 'Cangas', 'Bueu']

            for i in muniPonte:
                var.ui.cmbMuni.addItem(i)

        except Exception as error:
            print('Error en cargar la lista', error)
    def selMuni(muni):
        try:
            print('Has seleccionado el municipio: ', muni)
            return muni;
        except Exception as error:
            print('Error en seleccion municipio', error)

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en cargar fecha del calendario', error)
    def mayus():
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
        try:
            # preparamos el registro
            newcli = []  # para la base de datos
            tabClie = [] # para la tableWidget
            client = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            # codigo para cargar en la table
            for i in client:
                tabClie.append(i.text())
            #cargar los radiobuttons
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTargeta.isChecked():
                pagos.append('Targeta')
            pagos = set(pagos) #evita duplicados
            tabClie.append(' ; '.join(pagos))
            # Cargamos en la tabla

            if validodni: # la global
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)
                for campo in tabClie:
                    cell = QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row, column, cell)
                    column += 1
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('dni no valido')
                msg.exec()
                #colocar ventana de aviso por codigo --> qtwidgets.qmessagebox python
        except:
            print('Error en Guardar clientes')
            return None
    def limpiaFormcli(self):
        try:
            var.ui.txtApel.setText("")
            var.ui.txtDni.setText("")
            var.ui.txtAltaCli.setText("")
            var.ui.txtNome.setText("")
            var.ui.txtDir.setText("")
            cajas = [var.ui.txtApel,var.ui.txtNome,  var.ui.txtDni,var.ui.txtAltaCli,var.ui.txtDir]
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