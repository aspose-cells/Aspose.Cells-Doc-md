---
title: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen
type: docs
weight: 230
url: /de/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet eine Methode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-), die verwendet werden kann, um den String-Wert der Zelle mit oder ohne Formatierung abzurufen. Angenommen, du hast eine Zelle mit dem Wert 0.012345 und hast sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. Dann zeigt sie in Excel als 0.01 an. Du kannst Strings sowohl als 0.01 als auch als 0.012345 mit der Methode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) abrufen. Diese Methode nimmt den [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) enum als Parameter, das die folgenden Werte hat.

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Zellzeichenfolgenwert mit und ohne Formatierung abrufen**
Der folgende Beispielcode erklärt die Verwendung der [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsolenausgabe**
Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
