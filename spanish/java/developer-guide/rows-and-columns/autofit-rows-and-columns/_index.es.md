---
title: Ajustar automáticamente filas y columnas
type: docs
weight: 20
url: /es/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel proporciona una buena función para ajustar automáticamente el ancho y alto de una celda según su contenido. Esta función también está disponible para los usuarios de Aspose.Cells con el poder de ajustar automáticamente las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}} 
## **Ajuste automático**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Este artículo analiza el uso de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) para ajustar automáticamente filas o columnas.
### **Ajuste automático de fila - Simple**
El enfoque más sencillo para ajustar automáticamente el ancho y la altura de una fila es llamar al método [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). El método [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) acepta un índice de fila (de la fila a redimensionar) como parámetro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajuste automático de fila en un rango de celdas**
Una fila está compuesta por muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila según el contenido en un rango de celdas dentro de la fila llamando a una versión sobrecargada del método [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-). Este acepta los siguientes parámetros:

- **Índice de la fila**, el índice de la fila a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

El método [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) verifica el contenido de todas las columnas de la fila y ajusta automáticamente la fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Ajuste automático de columna - Simple**
La forma más fácil de ajustar automáticamente el ancho y la altura de una columna es llamar al método [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). El método [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) acepta el índice de columna (de la columna a redimensionar) como parámetro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajustar automáticamente la columna en un rango de celdas**
Una columna está compuesta por muchas filas. Es posible ajustar automáticamente una columna en función del contenido en un rango de celdas en la columna llamando a una versión sobrecargada del método [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) que acepta los siguientes parámetros:

- **Índice de columna**, representa el índice de la columna cuyo contenido necesita ajustarse automáticamente
- **Índice de la primera fila**, representa el índice de la primera fila de la columna
- **Índice de la última fila**, representa el índice de la última fila de la columna

El método [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Ajustar automáticamente filas para celdas fusionadas**
Con Aspose.Cells es posible ajustar automáticamente las filas incluso para celdas que han sido fusionadas utilizando la API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). La clase [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) proporciona la propiedad [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) que se puede usar para ajustar automáticamente las filas para celdas fusionadas. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) acepta el enumerador [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) que tiene los siguientes miembros.

- [NINGUNO](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NINGUNO): Ignorar celdas fusionadas.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): Solo expande la altura de la primera fila.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): Solo expande la altura de la última fila.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): Solo expande la altura de cada fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

También puedes usar las versiones sobrecargadas de los métodos [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) y [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) que aceptan un rango de filas/columnas y una instancia de [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) para ajustar automáticamente las filas/columnas seleccionadas con las [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) deseadas.

Las firmas de los métodos antes mencionados son las siguientes:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Importante saber**
{{% alert color="primary" %}} 

Si una celda está fusionada, los métodos *AutoFit* no se aplicarán, lo cual es el mismo comportamiento que en Microsoft Excel. Además, si el texto en una celda está envuelto, tampoco se aplicará el método [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-). Otra cosa que debe saber es que los métodos *AutoFit* consumen mucho tiempo. Por lo tanto, debe llamar a estos métodos lo menos posible para garantizar la eficiencia de su aplicación.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
