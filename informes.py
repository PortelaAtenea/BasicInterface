import os, var
from datetime import datetime

from PyQt5 import QtSql
from reportlab.pdfgen import canvas

import conexion


class Informes():
    var.cv = canvas.Canvas('informes/ListadoClientes.pdf')  # Creación del lienzo de la plantilla
    def listadoClientes(self):
        """

        Metodo que imprime en el informwe todos los clientes. Lalama al emtodo cabecera para poder imprimir la cabecera en todas las hioojas del pdf

        """
        try:

            Informes.cabecera(var.cv)

            var.cv.setFont('Helvetica-Bold', size = 9)
            #Se guardan estos datos internamente
            var.cv.setTitle('Listado de Clientes')
            var.cv.setAuthor('Departamento de Administración')
            #Titulo
            textoTitulo = 'LISTADO CLIENTES'
            Informes.pie(textoTitulo)
            var.cv.drawString(255,690, textoTitulo)
            var.cv.line(40,685,530,685)
            items = ['DNI', 'Nombre','Formas de pago' ] #Cabezera de la tabla
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(350, 675, items[2])
            var.cv.line(40,670,530,670)
            var.cv.setFont('Helvetica', size=8)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pago from clientes order by apellidos, nombre')
            if query.exec_():
                i = 50
                j = 655     # i = x, j= y
                while query.next():
                    if j <=80:
                        var.cv.drawString(460,30,'Pagina siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(var.cv)
                        var.cv.drawString(255, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de pago']  # Cabezera de la tabla
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(350, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        Informes.pie(textoTitulo)
                        i = 50
                        j = 655  # i = x, j= y
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i,j,str(query.value(0)))
                    var.cv.drawString(i + 140, j, str(query.value(1)+', '+query.value(2)))
                    print(str(query.value(3)))
                    print(query.value(3))
                    var.cv.drawString(i + 300, j, str(query.value(3)))

                    j = j-20

            var.cv.save()#guardado de la plantilla

            rootPath = '.\\informes'
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1


        except Exception as error:
            print('Error al emitir el listado de clientes ', error)
    def cabecera(self):
        """

        Metodo qeu imprime la cabecera en el pdf

        """
        try:
            logo ='\\img\logo_empresa.png'
            var.cv.line(40,800,530,800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Direccion Avenida Galiza 102')
            var.cv.drawString(50, 740, 'Vigo - 123456 - Galiza')
            var.cv.drawString(50, 725, 'email: importexportVigo@gmail.com')
            #var.cv.drawImage(logo, 425,735)
            var.cv.line(40,710,530,710)



        except Exception as error:
            print('Error en cabezeca interna ', error)

    def pie(texto):
        """

        Metodo qeu imprime el pie de pagina en el pdf

        """
        try:

            var.cv.line(50, 50, 530, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y   %H.%M.%S')
            var.cv.setFont('Helvetica', size = 6)
            var.cv.drawString(70, 40, str(fecha))
            var.cv.drawString(255, 40, texto)
            var.cv.drawString(500, 40, str('Pagina %s' %var.cv.getPageNumber()))



        except Exception as error:
            print('Error en creacion de pie de informe clientes ', error)

    def factura(self):
        """

        Metodo que imprime en el pdf de facturas, todas las facturas de la bbdd. Tambien llama a los metodos cabecera y pie de esta clase

        """
        try:
            var.cv = canvas.Canvas('informes/factura.pdf')
            var.cv.setTitle('Factura')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=12)

            textotitulo = 'FACTURA'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            codfac = var.ui.lblNumfac.text()

            var.cv.drawString(260, 694, textotitulo + ': ' + (str(codfac)))
            var.cv.line(30, 685, 550, 685)

            var.cv.drawString(180,790,'CIF: '+ var.ui.txtDniFac.text())
            var.cv.drawString(180,790,'Nombre: '+ var.ui.txtNombreFac.text())
            items = ['Venta', 'Articulo', 'Precio', 'Cantidad', 'Total']
            var.cv.drawString(65, 673, items[0])
            var.cv.drawString(165, 673, items[1])
            var.cv.drawString(270, 673, items[2])
            var.cv.drawString(380, 673, items[3])
            var.cv.drawString(490, 673, items[4])
            suma = 0.0
            query = QtSql.QSqlQuery()
            query.prepare('select codven,precio,cantidad,codpro from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    codventa = query.value(0)
                    precio = query.value(1)
                    cantidad = query.value(2)
                    nombre = conexion.Conexion.buscaArt(int(query.value(3)))
                    total = round(precio * cantidad, 2)
                    suma += total
                    var.cv.setFont('Helvetica', size=9)
                    var.cv.drawString(i + 20, j, str(query.value(0)))
                    var.cv.drawString(i + 100, j, str(nombre))
                    var.cv.drawString(i + 219, j, str(precio) + '€/kg')
                    var.cv.drawString(i + 340, j, str(cantidad))
                    var.cv.drawString(i + 442, j, str(total))
                    j = j - 20
            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error creación informe facturas', error)