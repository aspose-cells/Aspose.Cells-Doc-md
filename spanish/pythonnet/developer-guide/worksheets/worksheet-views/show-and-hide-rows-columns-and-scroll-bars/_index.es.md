---
title: Mostrar y ocultar filas, columnas y barras de desplazamiento
type: docs
weight: 20
url: /es/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Este artículo demuestra cómo mostrar y ocultar programáticamente filas y columnas en la hoja de cálculo de Excel usando la API Aspose.Cells para Python via .NET. La visibilidad de las barras de desplazamiento puede ajustarse, y varias filas y columnas pueden ser ocultadas.
keywords: Biblioteca de Excel en Python, Mostrar filas y columnas en Python, Ocultar filas y columnas en Python, Mostrar barra de desplazamiento vertical en Python, Mostrar barra de desplazamiento horizontal en Python, Ocultar barra de desplazamiento vertical en Python, Ocultar barra de desplazamiento horizontal en Python, Mostrar y Ocultar Filas, Columnas y Barras de Desplazamiento en Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET proporciona formas de controlar la visibilidad de filas, columnas y barras de desplazamiento de una hoja de cálculo.

{{% /alert %}}

## **Mostrar y ocultar filas y columnas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite a los desarrolladores acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) que representa todas las celdas en la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) ofrece varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

### **Mostrar filas y columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) y [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Mientras se hace visible una columna oculta, si se necesita restaurarla al ancho asignado previamente o a su ancho original, por favor desocultar la columna con un ancho negativo. Por ejemplo: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Ocultar filas y columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) y [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

### **Ocultar múltiples filas y columnas**

Los desarrolladores pueden ocultar múltiples filas o columnas a la vez llamando a los métodos [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) y [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) respectivamente. Ambos métodos toman el índice de la fila o columna inicial y el número de filas o columnas que se deben ocultar como parámetros.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento se utilizan para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja. Usando Aspose.Cells para Python via .NET, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en archivos de Excel.

### **Controlar la visibilidad de las barras de desplazamiento**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ofrece una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, usa las propiedades [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) y [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) de la clase. [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) y [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) son propiedades booleanas, lo que significa que solo pueden almacenar valores **verdadero** o **falso**.

#### **Hacer visibles las Barras de Desplazamiento**

Haga visibles las barras de desplazamiento estableciendo la propiedad [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) o [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) en **true**.

#### **Ocultar Barras de Desplazamiento**

Oculte las barras de desplazamiento estableciendo la propiedad [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) o [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) en **false**.

**Código de Ejemplo**

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
