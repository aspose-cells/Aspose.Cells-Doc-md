---
title: Obtener el valor de cadena de la celda con o sin formato
type: docs
weight: 230
url: /es/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona un método [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) que se puede usar para obtener el valor de la cadena de la celda con o sin formato. Supón que tienes una celda con valor 0.012345 y la has formateado para mostrar solo dos lugares decimales. Entonces se mostrará como 0.01 en Excel. Puedes recuperar valores de cadena tanto como 0.01 como 0.012345 usando el método [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-). Este método toma un enumerado de [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) como parámetro, que tiene los siguientes valores

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Obtener el valor de cadena de celda con y sin formato**
El siguiente código de ejemplo explica el uso del método [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Salida de la consola**
A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
