
- crear un boton(imaghen) para buscar al lado del reecargar en ambor modulos
- la tabla tien  que ser amplia para poder verla bien pero con ceherenca  con el resto


# Posibles ejercicios del examen



-El programa funciona 
-3 mejoras con distintos apastados
-1 hora por mejora
-la documentacion tien eque estar hecha
-ejecutable
-el exe es necesario(como minimo)(es previo a la mejora del exemen)
-

https://github.com/XoanCarlos?tab=repositories

##Modulo Articulos

[* codi*go y precio en tabla ajustado al contenido, en nombre que noja el resto
* color rojo el codigo   --> hecho
* arregalr el coso del precio:
  * si es con coma o con punto da igual, se peude guardar igual pero cse cambia igual al qeu es correcto: --> precio = precio.remplace(',', ''.')????Mas o meneso, creo
  * tine que poder poner la current moneda del --- > precio = locale.currency(float(precio))
  * en la base de datos se guarda como texto porque va con en € 
  * cuando se cojen los datos de los precios se quita el€ y se cambia la , por el .
  ** 
  * 
]()
##Informes

* poner imagen
* no me va el forma de pagos

##Tabla Facturas
* Poner cosas en la tabla
* Que al 
* Boton de eliminar ventas
* subtotal, iva, total _-Abajo

##BBDD
* falta poner los delete on cascade en codFactura y dni cleinte

##Ejemplo de examen posible:
  * adaptacion de codigo a cosas DIFERENTES
  * Eleccion de campos que quieres incluir en el informe
  * nuevos campos de busqueda

##Arreghlar lo que falta de los dias que fralte en abrir:
  * dar de alta proveedores
  * tavka como con los clientes que pone la informacion c
  * unado clicas en la tabla en los cosas de arriba
  * 








from img import basura
from img import calendar
from img import abrirCarpeta
from img import crearBackup
from img import impresion
from img import limpiar
from img import lupa
from img import restaurarBackup
from img import salir
from img import verPdf






Error en Cargar la linea de venta(Invoice.Facturas.CargarLineaVenta):    
arguments did not match any overloaded call:
  setFixedSize(self, QSize): first argument of unbound method must have type 'QWidget'
  setFixedSize(self, int, int): first argument of unbound method must have type 'QWidget'
Error en Cargar la linea de venta(Invoice.Facturas.processVenta):    currentText(self): first argument of unbound method must have type 'QComboBox'
Conexion establecida
Error en Cargar la linea de venta(Invoice.Facturas.CargarLineaVenta):    arguments did not match any overloaded call:
  setFixedSize(self, QSize): first argument of unbound method must have type 'QWidget'
  setFixedSize(self, int, int): first argument of unbound method must have type 'QWidget'
Error en Borrar Venta Factura (conexión.delVentaFac)  invalid literal for int() with base 10: ''
Error en dar baja factura(conexion) invalid literal for int() with base 10: ''