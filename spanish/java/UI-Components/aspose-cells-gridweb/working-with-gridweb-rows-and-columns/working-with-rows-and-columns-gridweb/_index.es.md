---
title: Trabajar con filas y columnas GridWeb
type: docs
weight: 20
url: /es/java/working-with-rows-and-columns-gridweb/
---
##  **Insertar filas y columnas**
Este tema explica cómo insertar nuevas filas y columnas en una hoja de trabajo usando Aspose.Cells.GridWeb API. Se pueden insertar filas o columnas en cualquier posición de la hoja de trabajo.
###  **Insertar filas**
Para insertar una fila en cualquier posición de una hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb al formulario o página web.
1. Acceda a la hoja de trabajo a la que está agregando filas.
1. Inserte una fila especificando un índice de fila donde se insertaría la fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **Insertar columnas**
Para insertar una columna en cualquier posición de una hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo a la que está agregando columnas.
1. Inserte una columna especificando el índice de la columna donde se insertaría la columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

También puede utilizar los métodos insertRows()/insertColumns() para insertar varias filas/columnas en las hojas de trabajo en consecuencia.

{{% /alert %}} 
##  **Eliminar filas y columnas**
Este tema muestra cómo eliminar filas y columnas de una hoja de cálculo utilizando Aspose.Cells.GridWeb API. Con la ayuda de esta función, los desarrolladores pueden eliminar filas o columnas en tiempo de ejecución.
###  **Eliminar filas**
Para eliminar una fila de su hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo de la que desea eliminar filas.
1. Elimine una fila de la hoja de trabajo especificando su índice de fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **Eliminar columnas**
Para eliminar una columna de su hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo de la que desea eliminar columnas.
1. Elimine una columna de la hoja de trabajo especificando su índice de columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **Configuración de la altura de fila y el ancho de columna**
A veces, los valores de las celdas son más anchos que la celda en la que se encuentran o están en varias líneas. Dichos valores no son completamente visibles para los usuarios a menos que cambien la altura y el ancho de las filas y columnas. Aspose.Cells.GridWeb admite totalmente la configuración de alturas de fila y ancho de columna. En este tema se analizan estas características en detalle con la ayuda de ejemplos.
###  **Trabajar con alturas de fila y ancho de columna**
####  **Configuración de la altura de la fila**
Para establecer la altura de una fila:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección GridCells de la hoja de trabajo.
1. Establezca la altura de todas las celdas en cualquier fila especificada.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb acepta medidas de alto de fila y ancho de columna en puntos, pulgadas, píxeles, etc.

{{% /alert %}} 

**Salida: la altura de la primera fila se ha establecido en 50 puntos** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **Configuración del ancho de columna**
Para establecer el ancho de una columna:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección GridCells de la hoja de trabajo.
1. Establezca el ancho de todas las celdas en cualquier columna especificada.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **Personalización de encabezados de filas y columnas**
Al igual que Microsoft Excel, Aspose.Cells.GridWeb también utiliza encabezados o títulos estándar para filas (números como 1, 2, 3, etc.) y columnas (alfabéticas como A, B, C, etc.). Aspose.Cells.GridWeb también permite personalizar los subtítulos. En este tema se analiza la personalización de encabezados de filas y columnas en tiempo de ejecución utilizando Aspose.Cells.GridWeb API.
###  **Personalización del encabezado de fila**
Para personalizar el encabezado o título de una fila:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en GridWorksheetCollection.
1. Establece el título de cualquier fila especificada.

**Se han personalizado los encabezados de las filas 1 y 2.** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **Personalización del encabezado de columna**
Para personalizar el encabezado o título de una columna:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en GridWorksheetCollection.
1. Establezca el título de cualquier columna especificada.

**Se han personalizado los encabezados de las columnas 1 y 2.** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **Congelar y descongelar filas y columnas**
Este tema explica cómo congelar y descongelar filas y columnas. Congelar columnas o filas permite a los usuarios mantener visibles los encabezados de las columnas o las filas mientras se desplazan a otras partes de la hoja de trabajo. Esta característica es muy útil cuando se trabaja con hojas de trabajo que contienen grandes volúmenes de datos. Cuando los usuarios se desplazan, solo los datos se desplazan hacia abajo y los encabezados permanecen en su lugar, lo que hace que la fecha sea más fácil de leer. La función congelar paneles solo se admite en Internet Explorer 6.0 o superior.
###  **Congelar filas y columnas**
Para congelar un número específico de filas y columnas:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceder a una hoja de trabajo.
1. Congele varias filas y columnas.

{{% alert color="primary" %}} 

 También es posible congelar una cantidad específica de filas y columnas usando la interfaz. Haga clic derecho en una celda donde desea congelar filas y columnas y seleccione**Congelar** de la lista.

{{% /alert %}} 

**Filas y columnas en estado congelado** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **Descongelar filas y columnas**
Para descongelar filas y columnas:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceder a una hoja de trabajo.
1. Descongelar filas y columnas.

**Hoja de trabajo después de ser descongelada** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **Proteger filas y columnas**
En este tema se analizan algunas técnicas para proteger celdas en filas y columnas de cualquier tipo de acción realizada por los usuarios finales. Los desarrolladores pueden implementar esta protección usando dos técnicas: haciendo que las celdas en filas y columnas sean de solo lectura, o restringiendo las opciones del menú contextual de GridWeb.
###  **Restringir las opciones del menú contextual**
GridWeb proporciona un menú contextual que los usuarios finales pueden utilizar para realizar operaciones en el control. El menú ofrece muchas opciones para manipular celdas, filas y columnas.

**Opciones contextuales completas** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Es posible restringir cualquier tipo de operaciones del lado del cliente en filas y columnas restringiendo las opciones disponibles en el menú contextual. Se puede hacer configurando los atributos EnableClientColumnOperations y EnableClientRowOperations del control GridWeb en falso. También es posible impedir que los usuarios congelen filas y columnas estableciendo el atributo EnableClientFreeze del control GridWeb en falso.

**Menú contextual después de restringir las opciones de filas y columnas** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
