import os, var

from reportlab.pdfgen import canvas

class Informes():
    var.cv = canvas.Canvas('informes/ListadoClientes.pdf')  # Creación del lienzo de la plantilla
    def listadoClientes(self):
        try:

            Informes.cabecera(var.cv)

            var.cv.setFont('Helvetica-Bold', 8)
            var.cv.setTitle('Listado de Clientes')
            var.cv.setAuthor('Departamento de Administración')
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
        try:
            logo ='\\img\logo_empresa.png'
            var.cv.line(40,800,500,800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Direccion Avenida Galiza 102')
            var.cv.drawString(50, 740, 'Vigo - 123456 - Galiza')
            var.cv.drawString(50, 725, 'email: importexportVigo@gmail.com')
            #var.cv.drawImage(logo, 425,735)
            var.cv.line(40,710,500,710)



        except Exception as error:
            print('Error en cabezeca interna ', error)