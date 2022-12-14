---
title: Holen Sie sich Cell Zeichenfolgenwert mit und ohne Formatierung
type: docs
weight: 230
url: /de/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells stellt eine Methode bereit[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)), die verwendet werden kann, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung abzurufen. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und Sie haben sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. Es wird dann in Excel als 0,01 angezeigt. Sie können Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 abrufen, indem Sie die verwenden[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) Methode. Es braucht[CellValueFormatStrategie](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum als Parameter, der die folgenden Werte hat

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Holen Sie sich Cell Zeichenfolgenwert mit und ohne Formatierung**
 Der folgende Beispielcode erläutert die Verwendung von[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsolenausgabe**
Unten ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
