---
title: Ajustar automáticamente filas y columnas
type: docs
weight: 20
url: /es/python-net/autofit-rows-and-columns/
description: Este artículo muestra cómo ajustar automáticamente filas, columnas, filas de celdas fusionadas y filas en un rango de celdas mediante la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca Python de Excel, Ajuste automático de filas en Python, ajuste automático de columnas en Python, ajuste automático de fila en un rango de celdas en Python, ajuste automático de filas de celdas fusionadas en Python.
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios ajustar automáticamente el ancho y la altura de las celdas según su contenido. Esta característica también está disponible a través de Aspose.Cells para Python via .NET para que los desarrolladores puedan ajustar dinámicamente las dimensiones de una celda.

{{% /alert %}}

## **Ajuste automático**

Aspose.Cells para Python via .NET proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Este artículo analiza el uso de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) para ajustar automáticamente filas o columnas.

### **Ajuste automático de fila - Simple**

El enfoque más directo para ajustar automáticamente el ancho y alto de una fila es llamar al método [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). El método [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) toma como parámetro el índice de la fila a redimensionar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Cómo AutoAjustar una Fila en un Rango de Celdas**

Una fila está compuesta de muchas columnas. Aspose.Cells for Python via .NET permite a los desarrolladores ajustar automáticamente una fila basándose en el contenido en un rango de celdas dentro de la fila llamando a una versión sobrecargada del método [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int). Toma los siguientes parámetros:

- **Índice de la fila**, el índice de la fila a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

El método [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) verifica el contenido de todas las columnas en la fila y luego ajusta automáticamente la fila.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Cómo AutoAjustar una Columna en un Rango de Celdas**

Una columna está compuesta por muchas filas. Es posible ajustar automáticamente una columna en función del contenido en un rango de celdas en la columna llamando a una versión sobrecargada del método [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) que toma los siguientes parámetros:

- **Índice de columna**, el índice de la columna que se va a ajustar automáticamente.
- **Índice de la primera fila**, el índice de la primera fila de la columna.
- **Índice de la última fila**, el índice de la última fila de la columna.

El método [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Cómo AutoAjustar Filas para Celdas Fusionadas**

Con Aspose.Cells para Python via .NET es posible ajustar automáticamente filas incluso para celdas que han sido fusionadas utilizando la API [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions). La clase [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) proporciona la propiedad [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) que se puede usar para ajustar automáticamente filas para celdas fusionadas. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) acepta una enumeración [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) que tiene los siguientes miembros.

- NONE: Ignorar celdas fusionadas.
- FIRST_LINE: Solo expande la altura de la primera fila.
- LAST_LINE: Solo expande la altura de la última fila.
- EACH_LINE: Solo expande la altura de cada fila.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

También puedes probar a usar las versiones sobrecargadas de los métodos [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) y [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) que aceptan un rango de filas/columnas y una instancia de [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) para ajustar automáticamente las filas/columnas seleccionadas con tu [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) deseado correspondientemente.

Las firmas de los métodos antes mencionados son las siguientes:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) opciones)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Importante saber**

{{% alert color="primary" %}}

Si una celda está fusionada, entonces los métodos AutoFit no se aplicarán, lo cual es el mismo comportamiento que en Microsoft Excel. Puedes evitar esto utilizando la API de filtro automático. Además, si el texto en una celda está envuelto, el método [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) tampoco se aplicará. Otro detalle que debes saber es que los métodos *AutoFit* consumen tiempo. Por lo tanto, debes llamar a estos métodos lo menos posible para garantizar la eficiencia de tu aplicación.

{{% /alert %}}

## **Temas avanzados**
- [Ajustar automáticamente filas para celdas fusionadas](/cells/es/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
