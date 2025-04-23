---
title: Ajustar la altura de fila y el ancho de columna
type: docs
weight: 10
url: /es/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

Al trabajar con hojas de cálculo y añadir datos a filas o columnas, es posible que necesites cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que la altura o el ancho actual necesitan modificarse para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno visual utilizando Microsoft Excel. Sin embargo, con Aspose.Cells los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}}

## **Trabajar con filas**

### **Ajustar la altura de la fila**

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) proporciona una colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/) que representa todas las celdas en la hoja de cálculo. La colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/) ofrece varios métodos para administrar filas o columnas en una hoja de cálculo. Algunos de estos se discuten en más detalle a continuación.

#### **Ajuste de la Altura de una Fila**

Es posible establecer la altura de una sola fila llamando al método [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Ajuste de la Altura de Todas las Filas en una Hoja de Cálculo**

Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas en la hoja de cálculo, pueden hacerlo usando el método [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Trabajar con columnas**

### **Establecer el ancho de una columna**

Establece el ancho de una columna llamando al método [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Ajuste del Ancho de Todas las Columnas en una Hoja de Cálculo**

Para establecer el mismo ancho de columna para todas las columnas en la hoja de cálculo, usa el método [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
