from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import var


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

    def cargaTabCli(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, alta, pago from clientes order by apellidos, nombre')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tabClientes.setRowCount(index+1) #creamos la fila
                    #cargamos datos
                    var.ui.tabClientes.setItem(index, 0, QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QTableWidgetItem(pago))
                    index+=1

        except Exception as error:
            print('Problemas al mostrar table clientes :(  ', error)

    def oneClie(dni):

        try:
            record = []

            query = QtSql.QSqlQuery()

            query.prepare("select direccion, provincia,municipio, sexo from clientes where dni = :dni")
            query.bindValue(':dni', dni)

            if query.exec_():
                while query.next():
                    for i in range(4):
                        record.append(query.value(i))
            return record

        except Exception as error:
            print('Error en Cargar datos de un cliente de la bd  ', error)
            return None


    def bajaCli( dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('CLIENTE DADO DE BAJA DE LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en baja de un cliente de la bd  ', error)
            return None

    def listaMunicipios(prov):
        municipios = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT municipio FROM municipios WHERE provincia_id = (SELECT id FROM provincias WHERE provincia =:prov)')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    municipios.append(query.value(0))
        except Exception as error:
            print('Error en lista municipios (conexión) ', error)
        return municipios

    def listaProvincias(self):
        provincias = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT provincia FROM provincias')
            if query.exec_():
                while query.next():
                    provincias.append(query.value(0))
        except Exception as error:
            print('Error en lista municipios (conexión) ', error)
        return provincias
