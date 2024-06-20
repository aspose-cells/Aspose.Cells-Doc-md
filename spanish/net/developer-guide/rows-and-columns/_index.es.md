---
title: Formato de Filas y Columnas
linktitle: Filas y Columnas
type: docs
weight: 100
url: /es/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET puede admitir cambios en la altura de fila o el ancho de columna, así como aplicar formato a filas o columnas.
keywords: Establecer altura de la fila y ancho de la columna, ajustar la altura de la fila y ancho de la columna, cambiar la altura de la fila o ancho de la columna, dar formato a filas y columnas, cómo establecer la altura de la fila y el ancho de la columna.
---


{{% alert color="primary" %}}

Al trabajar con hojas de cálculo y añadir datos a filas o columnas, es posible que necesites cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que la altura o el ancho actuales necesitan cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Sin embargo, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}}

## **Trabajar con filas**

### **Cómo ajustar la altura de fila**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación con más detalle.

### **Cómo establecer la altura de una fila**

Es posible establecer la altura de una sola fila llamando al método [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). El método [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) toma los siguientes parámetros como sigue:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Cómo establecer la altura de todas las filas en una hoja de cálculo**

Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas en la hoja de cálculo, pueden hacerlo usando la propiedad [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

**Ejemplo:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Trabajar con columnas**

### **Cómo establecer el ancho de una columna**

Establezca el ancho de una columna llamando al método [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). El método [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Cómo establecer el ancho de columna en píxeles**

Establezca el ancho de una columna llamando al método [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). El método [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de columna**, el ancho de columna deseado en píxeles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Cómo establecer el ancho de todas las columnas en una hoja de cálculo**

Para establecer el mismo ancho de columna para todas las columnas en la hoja de cálculo, use la propiedad [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Temas avanzados**
- [Ajustar automáticamente filas y columnas](/cells/es/net/autofit-rows-and-columns/)
- [Convertir Texto en Columnas usando Aspose.Cells](/cells/es/net/convert-text-to-columns-using-aspose-cells/)
- [Copiando Filas y Columnas](/cells/es/net/copying-rows-and-columns/)
- [Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo](/cells/es/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Agrupar y Desagrupar Filas y Columnas](/cells/es/net/grouping-and-ungrouping-rows-and-columns/)
- [Ocultar y Mostrar Filas y Columnas](/cells/es/net/hiding-and-showing-rows-and-columns/)
- [Insertar o Eliminar Filas en una Hoja de Cálculo de Excel](/cells/es/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insertar y Eliminar Filas y Columnas de un archivo de Excel](/cells/es/net/inserting-and-deleting-rows-and-columns/)
- [Eliminar filas duplicadas en una hoja de cálculo](/cells/es/net/remove-duplicate-rows-in-a-worksheet/)
- [Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo](/cells/es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
