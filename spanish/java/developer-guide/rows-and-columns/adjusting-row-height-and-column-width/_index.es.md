---
title: Ajuste de altura de fila y ancho de columna
type: docs
weight: 10
url: /es/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Cuando trabaje con hojas de cálculo y agregue datos a filas o columnas, es posible que deba cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que la altura o el ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución. Los índices de filas y columnas comenzarán desde 0.

{{% /alert %}} 
## **Trabajar con filas**
### **Ajuste de altura de fila**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección que representa todas las celdas de la hoja de trabajo.

 los[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo. Algunos de estos se discuten a continuación con más detalle.
### **Configuración de la altura de la fila**
 Es posible establecer la altura de una sola fila llamando al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[establecerRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) método. los[establecerRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) método toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila cuya altura está cambiando.
- **Altura de la fila**, el alto de fila que se aplicará en la fila.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Configuración de la altura de todas las filas**
 Para establecer el mismo alto de fila para todas las filas de una hoja de trabajo, use el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[establecerAlturaEstándar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)método.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Trabajar con columnas**
### **Establecer el ancho de una columna**
 Establezca el ancho de una columna llamando al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[establecerAnchoColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) método. los[establecerAnchoColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) método toma los siguientes parámetros:

- **índice de columna**, el índice de la columna cuyo ancho está cambiando.
- **Ancho de columna**, el ancho de columna deseado.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Configuración del ancho de todas las columnas**
 Para establecer el mismo ancho de columna para todas las columnas de una hoja de trabajo, use el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[establecerAnchoEstándar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)método.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
