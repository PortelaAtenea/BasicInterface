import sys, var, events
from datetime import datetime

import clients
import conexion
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
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)



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

        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli) #Acciones del boton de Aceptar
        var.ui.btnLimpiar.clicked.connect(clients.Clientes.limpiaFormcli)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir) #SAlir del programa
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSex)   #Seleccion del sexo
        # var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)  #Seleccion del metodo de pago
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)



        '''
        Eventos de la barra de menus
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)  #Slair del programa por la barrita de arriba
        '''
        Eventos de la caje de texto
        '''
        var.ui.txtDni.editingFinished.connect(clients.Clientes.validarDNI)  #Validar dni
        var.ui.txtApel.editingFinished.connect(clients.Clientes.mayus)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.mayus)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.mayus)
        '''
        Eventos  de comboBox
        '''

        var.ui.cmbProv.currentIndexChanged.connect(clients.Clientes.cargaMun)
        '''
        Eventos QTabWidget
        '''

        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        '''
        Eventos de la bbdd
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli(self)
        clients.Clientes.cargaProv(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width())//2
    y = (desktop.height() - window.height())//2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = dialogCalendar()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/