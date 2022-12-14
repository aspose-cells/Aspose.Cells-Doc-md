---
title: Ocultar y mostrar filas y columnas
type: docs
weight: 50
url: /es/java/hiding-and-showing-rows-and-columns/
---
## **Introducción**
A veces, los usuarios también pueden solicitar que oculten ciertas filas o columnas de la hoja de trabajo y luego las muestren más tarde. Microsoft Excel proporciona esta función y también Aspose.Cells.
## **Controlar la visibilidad de filas y columnas**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección que representa todas las celdas de la hoja de trabajo. los[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección proporciona varios métodos para administrar filas o columnas en una hoja de cálculo. Algunos de éstos se discuten a continuación.
### **Ocultar filas o columnas**
 Los desarrolladores pueden ocultar una fila o columna llamando al[Ocultarfila](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) y[OcultarColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) métodos de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección respectivamente. Ambos métodos toman el índice de fila/columna como parámetro para ocultar la fila o columna específica.

{{% alert color="primary" %}} 

Nota: También es posible ocultar una fila o una columna si configuramos la altura de la fila o el ancho de la columna en 0 respectivamente.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Mostrar filas y columnas**
 Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando al[Mostrar Fila](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) y[Mostrar columna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) métodos de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Alto de fila o ancho de columna** - el alto de fila o el ancho de columna asignado a la fila o columna después de mostrarse.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Mientras hace visible una columna/fila oculta, si necesita restaurarla al ancho o alto previamente asignado, o su ancho o alto original, muestre la columna o fila con ancho o alto negativo. Por ejemplo, hoja de trabajo.getCells().unhideColumn(5, -1)

{{% /alert %}}
