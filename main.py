import locale
import sys, var, events, locale
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog

import clients
import conexion
from windowaviso import *
from window import *
from windowcal import *

locale.setlocale(locale.LC_ALL, 'es-ES')

#hasta lo del dia anterior tiene que funcionar tal cual para que se corrija el examen
class fileDialogAbrir(QtWidgets.QFileDialog):
    '''Ventana abrir explorador windows'''

    def __init__(self):
        super(fileDialogAbrir, self).__init__()


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
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)  # Acciones del boton de Aceptar
        var.ui.btnLimpiar.clicked.connect(clients.Clientes.limpiaFormcli)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)  # SAlir del programa
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSex)   #Seleccion del sexo
        # var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)  #Seleccion del metodo de pago
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)

        '''
        Eventos de la barra de menus
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)  # Slair del programa por la barrita de arriba
        var.ui.actionAbrir.triggered.connect(events.Eventos.abrir)
        var.ui.actionCrear_Buckup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionImprimir.triggered.connect(events.Eventos.imprimir)

        '''
        Eventos de la caje de texto
        '''
        var.ui.txtDni.editingFinished.connect(clients.Clientes.validarDNI)  # Validar dni
        var.ui.txtApel.editingFinished.connect(clients.Clientes.mayus)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.mayus)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.mayus)

        '''
        Eventos  de comboBox
        '''
        var.ui.cmbProv.currentIndexChanged.connect(clients.Clientes.cargaMun)

        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        x = datetime.now()
        var.ui.lblFecha.setText(x.strftime(('%A, %d de %B de %Y')).title())

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
        '''Eventos del menu de herramientas'''

        var.ui.actionbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionbarAbrirCarpeta.triggered.connect(events.Eventos.abrir)
        var.ui.actionvarBackupCrear.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionvarBackupRestaurar.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionbarImprimir.triggered.connect(events.Eventos.imprimir)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = dialogCalendar()
    var.dlgabrir = fileDialogAbrir()
    window.show()
    sys.exit(app.exec())
