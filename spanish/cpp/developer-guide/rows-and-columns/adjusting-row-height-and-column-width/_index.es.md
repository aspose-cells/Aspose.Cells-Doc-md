---
title: Ajuste de altura de fila y ancho de columna
type: docs
weight: 10
url: /es/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Cuando trabaje con hojas de cálculo y agregue datos a filas o columnas, es posible que deba cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato en filas o columnas significa que la altura o el ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}} 
## **Trabajar con filas**
### **Ajuste de altura de fila**
 Aspose.Cells proporciona una clase,[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona un[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección que representa todas las celdas de la hoja de trabajo. Él[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo. Algunos de estos se discuten a continuación con más detalle.
#### **Establecer la altura de una fila**
 Es posible establecer la altura de una sola fila llamando al[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección[EstablecerRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) método. Él[EstablecerRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)El método toma los siguientes parámetros de la siguiente manera:

- **Índice de fila**, el índice de la fila cuya altura está cambiando.
- **Altura de la fila**, el alto de fila que se aplicará en la fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Establecer la altura de todas las filas en una hoja de cálculo**
 Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas de la hoja de cálculo, pueden hacerlo mediante el[EstablecerAlturaEstándar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)recopilación.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Trabajar con columnas**
### **Establecer el ancho de una columna**
 Establezca el ancho de una columna llamando al[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección[Establecer ancho de columna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) método. Él[Establecer ancho de columna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)método toma los siguientes parámetros:

- **índice de columna**, el índice de la columna cuyo ancho está cambiando.
- **Ancho de columna**, el ancho de columna deseado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Establecer el ancho de todas las columnas en una hoja de trabajo**
 Para establecer el mismo ancho de columna para todas las columnas de la hoja de trabajo, use el[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección[EstablecerAnchoEstándar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
