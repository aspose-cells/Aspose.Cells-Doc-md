---
title: Skapa Skärmdump till ett Pivottabell
type: docs
weight: 10
url: /sv/java/create-slicer-to-a-pivot-table/
---

## **Möjliga användningsscenario**
Slicern används för att snabb filtrera data. Den kan användas för att filtrera data både i en tabell och i pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på *Insert > Slicer*. Aspose.Cells tillåter också att du skapar slicer med hjälp av metoden [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-).
## **Skapa skärva till en pivot-tabell**
Var god se följande exempelkod. Den laddar in den [exempel-Excel-filen](67338498.xlsx) som innehåller pivottabellen. Den skapar sedan slicern baserat på den första baspivottabellfältet. Slutligen sparar den arbetsboken i [utdata XLSX](67338497.xlsx) och [utdata XLSB](67338496.xlsb) format. Följande skärmbild visar slicern som skapats av Aspose.Cells i utdata-Excel-filen.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
