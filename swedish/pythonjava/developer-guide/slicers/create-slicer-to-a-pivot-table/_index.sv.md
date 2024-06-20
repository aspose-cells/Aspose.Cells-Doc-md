---
title: Skapa Skärmdump till ett Pivottabell
type: docs
weight: 10
url: /sv/python-java/create-slicer-to-a-pivot-table/
---

## **Möjliga användningsscenario**
Skärmdumpar används för att filtrera data snabbt. De kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel tillåter dig att skapa en skärmdump genom att välja en tabell eller pivottabell och sedan klicka på *Infoga > Skärmdump*. Aspose.Cells for Python via Java tillhandahåller metoden Worksheet.getSlicers().add() för att skapa skärmdump.
## **Skapa skärva till en pivot-tabell**
Följande kodsnutt laddar in [prov Excel-filen](106364966.xlsx) som innehåller pivottabellen. Sedan skapar den slicern baserat på det första pivefältet. Slutligen sparar den arbetsboken i [utdata XLSX](106364967.xlsx)-format. Följande skärmbild visar slicern skapad av Aspose.Cells i den genererade Excel-filen.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
