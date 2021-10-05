'''

fichero de eventos generales(eventos que no tienen relacion directa con ningun otro archivo(salir del programa, etc))


'''
import sys

import var


class Eventos():
    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('Error en modulo salir ', error)