---
title: Skapa en skivare till en pivottabell
type: docs
weight: 10
url: /sv/java/create-slicer-to-a-pivot-table/
---
## **Möjliga användningsscenarier**
Skäraren används för att snabbt filtrera data. Den kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på*Infoga > Slicer*. Aspose.Cells låter dig också skapa en skivare med hjälp av[Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) metod.
## **Skapa en skivare till en pivottabell**
Se följande exempelkod. Den laddar[exempel på Excel-fil](67338498.xlsx)som innehåller pivottabellen. Den skapar sedan slicer baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](67338497.xlsx)och[utgång XLSB](67338496.xlsb)formatera. Följande skärmdump visar slicer skapad av Aspose.Cells i utdata Excel-fil.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
