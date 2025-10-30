---
title: Formato de Filas y Columnas
linktitle: Filas y Columnas
type: docs
weight: 100
url: /es/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells para Python via .NET puede admitir el cambio de altura de fila o ancho de columna, así como aplicar formato en filas o columnas.
keywords: Biblioteca de Excel de Python, Establecer altura de fila y ancho de columna en Python, Ajustar altura de fila y ancho de columna en Python, Cambiar la altura de fila o ancho de columna en Python, Formatear filas y columnas en Python, Cómo establecer la altura de fila y ancho de columna en Python.
---


{{% alert color="primary" %}}

Cuando se trabaja con hojas de cálculo y se agrega datos a filas o columnas, es posible que necesite cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato en filas o columnas significa que la altura o el ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Sin embargo, con Aspose.Cells para Python via .NET, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}}

## **Trabajar con filas**

### **Cómo ajustar la altura de fila**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación con más detalle.

### **Cómo establecer la altura de una fila**

Es posible establecer la altura de una sola fila llamando al método [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). El método [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) toma los siguientes parámetros como sigue:

- **fila**, el índice de la fila a la que se le cambia la altura.
- **altura**, la altura de la fila que se aplica en la fila.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Cómo establecer la altura de todas las filas en una hoja de cálculo**

Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas en la hoja de cálculo, pueden hacerlo usando la propiedad [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**Ejemplo:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Trabajar con columnas**

### **Cómo establecer el ancho de una columna**

Establezca el ancho de una columna llamando al método [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). El método [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) toma los siguientes parámetros:

- **columna**, el índice de la columna cuyo ancho estás cambiando.
- **ancho**, el ancho de la columna deseado.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Cómo establecer el ancho de columna en píxeles**

Establezca el ancho de una columna llamando al método [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). El método [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) toma los siguientes parámetros:

- **columna**, el índice de la columna cuyo ancho estás cambiando.
- **píxeles**, el ancho de columna deseado en píxeles.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Cómo establecer el ancho de todas las columnas en una hoja de cálculo**

Para establecer el mismo ancho de columna para todas las columnas en la hoja de cálculo, use la propiedad [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Temas avanzados**
- [Ajustar automáticamente filas y columnas](/cells/es/python-net/autofit-rows-and-columns/)
- [Convertir Texto en Columnas usando Aspose.Cells](/cells/es/python-net/convert-text-to-columns-using-aspose-cells/)
- [Copiando Filas y Columnas](/cells/es/python-net/copying-rows-and-columns/)
- [Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo](/cells/es/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Agrupar y Desagrupar Filas y Columnas](/cells/es/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Ocultar y Mostrar Filas y Columnas](/cells/es/python-net/hiding-and-showing-rows-and-columns/)
- [Insertar o Eliminar Filas en una Hoja de Cálculo de Excel](/cells/es/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insertar y Eliminar Filas y Columnas de un archivo de Excel](/cells/es/python-net/inserting-and-deleting-rows-and-columns/)
- [Eliminar filas duplicadas en una hoja de cálculo](/cells/es/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo](/cells/es/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="python-net" >}}
