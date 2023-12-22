---
title: Ajustar la altura de la fila y el ancho de la columna
type: docs
weight: 10
url: /es/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Al trabajar con hojas de cálculo y agregar datos a filas o columnas, es posible que necesite cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que el alto o ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero con Aspose.Cells los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}} 
##  **Trabajar con filas**
###  **Ajustar la altura de la fila**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase proporciona un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección que representa todas las celdas de la hoja de trabajo. El[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)La colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo. Algunos de estos se analizan a continuación con más detalle.
####  **Establecer la altura de una fila**
 Es posible establecer la altura de una sola fila llamando al[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección[Establecer altura de fila](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) método. El[Establecer altura de fila](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)El método toma los siguientes parámetros de la siguiente manera:

- *Índice de fila**, el índice de la fila cuya altura estás cambiando.
- *Alto de fila**, el alto de fila que se aplicará en la fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Establecer la altura de todas las filas en una hoja de trabajo**
 Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas de la hoja de trabajo, pueden hacerlo usando el[Establecer altura estándar](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)recopilación.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Trabajar con columnas**
###  **Establecer el ancho de una columna**
 Establezca el ancho de una columna llamando al[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección[Establecer ancho de columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) método. El[Establecer ancho de columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)El método toma los siguientes parámetros:

- *Índice de columna**, el índice de la columna cuyo ancho está cambiando.
- *Ancho de columna**, el ancho de columna deseado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Establecer el ancho de todas las columnas en una hoja de trabajo**
 Para establecer el mismo ancho de columna para todas las columnas de la hoja de trabajo, utilice el[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección[Establecer ancho estándar](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
