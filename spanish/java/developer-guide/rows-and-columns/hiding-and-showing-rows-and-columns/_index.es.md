---
title: Ocultar y Mostrar Filas y Columnas
type: docs
weight: 50
url: /es/java/hiding-and-showing-rows-and-columns/
---

## **Introducción**
A veces, los usuarios también pueden requerir ocultar ciertas filas o columnas de la hoja de cálculo y luego mostrarlas más tarde. Microsoft Excel proporciona esta función y también lo hace Aspose.Cells.
## **Control de la Visibilidad de Filas y Columnas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) que representa todas las celdas en la hoja de cálculo. La colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.
### **Ocultar Filas o Columnas**
Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\)) y [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\)) respectivamente, de la colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ambos métodos toman el índice de la fila/columna como parámetro para ocultar la fila o columna específica.

{{% alert color="primary" %}} 

Nota: También es posible ocultar una fila o columna si establecemos la altura de la fila o el ancho de la columna en 0 respectivamente.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Mostrar Filas y Columnas**
Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\)) y [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\)) respectivamente, de la colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o ancho de columna asignado a la fila o columna después de que se muestra.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Al hacer visible una columna/fila oculta, si necesita restaurarla a la anchura o altura asignadas anteriormente, o a su anchura o altura original, desoculte la columna o fila con una anchura o altura negativa. Por ejemplo, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
