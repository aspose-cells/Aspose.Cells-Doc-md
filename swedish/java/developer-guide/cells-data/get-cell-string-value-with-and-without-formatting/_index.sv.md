---
title: Hämta cellsträngvärde med och utan formatering
type: docs
weight: 230
url: /sv/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller en metod [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) som kan användas för att hämta cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0.012345 och du har formaterat den för att visa endast två decimaler. Den kommer då att visas som 0.01 i Excel. Du kan hämta strängvärden både som 0.01 och som 0.012345 med metod [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-). Den tar emot enum [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) som parameter, vilket har följande värden.

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Få cellsträngvärde med och utan formatering**
Följande exempel kod förklarar användningen av [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsoloutput**
Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
