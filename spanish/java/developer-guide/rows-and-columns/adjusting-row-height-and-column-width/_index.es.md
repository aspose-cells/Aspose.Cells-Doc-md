---
title: Ajustar la altura de fila y el ancho de columna
type: docs
weight: 10
url: /es/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Cuando trabajas con hojas de cálculo y añades datos a filas o columnas, es posible que necesites cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que la altura o el ancho actuales necesitan modificarse para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución. Los índices de filas y columnas comenzarán desde 0.

{{% /alert %}} 
## **Trabajar con filas**
### **Ajustar la altura de la fila**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de ellos se discuten a continuación con más detalle.
### **Establecer la altura de la fila**
Es posible establecer la altura de una sola fila llamando al método [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Establecer la altura de todas las filas**
Para establecer la misma altura de fila para todas las filas en una hoja de cálculo, utiliza el método [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Trabajar con columnas**
### **Establecer el ancho de una columna**
Establezca el ancho de una columna llamando al método [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Configuración del ancho de todas las columnas**
Para establecer el mismo ancho de columna para todas las columnas en una hoja de cálculo, use el método [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
