---
title: Läsa och skriva frågetabell med arbetsblad
type: docs
weight: 560
url: /sv/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) samling som returnerar[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . För att få en specifik[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , Använd[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) egenskapen och skicka indexet för frågetabellen. De[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) klass har följande två egenskaper för att justera frågetabellen.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Dessa är båda booleska värden. Du kan se dem i Microsoft Excel via Data > Anslutningar > Egenskaper.

{{% /alert %}} 
## **Läsa och skriva frågetabell med arbetsblad**
 Följande exempelkod läser den första[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)av det första kalkylbladet och skriver sedan ut båda[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) egenskaper. Sedan ställer den in[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) till**Sann**.

 Följande skärmdump visar[source excel-fil](5472578.xlsx) används i koden och dess egenskaper som visar båda[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)värden.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

 Följande skärmdump visar[output excel-fil](5472574.xlsx) genereras av koden och dess egenskaper som visar båda[Frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)värden. Som du kan se är kryssrutan Bevarad formatering markerad nu.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Hämta resultatintervall för frågetabell**
Aspose.Cells ger alternativet att läsa adressen, dvs. resultatintervall av celler för en frågetabell. Följande kod demonstrerar denna funktion genom att läsa adressen till resultatintervallet för en frågetabell. Exempelfilen kan laddas ner[här](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
