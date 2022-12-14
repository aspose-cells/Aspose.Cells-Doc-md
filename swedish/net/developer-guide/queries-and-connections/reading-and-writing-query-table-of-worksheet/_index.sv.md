---
title: Läsa och skriva frågetabell med arbetsblad
type: docs
weight: 40
url: /sv/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells tillhandahåller Worksheet.QueryTables-samlingen som returnerar objektet av typen QueryTable efter index. Den har följande två egenskaper

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Dessa är båda booleska värden. Du kan se dem i Microsoft Excel via Data > Anslutningar > Egenskaper.

{{% /alert %}}

## Läsa och skriva frågetabell med arbetsblad

Följande exempelkod läser den första frågetabellen i det första kalkylbladet och skriver sedan ut båda QueryTable-egenskaperna. Sedan ställs QueryTable.PreserveFormatting till sant.

Du kan ladda ner källfilen för Excel som används i den här koden och Excel-utdatafilen som genereras av koden från följande länkar.

- [Excel-källfil](5115533.xlsx)
- [Utdata Excel-fil](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsolutgång

Här är konsolutgången för ovanstående exempelkod

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Hämta resultatintervall för frågetabell

 Aspose.Cells ger möjlighet att läsa adressen, dvs resultatintervall av celler för en frågetabell. Följande kod demonstrerar denna funktion genom att läsa adressen till resultatintervallet för en frågetabell. Exempelfil kan laddas ner[här](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
