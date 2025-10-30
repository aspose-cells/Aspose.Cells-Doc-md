---
title: Läsning och skrivning av frågetabell i arbetsblad
type: docs
weight: 40
url: /sv/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET erbjuder Worksheet.QueryTables samling som returnerar QueryTable-objektet efter index. Den har följande två egenskaper

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Dessa är båda Boolean-värden. Du kan se dem i Microsoft Excel via Data > Connections > Properties.

{{% /alert %}}

## Läsning och skrivning av frågetabell i arbetsblad

Följande kodexempel läser den första frågetabellen på det första arbetsbladet och skriver sedan ut båda frågetabellegenskaperna. Sedan ställer den QueryTable.PreserveFormatting till true.

Du kan ladda ned den angivna källfilen Excel som används i koden och den genererade utdatafilen Excel med hjälp av följande länkar.

- [Käll-Excel-fil](5115533.xlsx)
- [Utdata-Excel-fil](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Konsolutfall

Här är konsoloutputen av ovanstående kodexempel

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Hämta frågetabellens resultatintervall

Aspose.Cells för Python via .NET ger möjlighet att läsa adressen dvs. resultatområdet för en frågetabell. Följande kod visar denna funktion genom att läsa adressen för resultatområdet för en frågetabell. En provfil kan laddas ner [här](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

{{< app/cells/assistant language="python-net" >}}
