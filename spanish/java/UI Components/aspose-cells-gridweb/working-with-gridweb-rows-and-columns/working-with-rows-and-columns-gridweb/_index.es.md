---
title: Trabajando con Filas y Columnas GridWeb
type: docs
weight: 20
url: /es/java/working-with-rows-and-columns-gridweb/
---
## **Insertar filas y columnas**
Este tema explica cómo insertar nuevas filas y columnas en una hoja de cálculo mediante Aspose.Cells.GridWeb API. Las filas o columnas se pueden insertar en cualquier posición de la hoja de cálculo.
### **Insertar filas**
Para insertar una fila en cualquier posición de una hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb al formulario o página web.
1. Acceda a la hoja de trabajo a la que está agregando filas.
1. Inserte una fila especificando un índice de fila donde se insertaría la fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Insertar columnas**
Para insertar una columna en cualquier posición de una hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo a la que está agregando columnas.
1. Inserte una columna especificando el índice de columna donde se insertaría la columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

También puede usar los métodos insertRows()/insertColumns() para insertar varias filas/columnas en las hojas de trabajo según corresponda.

{{% /alert %}} 
## **Eliminación de filas y columnas**
Este tema demuestra cómo eliminar filas y columnas de una hoja de cálculo mediante Aspose.Cells.GridWeb API. Con la ayuda de esta característica, los desarrolladores pueden eliminar filas o columnas en tiempo de ejecución.
### **Eliminación de filas**
Para eliminar una fila de su hoja de trabajo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo de la que desea eliminar filas.
1. Elimine una fila de la hoja de trabajo especificando su índice de fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Eliminación de columnas**
Para eliminar una columna de su hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Acceda a la hoja de trabajo de la que desea eliminar columnas.
1. Elimine una columna de la hoja de trabajo especificando su índice de columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Configuración de la altura de fila y el ancho de columna**
A veces, los valores de celda son más anchos que la celda en la que se encuentran o ocupan varias líneas. Dichos valores no son completamente visibles para los usuarios a menos que cambien la altura y el ancho de las filas y columnas. Aspose.Cells. GridWeb es totalmente compatible con la configuración de la altura de las filas y el ancho de las columnas. En este tema se describen estas características en detalle con la ayuda de ejemplos.
### **Trabajar con alturas de fila y ancho de columna**
#### **Configuración de la altura de fila**
Para establecer la altura de una fila:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección GridCells de la hoja de trabajo.
1. Establezca la altura de todas las celdas en cualquier fila especificada.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb acepta medidas de altura de fila y ancho de columna en puntos, pulgadas, píxeles, etc.

{{% /alert %}} 

**Salida: la altura de la primera fila se ha establecido en 50 puntos** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Configuración del ancho de columna**
Para establecer el ancho de una columna:

1. Agregue el control Aspose.Cells.GridWeb a su formulario/página web.
1. Acceda a la colección GridCells de la hoja de trabajo.
1. Establezca el ancho de todas las celdas en cualquier columna especificada.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personalización de encabezados de fila y columna**
Al igual que Microsoft Excel, Aspose.Cells. GridWeb también usa encabezados o leyendas estándar para filas (números como 1, 2, 3, etc.) y columnas (alfabéticas como A, B, C, etc.). Aspose.Cells. GridWeb también permite personalizar los subtítulos. Este tema trata sobre la personalización de encabezados de filas y columnas en tiempo de ejecución mediante Aspose.Cells.GridWeb API.
### **Personalización del encabezado de fila**
Para personalizar el encabezado o título de una fila:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en GridWorksheetCollection.
1. Establezca el título de cualquier fila especificada.

**Se han personalizado los encabezados de las filas 1 y 2** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personalización del encabezado de columna**
Para personalizar el encabezado o título de una columna:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Acceda a la hoja de trabajo en GridWorksheetCollection.
1. Establezca el título de cualquier columna especificada.

**Se han personalizado los encabezados de las columnas 1 y 2** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Congelar y descongelar filas y columnas**
Este tema explica cómo congelar y descongelar filas y columnas. La congelación de columnas o filas permite a los usuarios mantener visibles los encabezados de las columnas o los títulos de las filas mientras se desplazan a otras partes de la hoja de trabajo. Esta característica es muy útil cuando se trabaja con hojas de cálculo que contienen grandes volúmenes de datos. Cuando los usuarios se desplazan solo los datos se desplazan hacia abajo y los encabezados permanecen en su lugar, lo que facilita la lectura de la fecha. La característica de congelar paneles solo es compatible con Internet Explorer 6.0 o superior.
### **Congelación de filas y columnas**
Para congelar un número específico de filas y columnas:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Accede a una hoja de trabajo.
1. Congele un número de filas y columnas.

{{% alert color="primary" %}} 

 También es posible congelar un número específico de filas y columnas usando la interfaz. Haga clic derecho en una celda donde desea congelar filas y columnas y seleccione**Congelar** de la lista.

{{% /alert %}} 

**Filas y columnas en estado congelado** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Descongelar filas y columnas**
Para descongelar filas y columnas:

1. Agregue el control Aspose.Cells.GridWeb a un formulario/página web.
1. Accede a una hoja de trabajo.
1. Descongele filas y columnas.

**Hoja de trabajo después de ser descongelada** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Protección de filas y columnas**
Este tema analiza algunas técnicas para proteger celdas en filas y columnas de cualquier tipo de acción realizada por los usuarios finales. Los desarrolladores pueden implementar esta protección usando dos técnicas: haciendo que las celdas en filas y columnas sean de solo lectura, o restringiendo las opciones del menú contextual de GridWeb.
### **Restricción de las opciones del menú contextual**
GridWeb proporciona un menú contextual que los usuarios finales pueden usar para realizar operaciones en el control. El menú proporciona muchas opciones para manipular celdas, filas y columnas.

**Opciones contextuales completas** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_6.png)

Es posible restringir cualquier tipo de operaciones del lado del cliente en filas y columnas restringiendo las opciones disponibles en el menú contextual. Se puede hacer configurando los atributos EnableClientColumnOperations y EnableClientRowOperations del control GridWeb en false. También es posible impedir que los usuarios congelen filas y columnas configurando el atributo EnableClientFreeze del control GridWeb en falso.

**Menú contextual después de restringir las opciones de fila y columna** 

![todo:imagen_alternativa_texto](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
