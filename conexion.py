from asyncio import wait
from datetime import datetime
import xlwt
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

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
                'insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio) '
                'VALUES (:dni, :alta, :apellidos, :nombre, :direcion, :provincia, :municipio, :sexo, :pago, :envio)')

            query.bindValue(':dni', str(newcli[0]))

            query.bindValue(':alta', str(newcli[1]))

            query.bindValue(':apellidos', str(newcli[2]))

            query.bindValue(':nombre', str(newcli[3]))

            query.bindValue(':direcion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            query.bindValue(':envio', str(newcli[9]))

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

            query.prepare("select direccion, provincia,municipio, sexo, envio from clientes where dni = :dni")
            query.bindValue(':dni', dni)

            if query.exec_():
                while query.next():
                    for i in range(5):
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
                          ' sexo =:sexo, pago =:pago, envio=:envio WHERE dni =:dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direcion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            query.bindValue(':envio', str(modcliente[9]))
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

    '''MODULOS DE GESTION DE BASES DE DATOS DE ARTICULOS / PRODUCTOS'''

    def altaArti(newArti):
        try:

            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into articulos (nombre, precio) '
                'VALUES (:nombre, :precio)')

            query.bindValue(':nombre', str(newArti[0]))
            query.bindValue(':precio', str(newArti[1]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('ARTICULO INSERTADO EN LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas con el nuevo cliente ', error)

    def cargaTabArti(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos order by codigo')
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabArti.setRowCount(index + 1)  # creamos la fila
                    # cargamos datos
                    var.ui.tabArti.setItem(index, 0, QTableWidgetItem(codigo))
                    var.ui.tabArti.setItem(index, 1, QTableWidgetItem(nombre))
                    var.ui.tabArti.setItem(index, 2, QTableWidgetItem(precio))
                    index += 1

        except Exception as error:
            print('Problemas al mostrar table clientes :(  ', error)
    def bajaArti( codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from articulos where codigo = :codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('ARTICULO DADO DE BAJA DE LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en baja de un articulo de la bd  ', error)
            return None

    def buscaArti(nombre):
        try:
            index = 0
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos where nombre = :nombre')
            query.bindValue(':nombre', str(nombre))
            #Limpiar la tabla
            #Colocar el articulo en la labla


            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabArti.setRowCount(index + 1)  # creamos la fila
                    # cargamos datos
                    var.ui.tabArti.setItem(index, 0, QTableWidgetItem(codigo))
                    var.ui.tabArti.setItem(index, 1, QTableWidgetItem(nombre))
                    var.ui.tabArti.setItem(index, 2, QTableWidgetItem(precio))
                    index += 1


            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
            return record
        except Exception as error:
            print('Error en baja de un articulo de la bd  ', error)
    def oneArti(codigo):

        try:
            record = []

            query = QtSql.QSqlQuery()

            query.prepare("select nombre, provincia,municipio, sexo, envio from clientes where dni = :dni")
            query.bindValue(':dni', codigo)

            if query.exec_():
                while query.next():
                    for i in range(5):
                        record.append(query.value(i))
            return record

        except Exception as error:
            print('Error en Cargar datos de un cliente de la bd  ', error)
            return None

    def modifArti(modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'UPDATE articulos SET nombre =:nombre, precio =:precio '
                ' WHERE codigo =:codigo')
            query.bindValue(':codigo', str(modcliente[0]))
            query.bindValue(':nombre', str(modcliente[1]))
            query.bindValue(':precio', str(modcliente[2]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('ARTICULO MODIFICADO EN LA BBDD CON EXITO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en modificar clientes (conexión) ', error)

    '''GESTION DE LA FACTURACION'''

    #Busca el clinete para la facturacion(nombre y aplledos) ------> Funciona bien
    def BuscaCliFac(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select apellidos, nombre from clientes where dni = :dni")
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(2):
                        registro.append(query.value(i))
            print(registro)
            return registro
        except Exception as error:
            print('Error en BUSCAR CLIENTE PARA FACTURAS(conexión) ', error)

    # Da de alta la factura el al tabla factura ------> Funciona bien
    def AltaFac(registro):
        try:

            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into facturas (dni, fecha) '
                'VALUES (:dni, :fecha)')
            query.bindValue(':dni', str(registro[0]))
            query.bindValue(':fecha', str(registro[1]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('FACTURA CREADA CON EXISTO')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en BUSCAR CLIENTE PARA FACTURAS(conexión) ', error)

    #Carga la los datos de la factura en la tabla -------> Funciona bien
    def cargaTabFac():

        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, fecha from facturas order by date(fecha) desc ')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    icopapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(24, 24)
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))
                    var.ui.tabFac.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFac.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tabFac.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFac.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFac.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index = index + 1


        except Exception as error:
            print('Error en carga listado facturas ', error)

    #Elimina la factura cuando le das al boton -------> No va(solo lo elimina cuando lo seleccionas primero)
    #todo
    def bajaFac():

        try:

            numfac = var.ui.lblNumFac.text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                Conexion.cargaTabFac()
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("La factura ha sido dada de baja")
                msgBox.setWindowTitle("Aviso")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

        except Exception as error:
            print('Error en dar baja factura(conexion)', error)

    #Busca el dni de una factura -------> Funciona Bien
    def buscaDNIFac(codigo):

        try:

            query = QtSql.QSqlQuery()

            query.prepare("select dni from facturas where codFac = :codigo")
            query.bindValue(':codigo', codigo)
            if query.exec_():
                while query.next():
                    record = str((query.value(0)))
            return record
        except Exception as error:
            print('Error en facturas en su sitio: :(  ', error)

    #Busca el nombre del cliente de una facura -------> Funciona Bien
    def buscaClifac(dni):

        try:

            query = QtSql.QSqlQuery()

            registro=[]
            query.prepare("select nombre , apellidos from clientes where dni = :dni")
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(2):
                        registro.append(str(query.value(i)))
            print(registro)
            return registro
        except Exception as error:
            print('Error en facturas en su sitio: :(  ', error)

    #Carga el precio del producto -------> No va
    #todo
    def CargarPrecioProd(prov):
        try:

            query = QtSql.QSqlQuery()
            query.prepare('SELECT precio FROM articulos WHERE nombre =:prov)')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    precio = str(query.value(0))
                    print(precio)
        except Exception as error:
            print('Error en lista municipios (conexión) ', error)

    #Carga el comboBox de la tabla con los productos -------> Funciona Bien
    def cargarCmbProducto(self):
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')
            query.prepare('select nombre from articulos order by nombre')
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))

        except Exception as error:
            print('Error en lista articulos (conexión) ', error)

    def cargarLineasVenta(codfac):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codventa,precio,cantidad from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codventa = query.value(0)
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codventa)))
                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    index = index + 1

        except Exception as error:
            print('error cargar las lines de factura', error)

    #Carga la venta cunado se le da al enter c en la tabla bventas -------> No Probado
    def CargarVenta(venta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into VENTAS (codFacFK,codProFK,precio,cantidad) '
                'VALUES (:codFac,:codPro,:precio,:cantidad)')
            query.bindValue(':codFac', int(venta[0]))
            query.bindValue(':codPro',  int(venta[1]))
            query.bindValue(':precio',  float(venta[2]))
            query.bindValue(':cantidad',  float(venta[3]))
            if query.exec_():
                var.ui.lblVenta.setText("Venta realizada")
            else:
                var.ui.lblVenta.setText("Venta NO realizada")
                var.ui.lblVenta.setStyleSheet('QLabel {color:red;}')

        except Exception as error:
            print('Error en Cargar venta (conexión.CargarVenta) ', error)

    #Busca El codigo de la factura(no se para que)-------> No Probado
    def buscaCodFac(self):
        try:
            dato =''
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from facturas order by codigo desc limit 1')
            if query.exec_():
                while query.next():
                    dato = query.value(0)
            else:
                var.ui.lblVenta.setText("Venta NO realizada")
                var.ui.lblVenta.setStyleSheet('QLabel {color:red;}')
            return dato
        except Exception as error:
            print('Error en Obtener codigo Factura (conexión.buscaCodFac) ', error)






