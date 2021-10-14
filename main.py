import sys, var, events
from datetime import datetime

import clients
from windowaviso import *
from window import *
from windowcal import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class dialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''

        Ventana del calendario

        '''
        super(dialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(anoactual, mesactual, diaactual))
        #var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)



class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase de instancia para la ventana de aviso salir
        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de boton
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir) #SAlir del programa
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSex)   #Seleccion del sexo
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)  #Seleccion del metodo de pago

        '''
        Eventos de la barra de menus
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)  #Slair del programa por la barrita de arriba
        '''
        Eventos de la caje de texto
        '''
        var.ui.txtDni.editingFinished.connect(clients.Clientes.validarDNI)  #Validar dni
        '''
        Eventos  de comboBox
        '''
        clients.Clientes.cargaProv_(self)       #Cargar provincias en el combox
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)     #Seleccion de la provincia

        var.ui.cmbMuni.activated[str].connect(clients.Clientes.selMuni)     #Seleccion del municipio


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = dialogCalendar()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
