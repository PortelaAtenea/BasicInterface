
- crear un boton(imaghen) para buscar al lado del reecargar en ambor modulos
- la tabla tien  que ser amplia para poder verla bien pero con ceherenca  con el resto


##Modulo Articulos

* codigo y precio en tabla ajustado al contenido, en nombre que noja el resto
* color rojo el codigo
* arregalr el coso del precio:
  * si es con coma o con punto da igual, se peude guardar igual pero cse cambia igual al qeu es correcto: --> precio = precio.remplace(',', ''.')????Mas o meneso, creo
  * tine que poder poner la current moneda del --- > precio = locale.currency(float(precio))
  * en la base de datos se guarda como texto porque va con en € 
  * cuando se cojen los datos de los precios se quita el€ y se cambia la , por el .
  * 
  * 

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