---
title: Formato de filas y columnas
linktitle: Filas y columnas
type: docs
weight: 100
url: /es/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

Cuando trabaje con hojas de cálculo y agregue datos a filas o columnas, es posible que deba cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato en filas o columnas significa que la altura o el ancho actual debe cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de las filas y el ancho de las columnas en un entorno WYSIWYG utilizando Microsoft Excel. Pero, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.

{{% /alert %}}

## **Trabajar con filas**

### **Ajuste de altura de fila**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección que representa todas las celdas de la hoja de cálculo.

 los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección proporciona varios métodos para administrar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación con más detalle.

### **Establecer la altura de una fila**

 Es posible establecer la altura de una sola fila llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**EstablecerRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) método. los[**EstablecerRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)El método toma los siguientes parámetros de la siguiente manera:

- **Índice de fila**, el índice de la fila cuya altura está cambiando.
- **Altura de la fila**, el alto de fila que se aplicará en la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Establecer la altura de todas las filas en una hoja de trabajo**

 Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas de la hoja de cálculo, pueden hacerlo mediante el[**Altura estándar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) propiedad de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)recopilación.

**Ejemplo:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Trabajar con columnas**

### **Establecer el ancho de una columna**

 Establezca el ancho de una columna llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Establecer ancho de columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) método. los[**Establecer ancho de columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)método toma los siguientes parámetros:

- **índice de columna**, el índice de la columna cuyo ancho está cambiando.
- **Ancho de columna**, el ancho de columna deseado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Configuración del ancho de columna en píxeles**

Establezca el ancho de una columna llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección[**EstablecerColumnaAnchoPíxel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)método. los[**EstablecerColumnaAnchoPíxel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)método toma los siguientes parámetros:

- **índice de columna**, el índice de la columna cuyo ancho está cambiando.
- **Ancho de columna**el ancho de columna deseado en píxeles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Establecer el ancho de todas las columnas en una hoja de trabajo**

 Para establecer el mismo ancho de columna para todas las columnas de la hoja de trabajo, use el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Ancho estándar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Temas avanzados**
- [Autoajustar filas y columnas](/cells/es/net/autofit-rows-and-columns/)
- [Convertir Texto a Columnas usando Aspose.Cells](/cells/es/net/convert-text-to-columns-using-aspose-cells/)
- [Copiar filas y columnas](/cells/es/net/copying-rows-and-columns/)
- [Eliminar filas y columnas en blanco en una hoja de cálculo](/cells/es/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Agrupación y desagrupación de filas y columnas](/cells/es/net/grouping-and-ungrouping-rows-and-columns/)
- [Ocultar y mostrar filas y columnas](/cells/es/net/hiding-and-showing-rows-and-columns/)
- [Insertar o eliminar filas en una hoja de cálculo de Excel](/cells/es/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insertar y eliminar filas y columnas de un archivo de Excel](/cells/es/net/inserting-and-deleting-rows-and-columns/)
- [Eliminar filas duplicadas en una hoja de trabajo](/cells/es/net/remove-duplicate-rows-in-a-worksheet/)
- [Actualice referencias en otras hojas de trabajo mientras elimina columnas y filas en blanco en una hoja de trabajo](/cells/es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
