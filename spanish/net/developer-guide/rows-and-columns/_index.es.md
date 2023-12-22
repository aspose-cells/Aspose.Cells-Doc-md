---
title: Dar formato a filas y columnas
linktitle: Filas y columnas
type: docs
weight: 100
url: /es/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET puede admitir cambios en la altura de la fila o el ancho de la columna, así como aplicar formato en filas o columnas.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

Al trabajar con hojas de cálculo y agregar datos a filas o columnas, es posible que necesite cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato a filas o columnas significa que el alto o ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero con Aspose.Cells los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}}

##  **Trabajar con filas**

###  **Cómo ajustar la altura de la fila**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección que representa todas las celdas de la hoja de trabajo.

 El[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)La colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo. Algunos de estos se analizan a continuación con más detalle.

###  **Cómo establecer la altura de una fila**

 Es posible establecer la altura de una sola fila llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Establecer altura de fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) método. El[**Establecer altura de fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)El método toma los siguientes parámetros de la siguiente manera:

- *Índice de fila**, el índice de la fila cuya altura estás cambiando.
- *Alto de fila**, el alto de fila que se aplicará en la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **Cómo establecer la altura de todas las filas en una hoja de trabajo**

 Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas de la hoja de trabajo, pueden hacerlo usando el[**Altura estándar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) propiedad de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)recopilación.

**Ejemplo:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Trabajar con columnas**

###  **Cómo establecer el ancho de una columna**

 Establezca el ancho de una columna llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Establecer ancho de columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) método. El[**Establecer ancho de columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)El método toma los siguientes parámetros:

- *Índice de columna**, el índice de la columna cuyo ancho está cambiando.
- *Ancho de columna**, el ancho de columna deseado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **Cómo establecer el ancho de la columna en píxeles**

Establezca el ancho de una columna llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección[**Establecer ancho de columnaPíxel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)método. El[**Establecer ancho de columnaPíxel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)El método toma los siguientes parámetros:

- *Índice de columna**, el índice de la columna cuyo ancho está cambiando.
- *Ancho de columna**, el ancho de columna deseado en píxeles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **Cómo establecer el ancho de todas las columnas en una hoja de trabajo**

 Para establecer el mismo ancho de columna para todas las columnas de la hoja de trabajo, utilice el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Ancho estándar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **Temas avanzados**
- [Autoajustar filas y columnas](/cells/es/net/autofit-rows-and-columns/)
- [Convertir texto en columnas usando Aspose.Cells](/cells/es/net/convert-text-to-columns-using-aspose-cells/)
- [Copiar filas y columnas](/cells/es/net/copying-rows-and-columns/)
- [Eliminar filas y columnas en blanco en una hoja de trabajo](/cells/es/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Agrupar y desagrupar filas y columnas](/cells/es/net/grouping-and-ungrouping-rows-and-columns/)
- [Ocultar y mostrar filas y columnas](/cells/es/net/hiding-and-showing-rows-and-columns/)
- [Insertar o eliminar filas en una hoja de cálculo de Excel](/cells/es/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insertar y eliminar filas y columnas de un archivo Excel](/cells/es/net/inserting-and-deleting-rows-and-columns/)
- [Eliminar filas duplicadas en una hoja de trabajo](/cells/es/net/remove-duplicate-rows-in-a-worksheet/)
- [Actualice referencias en otras hojas de trabajo mientras elimina columnas y filas en blanco en una hoja de trabajo](/cells/es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
