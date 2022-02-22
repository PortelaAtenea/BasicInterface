import unittest
import clients, conexion,var
from PyQt5 import QtSql

class MyTestCase(unittest.TestCase):
    def test_dni(self):
        dni = '39510218J'
        value = clients.Clientes.validarDNI(str(dni))
        msg = 'Proba erronea'
        self.assertTrue(value, msg)
    def test_conexion(self):
        value = conexion.Conexion.db_connect(var.filedb)
        msg = 'Conexion no valida'
        self.assertTrue(value, msg)
    def test_fact(self):
        valor = 40.03
        codFac = 1
        query1 = QtSql.QSqlQuery()
        query2 = QtSql.QSqlQuery()

        query1.prepare('select codventa, codarti, cantidad from ventas')
        self.assertTrue(value, msg)


if __name__ == '__main__':
    unittest.main()
