---
title: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen
type: docs
weight: 230
url: /de/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet eine Methode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)), die verwendet werden kann, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung zu erhalten. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und Sie haben sie formatiert, um nur zwei Dezimalstellen anzuzeigen. Es wird dann als 0,01 in Excel angezeigt. Sie können Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 mithilfe der Methode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) abrufen. Sie nimmt [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) enum als Parameter an, die die folgenden Werte enthält

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Zellzeichenfolgenwert mit und ohne Formatierung abrufen**
Der folgende Beispielcode erläutert die Verwendung der Methode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsolenausgabe**
Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
