''''
Funciones  gestion de clientes
'''
from window import *
import var

class Clientes():
    def validarDNI():
        try:
            dni = var.ui.txtDni.text()              #Sea lo que sea que hayya en una caja de texto de la interfaz(float, int String) el lo va a cojer siempre como un string
            var.ui.txtDni.setText(dni)
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'       #lETRAS DEL DNI
            dig_ext = 'XYZ'                         #Letra Dni extrangero
            reemp_dig_ext = {'X': '0','Y': '1', 'Z': '2'} #rEEMPLAZAR EL IGITO POR LA LETRA EXTRANGERA. #ES UN  DICCIONARIO
            numeros= '1234567890'
            dni = dni.upper()                        #convierte la letra en mayuscula
            if len(dni) == 9:                       # si la longitud es igual a 9
                dig_control = dni[8]                 #
                dni = dni[:8]                       #Tomo elnumero de los 8 primeros
                if dni[0] in dig_ext:
                    dni = dni.remplace(dni[0],reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValidoDni.setText('V')
                    print('Correcto')
                else:
                    print('Incorrecto')
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValidoDni.setText('X')
            else:
                print('Incorrecto')
                var.ui.lblValidoDni.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidoDni.setText('X')

        except:
            print('Error en la aplicacion')
            return None
