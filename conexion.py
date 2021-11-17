from datetime import datetime

import xlwt
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import archivo
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
            print('Error en lista provincias (conexión) ', error)
        return provincias


    def modifCli( modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE clientes SET alta =:alta, apellidos =:apellidos, nombre =:nombre, direccion =:direcion, provincia =:provincia, municipio =:municipio, '
                          ' sexo =:sexo, pago =:pago WHERE dni =:dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direcion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('CLIENTE MODIFICADO EN LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en modificar clientes (conexión) ', error)

    def altaCliEx(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo) VALUES '
                          '(:dni, :apellidos, :nombre, :direccion, :provincia, :sexo)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':apellidos', str(newcli[1]))
            query.bindValue(':nombre', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':sexo', str(newcli[5]))

            if query.exec_():
                print('Inserción correcta')

            else:
                print('Inserción No correcta')
        except Exception as error:
            print('Problemas alta cliente',error)

    def exportEx(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls',
                                                                options=option)
            wb = xlwt.Workbook()
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'ALTA')
            sheet1.write(0, 2, 'APELIDOS')
            sheet1.write(0, 3, 'NOME')
            sheet1.write(0, 4, 'DIRECCION')
            sheet1.write(0, 5, 'PROVINCIA')
            sheet1.write(0, 6, 'MUNICIPIO')
            sheet1.write(0, 7, 'SEXO')
            sheet1.write(0, 8, 'PAGO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    for c in range(9):
                        sheet1.write(f, c, query.value(c))
                    f += 1
            wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ', error)
'''
    def altaCliFichero(newcli):
        try:

            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo) '
                'VALUES (:dni, :apellidos, :nombre, :direcion, :provincia, :sexo)')

            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':apellidos', str(newcli[1]))
            query.bindValue(':nombre', str(newcli[2]))
            query.bindValue(':direcion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':sexo', str(newcli[5]))

            if query.exec_():
                print("Cliente insertado")
            else:
               print('Error al insertar el cliente: '+query.lastError().text())
        except Exception as error:
            print('Problemas con el nuevo cliente ', error)

    def listaCli(i, hoja):

        try:
            record = []
            index = 0
            query = QtSql.QSqlQuery()
            print('1')
            query.prepare("select dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pagos from clientes")
            print(query.exec_())
            if query.exec_():
                print('1')
                while query.next():
                    print('1')
                    dni = query.value(0)
                    record.append(dni)
                    alta = query.value(1)
                    record.append(alta)
                    apellidos = query.value(2)
                    record.append(apellidos)
                    nombre = query.value(3)
                    record.append(nombre)
                    direccion = query.value(4)
                    record.append(direccion)
                    provincia = query.value(5)
                    record.append(provincia)
                    municipio = query.value(6)
                    record.append(municipio)
                    sexo = query.value(7)
                    record.append(sexo)
                    pago = query.value(8)
                    record.append(pago)
                    archivo.Archivo.enviarCliente(record, i, hoja)
                    # cargamos datos
                    index += 1
            if query.exec_():
                while query.next():
                    for i in range(6):
                        record.append(query.value(i))
            return record

        except Exception as error:
            print('Error en Cargar datos de un cliente de la bd  ', error)'''
''' return None'''