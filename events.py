'''

fichero de eventos generales(eventos que no tienen relacion directa con ningun otro archivo(salir del programa, etc))


'''
import sys, var


class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec_():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en modulo salir ', error)