---
title: Obtenga el valor de cadena Cell con y sin formato
type: docs
weight: 230
url: /es/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells proporciona un método[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) que se puede usar para obtener el valor de cadena de la celda con o sin formato. Suponga que tiene una celda con valor 0.012345 y la ha formateado para mostrar solo dos lugares decimales. Luego se mostrará como 0.01 en Excel. Puede recuperar valores de cadena como 0.01 y como 0.012345 usando el[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) método. Se necesita[CellValueFormatoEstrategia](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum como un parámetro que tiene los siguientes valores

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Obtenga el valor de cadena Cell con y sin formato**
 El siguiente código de ejemplo explica el uso de[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Salida de consola**
A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
