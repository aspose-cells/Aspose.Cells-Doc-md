---
title: Skapa slicer till Excel tabell
type: docs
weight: 15
url: /sv/java/create-slicer-to-excel-table/
---

## **Möjliga användningsscenario**

En slicer används för att filtrera data snabbt. Den kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel tillåter dig att skapa slicer genom att markera en tabell eller pivottabell och sedan klicka på *Infoga > Slicer*. Aspose.Cells tillåter också att du skapar slicer med hjälp av [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int)) -metoden.

## **Skapa skärva till Excel-tabell**

Vänligen se det följande provkoden. Den laddar [provmappen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Sedan skapar den en slicer baserad på den första kolumnen. Slutligen sparar den arbetsboken i [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
