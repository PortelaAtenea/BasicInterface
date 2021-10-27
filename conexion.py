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

    def altaCli(newcli):
        try:

            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago) '
                'VALUES (:dni, :alta, :apellidos, :nombre, :direcion, :provincia, :municipio, :sexo, :pago)')

            query.bindValue(':dni', str(newcli[0]))

            query.bindValue(':alta', str(newcli[1]))

            query.bindValue(':apellidos', str(newcli[2]))

            query.bindValue(':nombre', str(newcli[3]))

            query.bindValue(':direcion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('CLIENTE INSERTADO EN LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas con el nuevo cliente ', error)
