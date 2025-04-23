---
title: Ocultar y Mostrar Filas y Columnas
type: docs
weight: 60
url: /es/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

A veces, tiene sentido ocultar ciertas filas o columnas en una hoja de cálculo y mostrarlas más tarde. Microsoft Excel proporciona esta característica y también lo hace Aspose.Cells.

{{% /alert %}}

## **Controlar la Visibilidad de Filas y Columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) que representa todas las celdas de la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de ellos se discuten a continuación.

### **Ocultar Filas y Columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) y [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

### **Mostrar Filas y Columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) y [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mientras se hace visible una columna oculta, si se necesita restaurarla al ancho asignado previamente o a su ancho original, por favor desocultar la columna con un ancho negativo. Por ejemplo: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Ocultar Múltiples Filas y Columnas**

Los desarrolladores pueden ocultar múltiples filas o columnas a la vez llamando a los métodos [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) y [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) respectivamente. Ambos métodos toman el índice de la fila o columna inicial y el número de filas o columnas que se deben ocultar como parámetros.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

También es posible usar los métodos [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) y [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) para hacer varias filas y columnas visibles.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
