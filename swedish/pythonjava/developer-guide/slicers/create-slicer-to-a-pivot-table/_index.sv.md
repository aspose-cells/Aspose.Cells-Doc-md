---
title: Skapa en skivare till en pivottabell
type: docs
weight: 10
url: /sv/python-java/create-slicer-to-a-pivot-table/
---
## **Möjliga användningsscenarier**
Slicers används för att snabbt filtrera data. De kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på*Infoga > Slicer*. Aspose.Cells for Python via Java tillhandahåller metoden Worksheet.getSlicers().add() för att skapa slicer.
## **Skapa en skivare till en pivottabell**
Följande kodavsnitt laddar[exempel på Excel-fil](106364966.xlsx)som innehåller pivottabellen. Den skapar sedan slicer baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](106364967.xlsx)formatera. Följande skärmdump visar slicer skapad av Aspose.Cells i utdata Excel-fil.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
