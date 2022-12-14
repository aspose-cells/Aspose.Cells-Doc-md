---
title: Skapa Slicer till Excel-tabell
type: docs
weight: 15
url: /sv/java/create-slicer-to-excel-table/
---
## **Möjliga användningsscenarier**

 En slicer används för att filtrera data snabbt. Den kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på*Infoga > Slicer*. Aspose.Cells låter dig också skapa en skivare med hjälp av[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int)) metod.

## **Skapa Slicer till Excel-tabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Den skapar sedan slicer baserat på den första kolumnen. Slutligen sparar den arbetsboken[utgång XLSX](outputCreateSlicerToExcelTable.xlsx) formatera.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
