---
title: Trabajar con Filas y Columnas GridWeb
type: docs
weight: 20
url: /es/java/working-with-rows-and-columns-gridweb/
---

## **Inserción de Filas y Columnas**
Este tema explica cómo insertar nuevas filas y columnas en una hoja de cálculo utilizando la API Aspose.Cells.GridWeb. Las filas o columnas se pueden insertar en cualquier posición de la hoja de cálculo.
### **Inserción de Filas**
Para insertar una fila en cualquier posición de una hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb al formulario web o página.
1. Acceda a la hoja de cálculo a la que está agregando filas.
1. Inserte una fila especificando un índice de fila donde se insertará la fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Inserción de Columnas**
Para insertar una columna en cualquier posición de una hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web o página.
1. Acceda a la hoja de cálculo a la que está agregando columnas.
1. Inserte una columna especificando el índice de columna donde se insertará la columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

También puede usar los métodos insertRows()/insertColumns() para insertar múltiples filas/columnas en las hojas de cálculo correspondientemente.

{{% /alert %}} 
## **Eliminación de Filas y Columnas**
Este tema demuestra cómo eliminar filas y columnas de una hoja de cálculo utilizando la API Aspose.Cells.GridWeb. Con la ayuda de esta función, los desarrolladores pueden eliminar filas o columnas en tiempo de ejecución.
### **Eliminación de Filas**
Para eliminar una fila de su hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web o página.
1. Acceda a la hoja de cálculo de la que desea eliminar filas.
1. Elimine una fila de la hoja de cálculo especificando su índice de fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Eliminando columnas**
Para eliminar una columna de su hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web o página.
1. Acceda a la hoja de cálculo de la que desea eliminar columnas.
1. Elimine una columna de la hoja de cálculo especificando su índice de columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Configuración de la altura de fila y ancho de columna**
A veces los valores de las celdas son más anchos que la celda en la que se encuentran o están en varias líneas. Tales valores no son totalmente visibles para los usuarios a menos que cambien la altura y el ancho de las filas y columnas. Aspose.Cells.GridWeb admite completamente la configuración de la altura de las filas y el ancho de las columnas. Este tema discute estas características en detalle con la ayuda de ejemplos.
### **Trabajando con la altura de las filas y el ancho de las columnas**
#### **Configuración de la altura de fila**
Para configurar la altura de una fila:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección de cuadrículas de la hoja de trabajo.
1. Establezca la altura de todas las celdas en una fila especificada.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb acepta medidas de altura de fila y ancho de columna en puntos, pulgadas, píxeles, etc.

{{% /alert %}} 

**Salida: la altura de la primera fila se ha configurado en 50 puntos** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Configuración del ancho de columna**
Para establecer el ancho de una columna:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección de cuadrículas de la hoja de trabajo.
1. Establezca el ancho de todas las celdas en una columna específica.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personalización de encabezados de fila y columna**
Al igual que Microsoft Excel, Aspose.Cells.GridWeb también utiliza encabezados o títulos estándar para las filas (números como 1, 2, 3, etc.) y columnas (alfabéticos como A, B, C, etc.). Aspose.Cells.GridWeb también permite personalizar los títulos. Este tema trata sobre la personalización de encabezados de fila y columna en tiempo de ejecución utilizando la API Aspose.Cells.GridWeb.
### **Personalización de encabezado de fila**
Para personalizar el encabezado o título de una fila:

1. Agregar el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en la colección de hojas de cálculo de la cuadrícula.
1. Establezca el título de una fila específica.

**Se han personalizado los encabezados de la fila 1 y 2** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personalización de encabezado de columna**
Para personalizar el encabezado o título de una columna:

1. Agregar el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en la colección de hojas de cálculo de la cuadrícula.
1. Establezca el título de una columna específica.

**Se han personalizado los encabezados de la columna 1 y 2** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Congelar y descongelar filas y columnas**
Este tema explica cómo congelar y descongelar filas y columnas. Congelar columnas o filas permite a los usuarios mantener visibles los encabezados de columna o los títulos de fila mientras se desplazan a otras partes de la hoja de trabajo. Esta función es muy útil al trabajar con hojas de cálculo que contienen grandes volúmenes de datos. Cuando los usuarios se desplazan, solo los datos se desplazan hacia abajo y los encabezados permanecen en su lugar, facilitando la lectura de los datos. La función de paneles de congelación solo es compatible con Internet Explorer 6.0 o superior.
### **Congelar filas y columnas**
Para congelar un número específico de filas y columnas:

1. Agregar el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceder a una hoja de cálculo.
1. Congelar un número de filas y columnas.

{{% alert color="primary" %}} 

También es posible congelar un número específico de filas y columnas usando la interfaz. Haga clic derecho en una celda donde desea congelar filas y columnas y seleccione **Congelar** de la lista.

{{% /alert %}} 

**Filas y columnas en un estado congelado** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Descongelar filas y columnas**
Para descongelar filas y columnas:

1. Agregar el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceder a una hoja de cálculo.
1. Descongelar filas y columnas.

**Hoja de cálculo después de ser descongelada** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Proteger filas y columnas**
Este tema discute algunas técnicas para proteger celdas en filas y columnas de cualquier tipo de acción realizada por los usuarios finales. Los desarrolladores pueden implementar esta protección usando dos técnicas: haciendo que las celdas en filas y columnas sean de solo lectura, o restringiendo las opciones del menú contextual de GridWeb.
### **Restricción de las opciones del menú contextual**
GridWeb proporciona un menú contextual que los usuarios finales pueden utilizar para realizar operaciones en el control. El menú proporciona muchas opciones para manipular celdas, filas y columnas.

**Opciones contextuales completas** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Es posible restringir cualquier tipo de operaciones del lado del cliente en filas y columnas al restringir las opciones disponibles en el menú contextual. Se puede hacer configurando los atributos EnableClientColumnOperations y EnableClientRowOperations del control GridWeb como false. También es posible impedir que los usuarios congelen filas y columnas configurando el atributo EnableClientFreeze del control GridWeb como false.

**Menú contextual después de restringir las opciones de filas y columnas** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
