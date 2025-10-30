---
title: Ocultar y Mostrar Filas y Columnas
type: docs
weight: 60
url: /es/python-net/hiding-and-showing-rows-and-columns/
description: Este artículo muestra cómo ocultar y mostrar filas y columnas mediante la API via .NET de Aspose.Cells para Python.
keywords: Biblioteca de Excel de Python, Ocultar y mostrar filas de Python de Aspose.Cells, Ocultar y mostrar columnas de Python, Ocultar filas y columnas de Python, Mostrar filas y columnas de Python.
---

{{% alert color="primary" %}}

A veces, tiene sentido ocultar ciertas filas o columnas en una hoja de cálculo y mostrarlas más tarde. Microsoft Excel proporciona esta función y también lo hace Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Controlar la Visibilidad de Filas y Columnas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo. La colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) ofrece varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

## **Cómo ocultar filas y columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) y [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

## **Cómo mostrar filas y columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) y [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Mientras se hace visible una columna oculta, si se necesita restaurarla al ancho asignado previamente o a su ancho original, por favor desocultar la columna con un ancho negativo. Por ejemplo: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Cómo ocultar múltiples filas y columnas**

Los desarrolladores pueden ocultar múltiples filas o columnas a la vez llamando a los métodos [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) y [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) respectivamente. Ambos métodos toman el índice de la fila o columna inicial y el número de filas o columnas que se deben ocultar como parámetros.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

También es posible usar los métodos [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) y [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) de la clase [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) para hacer varias filas y columnas visibles.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
