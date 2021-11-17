from datetime import datetime

from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import csv
import conexion
import var
import xlrd
import xlwt

class Archivo():
    def ImportarExcel(self):
        try:
            newcli = []
            contador = 0
            option = QtWidgets.QFileDialog.Options()
            ruta_excel = var.dlgabrir.getOpenFileName(None, 'Elija archivo para importar Excel', '', '*.xls', options=option)
            if var.dlgabrir.Accepted and ruta_excel != '':
                fichero = ruta_excel[0]
            workbook = xlrd.open_workbook(fichero)
            hoja = workbook.sheet_by_index(0)
            while contador < hoja.nrows:
                for i in range(6):
                    newcli.append(hoja.cell_value(contador + 1, i))
                conexion.Conexion.altaCliEx(newcli)
                conexion.Conexion.cargaTabCli(newcli)
                newcli.clear()
                contador = contador + 1
        except Exception as error:
            print('Error al importar ', error)


    def ExportarDatos(self):
        try:
            conexion.Conexion.exportEx(self)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Datos exportados con éxito.")
                msgBox.setWindowTitle("Operación completada")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje generado exportar datos ', error)
        except Exception as error:
            print('Error en evento exportar datos ',error)

'''Mi version de las cosas --> Spoiler: Van mal'''
'''
    def abrirArch(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getSaveFileName(None, 'Importar Datos', '', '*.xls;All Files',
                                                                options=option)
            if var.dlgabrir.Accepted and filename != '':
                documento = xlrd.open_workbook(filename)
                hoja = documento.sheet_by_index(0)
                filas = []
                for fila in range(1, hoja.nrows):
                    columnas = []
                    for columna in range(0, 6):
                        dato = []
                        columnas.append(hoja.cell_value(fila, columna))
                        Archivo.guardaCli(columnas)
                    filas.append(columnas)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('EXITO!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('La base de datos ha sido creada con exito!!')
                msg.exec()
        except Exception as e:
            print("Error en modulo abrir archivo: " + e)

    def guardaCli(columnas): #pasarle un array con las datos???
        try:
            conexion.Conexion.altaCliFichero(columnas)  # graba en la tabla de la base de datos
            conexion.Conexion.cargaTabCli(columnas)  # reacrga la tabla

        except:
            print('Error en Guardar clientes desde excel')
    
    def enviarArchivo(self):
        try:
            i = 0
            lista = []
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.archivoDatos = (str(fecha) + '_datos.xls')
            print(var.archivoDatos)

            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos', '', '*.xls;All Files', options=option)
            if var.dlgabrir.Accepted and filename != '':
                documento = xlwt.Workbook(var.archivoDatos)
                hoja = documento.add_sheet("Clientes")
                hoja.write(i, 0, "Dni")
                hoja.write(i, 1, "Alta")
                hoja.write(i, 2, "Apellido")
                hoja.write(i, 3, "Nombre")
                hoja.write(i, 4, "Direccion")
                hoja.write(i, 5, "Provincia")
                hoja.write(i, 6, "Municipio")
                hoja.write(i, 7, "Sexo")
                hoja.write(i, 8, "Pagos")
                i =+1
                conexion.Conexion.listaCli(i, hoja)
                #Hay que tener cuidado con los nullos
                documento.save(var.archivoDatos)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('EXITO!!!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('La base de datos ha sido creada con exito!!')
                msg.exec()

        except Exception as error:
            print("Error en modulo enviar datos al archivo: " + error)

    def enviarCliente(record, i, hoja):
        try:
            for columna in range(0, 6):
                hoja.write(i, columna, record[columna])

        except Exception as error:''''''
            print("Error en modulo enviar datos al archivo: " + error)
'''