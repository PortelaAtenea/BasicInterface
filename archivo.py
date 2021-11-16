from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import conexion
import var
import xlrd


class Archivo():
    def abrirArch(self):
        try:
            print("1")
            print("2")
            documento = xlrd.open_workbook(var.filexlsx)
            # clientesAr = documento.sheet_by_index(0)
            print("3")
            hoja = documento.sheet_by_index(0)
            print("4")
            print(hoja.nrows)
            print(hoja.ncols) #---> Tiene 6 columnas(Dni, nombre, apellidos, direcion provincia y sexo)
            print(hoja.cell_value(0, 0))#DNI
            print(hoja.cell_value(0, 1))#Nombre
            print(hoja.cell_value(0, 2))#Aplellidos

            # Creamos listas
            filas = []
            for fila in range(1, hoja.nrows):
                columnas = []
                for columna in range(0,6):
                    dato = []
                    columnas.append(hoja.cell_value(fila, columna))
                    Archivo.guardaCli(columnas)
                filas.append(columnas)
            print(filas)
        except Exception as e:
            print("Error en modulo abrir archivo: " + e)

    def guardaCli(columnas): #pasarle un array con las datos???
        try:
            conexion.Conexion.altaCli(columnas)  # graba en la tabla de la base de datos
            conexion.Conexion.cargaTabCli(columnas)  # reacrga la tabla

        except:
            print('Error en Guardar clientes desde excel')