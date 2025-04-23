---
title: Mostrar y ocultar filas, columnas y barras de desplazamiento
type: docs
weight: 20
url: /es/net/show-and-hide-rows-columns-and-scroll-bars/
description: Este artículo muestra cómo mostrar y ocultar programáticamente filas y columnas de hojas de cálculo de Excel usando el lenguaje C# y la API o biblioteca .NET. La visibilidad de las barras de desplazamiento se puede ajustar y varias filas y columnas se pueden ocultar.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona formas de controlar la visibilidad de filas, columnas y barras de desplazamiento de una hoja de cálculo.

{{% /alert %}}

## **Mostrar y ocultar filas y columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) que representa todas las celdas en la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

### **Mostrar filas y columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) y [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mientras se hace visible una columna oculta, si se necesita restaurarla al ancho asignado previamente o a su ancho original, por favor desocultar la columna con un ancho negativo. Por ejemplo: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Ocultar filas y columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) y [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

### **Ocultar múltiples filas y columnas**

Los desarrolladores pueden ocultar múltiples filas o columnas a la vez llamando a los métodos [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) y [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) respectivamente. Ambos métodos toman el índice de la fila o columna inicial y el número de filas o columnas que se deben ocultar como parámetros.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento se utilizan para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de cálculo. Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en los archivos de Excel.

### **Controlar la visibilidad de las barras de desplazamiento**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, utilice las propiedades [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) son propiedades booleanas, lo que significa que estas propiedades solo pueden almacenar valores **true** o **false**.

#### **Hacer visibles las Barras de Desplazamiento**

Haga visibles las barras de desplazamiento estableciendo la propiedad [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) en **true**.

#### **Ocultar Barras de Desplazamiento**

Oculte las barras de desplazamiento estableciendo la propiedad [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) en **false**.

**Código de Ejemplo**

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
