---
title: Sätt i Slicer
linktitle: Skivmaskiner
type: docs
weight: 170
url: /sv/python-net/create-slicer/
description: Hantera utsnitt av Excel-filer med Aspose.Cells.
---
##  **Möjliga användningsscenarier**

En slicer används för att filtrera data snabbt. Den kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på *Infoga > Slicer*. Aspose.Cells for Python via .NET låter dig också skapa en skivare med[**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)metod.

##  **Skapa en skivare till en pivottabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](67338470.xlsx) som innehåller pivottabellen. Den skapar sedan slicer baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](67338471.xlsx) och[utgång XLSB](67338472.xlsb) formatera. Följande skärmdump visar slicer skapad av Aspose.Cells i utdata Excel-fil.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

###  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **Skapa Slicer till Excel-tabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Den skapar sedan slicer baserat på den första kolumnen. Slutligen sparar den arbetsboken[utgång XLSX](outputCreateSlicerToExcelTable.xlsx) formatera.

###  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **Förhandsämnen**
- [Ändra egenskaper för skivare](/cells/sv/python-net/change-slicer-properties/)
- [Rita Slicer medan du renderar Excel till PDF](/cells/sv/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatera Slicer](/cells/sv/python-net/formatting-slicer/)
- [Ta bort Slicer](/cells/sv/python-net/removing-slicer/)
- [Rendering Slicer](/cells/sv/python-net/rendering-slicer/)
- [Uppdaterar Slicer](/cells/sv/python-net/updating-slicer/)
