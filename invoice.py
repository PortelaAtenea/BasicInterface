'''Gestion de facturas'''
import conexion
import var
import window
class Facturas:
    def buscaCli(self):
        try:
            dni = var.ui.txtDniFac.text().upper()
            print(dni)
            registro = conexion.Conexion.BuscaCliFac(dni)

            nombre = registro[0] + ', ' +registro[1]
            var.ui.lblNombreApel.setText(nombre)
            var.ui.txtDniFac.setText(dni)
        except Exception as e:
            print('Eror en Buascar cliente en facturas.:    ',e)


    def fecha(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ', error)


    def altaFac(self):
        try:
            registro = []
            dni = var.ui.txtDniFac.text().upper()
            registro.append(str(dni))
            var.ui.txtDniFac.setText(dni)
            fecha = var.ui.txtFechaFac.text()
            registro.append(str(fecha))
            print(registro)
            registro = conexion.Conexion.AltaFac(registro)


        except Exception as error:
            print('Error al dar de alta un calendario ', error)


    def cargaFac(self):
        try:
            valor = 0
            #Facturas.limpiaFormFac(self)
            fila = var.ui.tabFac.selectedItems()  # seleciona la fila
            datos = [var.ui.lblNumFac, var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            var.ui.lblNumFac.setText(row[0])
            var.ui.txtFechaFac.setText(row[1])
        except Exception as error:
            print('Error en Cargar datos de Facturas', error)
            return None
