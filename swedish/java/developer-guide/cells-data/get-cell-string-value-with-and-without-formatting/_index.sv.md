---
title: Hämta Cell String Value med och utan formatering
type: docs
weight: 230
url: /sv/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller en metod[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) som kan användas för att få strängvärdet för cellen med eller utan någon formatering. Anta att du har en cell med värdet 0,012345 och du har formaterat den så att den endast visar två decimaler. Det kommer då att visas som 0.01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0,012345 med hjälp av[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) metod. Det tar[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum som en parameter som har följande värden

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Hämta Cell String Value med och utan formatering**
 Följande exempelkod förklarar användningen av[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsolutgång**
Nedan är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
