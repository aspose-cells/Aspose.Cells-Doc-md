---
title: Läsning och skrivning av frågetabell i arbetsblad
type: docs
weight: 560
url: /sv/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) samlingen som returnerar [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection). För att få en specifik [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable), använd [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) egenskapen och ange indexet för QueryTable. [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) klassen har följande två egenskaper för att justera QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Dessa är båda booleska värden. Du kan se dem i Microsoft Excel via Data > Anslutningar > Egenskaper.

{{% /alert %}} 
## **Läsning och skrivning av frågetabell i arbetsbladet**
Följande exempelkod läser den första [frågetabellen](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) i det första arbetsbladet och skriver sedan ut båda [frågetabell](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)-egenskaperna. Sedan ställer den in [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) till **true**.

Nedanstående skärmbild visar den [källa excel filen](5472578.xlsx) som används i koden och dess egenskaper som visar både [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) värden.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

Nedanstående skärmbild visar den [utdata excelfilen](5472574.xlsx) genererad av koden och dess egenskaper som visar både [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) värden. Som du kan se är kryssrutan Bevarad formatering nu markerad.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsoloutput**
Här är konsoloutputen av ovanstående kodexempel

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Hämta frågetabellresultatområde**
Aspose.Cells tillhandahåller alternativet att läsa adressen dvs. resultatområdet för en frågetabell. Nedanstående kod demonstrerar denna funktion genom att läsa adressen för resultatområdet för en frågetabell. Den provfilen kan laddas ner [här](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
