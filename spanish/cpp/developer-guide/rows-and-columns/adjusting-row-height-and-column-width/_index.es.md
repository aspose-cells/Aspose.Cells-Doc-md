---
title: Ajustar la altura de fila y el ancho de columna
type: docs
weight: 10
url: /es/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Al trabajar con hojas de cálculo y añadir datos a filas o columnas, es posible que necesites cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que la altura o el ancho actual necesitan modificarse para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno visual utilizando Microsoft Excel. Sin embargo, con Aspose.Cells los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}} 
## **Trabajar con filas**
### **Ajustar la altura de la fila**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de cálculo. La colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) ofrece varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de ellos se discuten a continuación con más detalle.
#### **Ajuste de la Altura de una Fila**
Es posible ajustar la altura de una sola fila llamando al método [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . El método [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) toma los siguientes parámetros como sigue:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Ajuste de la Altura de Todas las Filas en una Hoja de Cálculo**
Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas en la hoja de cálculo, pueden hacerlo utilizando el método [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) .



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Trabajar con columnas**
### **Establecer el ancho de una columna**
Establezca el ancho de una columna llamando al método [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . El método [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Ajuste del Ancho de Todas las Columnas en una Hoja de Cálculo**
Para establecer el mismo ancho de columna para todas las columnas en la hoja de cálculo, utilice el método [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) .



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
