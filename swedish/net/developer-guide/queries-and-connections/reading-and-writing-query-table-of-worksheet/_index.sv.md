---
title: Läsning och skrivning av frågetabell i arbetsblad
type: docs
weight: 40
url: /sv/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller Worksheet.QueryTables-samlingen som returnerar objektet av typ QueryTable efter index. Den har följande två egenskaper

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Dessa är båda Boolean-värden. Du kan se dem i Microsoft Excel via Data > Connections > Properties.

{{% /alert %}}

## Läsning och skrivning av frågetabell i arbetsblad

Följande kodexempel läser den första frågetabellen på det första arbetsbladet och skriver sedan ut båda frågetabellegenskaperna. Sedan ställer den QueryTable.PreserveFormatting till true.

Du kan ladda ned den angivna källfilen Excel som används i koden och den genererade utdatafilen Excel med hjälp av följande länkar.

- [Käll-Excel-fil](5115533.xlsx)
- [Utdata-Excel-fil](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsolutfall

Här är konsoloutputen av ovanstående kodexempel

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Hämta frågetabellens resultatintervall

Aspose.Cells ger möjlighet att läsa adressen dvs resultatintervallen av celler för en frågetabell. Följande kod visar denna funktion genom att läsa adressen för resultatintervallen för en frågetabell. Exempelfilen kan laddas ner [här](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
