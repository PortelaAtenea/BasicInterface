from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets

class Conexion():
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,
                'No se puede abrir la bbdd.\n''Haz click para continuar',
                        QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexion establecida')
                return True
        except Exception as error:
            print('Problemas en la conexion ', error)
'''MODULOS GESTION BASE DE DATOS CLIENTES'''
'''def altaCli(newcli):
        try:
           pass
        except Exception as error:
            print('Problemas con el nuevo cliente ', error)'''