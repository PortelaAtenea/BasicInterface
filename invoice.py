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
            var.ui.txtCliFac.setText(nombre)
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
            print('Error al abrir el calendario ', error)
