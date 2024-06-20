---
title: Obtener el valor de cadena de la celda con o sin formato
type: docs
weight: 230
url: /es/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona un método [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) que se puede utilizar para obtener el valor de cadena de la celda con o sin ningún formato. Supongamos que tiene una celda con el valor 0.012345 y lo ha formateado para mostrar solo dos decimales. Entonces se mostrará como 0.01 en Excel. Puede recuperar los valores de cadena tanto como 0.01 y como 0.012345 usando el método [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)). Toma [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) como un parámetro que tiene los siguientes valores

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Obtener el valor de cadena de celda con y sin formato**
El siguiente código de muestra explica el uso de [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Salida de la consola**
A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
