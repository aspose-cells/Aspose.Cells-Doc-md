---
title: Autoajustar filas y columnas
type: docs
weight: 20
url: /es/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel proporciona una buena función para cambiar automáticamente el tamaño del ancho y el alto de una celda según su contenido. Esta característica también está disponible para los usuarios de Aspose.Cells con el poder de cambiar automáticamente el tamaño de las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}} 
## **Ajuste automático**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de trabajo. Este artículo analiza el uso de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase para autoajustar filas o columnas.
### **Autoajustar fila - Simple**
 El enfoque más sencillo para cambiar automáticamente el tamaño del ancho y el alto de una fila es llamar al[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase'[autoajustar fila](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) método. los[autoajustar fila](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) toma un índice de fila (de la fila a redimensionar) como parámetro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Autoajustar fila en un rango de Cells**
 Una fila se compone de muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila según el contenido de un rango de celdas dentro de la fila llamando a una versión sobrecargada del[autoajustar fila](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) método. Toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila que se va a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

 los[autoajustar fila](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) comprueba el contenido de todas las columnas de la fila y luego ajusta automáticamente la fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Autoajustar columna - Simple**
 La forma más fácil de cambiar automáticamente el tamaño del ancho y el alto de una columna es llamar al[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase'[AutoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) método. los[AutoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)toma el índice de la columna (de la columna que se va a cambiar de tamaño) como parámetro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Autoajustar columna en un rango de Cells**
 Una columna se compone de muchas filas. Es posible ajustar automáticamente una columna en función del contenido de un rango de celdas de la columna llamando a una versión sobrecargada de[AutoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) método que toma los siguientes parámetros:

- **índice de columna**, representa el índice de la columna cuyo contenido debe ajustarse automáticamente
- **Índice de la primera fila**, representa el índice de la primera fila de la columna
- **Índice de la última fila**, representa el índice de la última fila de la columna

 los[AutoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) comprueba el contenido de todas las filas de la columna y luego ajusta automáticamente la columna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Autoajustar filas para combinar Cells**
Con Aspose.Cells es posible autoajustar filas incluso para celdas que se han combinado usando el[AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)clase proporciona[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)propiedad que se puede usar para autoajustar filas para celdas combinadas.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)acepta[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)enumerable que tiene los siguientes miembros.

- [NINGUNA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Ignora las celdas combinadas.
- [PRIMERA LINEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Solo expande la altura de la primera fila.
- [ÚLTIMA LÍNEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Solo expande la altura de la última fila.
- [CADA LÍNEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Solo expande la altura de cada fila.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 También puede utilizar las versiones sobrecargadas de[autoajustar filas](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [AutoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) métodos que aceptan un rango de filas/columnas y una instancia de[AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) para ajustar automáticamente las filas/columnas seleccionadas con el deseado[AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)respectivamente.

Las firmas de los métodos antes mencionados son las siguientes:

1.  autoFitRows(int StartRow, int EndRow,[AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)opciones)
1.  autoFitColumns(int primeracolumna, int ultimacolumna,[AutoFitterOpciones](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)opciones)
## **Importante saber**
{{% alert color="primary" %}} 

 Si se fusiona una celda, entonces el*Autoajustar* no se aplicarán los métodos, que es el mismo comportamiento que en Microsoft Excel. Además, si el texto de una celda está ajustado, la[AutoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) tampoco se aplicará el método. Otra cosa que debes saber es que el*Autoajustar*los métodos requieren mucho tiempo. Por lo tanto, debe llamar a estos métodos con la menor frecuencia posible para garantizar la eficiencia de su aplicación.

{{% /alert %}}
