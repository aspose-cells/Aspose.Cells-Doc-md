---
title: Infoga Slicer
linktitle: Slicers
type: docs
weight: 170
url: /sv/python-net/create-slicer/
description: Hantera slicers av Excel filer med Aspose.Cells.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Python skapar Slicer utan Excel, Lägg till Slicer via Aspose.Cells för Python, Infoga Slicer med Aspose.Cells för Python.
---

## **Möjliga användningsscenario**

En slicer används för att snabbt filtrera data. Den kan användas för att filtrera data både i en tabell eller en pivottabell. Microsoft Excel låter dig skapa en slicer genom att välja en tabell eller pivottabell och sedan klicka på *Infoga > Slicer*. Aspose.Cells för Python via .NET låter dig också skapa en slicer med hjälp av metoden [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField).

## **Hur man skapar en slicer till en pivottabell med hjälp av Aspose.Cells för Python Excel-bibliotek**

Se följande exempelkod. Den laddar den [prov-Excel-filen](67338470.xlsx) som innehåller pivottabellen. Den skapar sedan slicern baserad på det första baspivottfältet. Slutligen sparar den arbetsboken i [utmatnings-XLSX](67338471.xlsx) och [utmatnings-XLSB](67338472.xlsb) format. Följande skärmbild visar slicern skapad av Aspose.Cells i den utmatnings-Excel-filen.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

## **Hur man skapar en slicer till Excels tabell med hjälp av Aspose.Cells för Python Excel-bibliotek**

Vänligen se det följande provkoden. Den laddar [provmappen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Sedan skapar den en slicer baserad på den första kolumnen. Slutligen sparar den arbetsboken i [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

## **Fortsatta ämnen**
- [Ändra Slicer-egenskaper](/cells/sv/python-net/change-slicer-properties/)
- [Rita Slicer vid rendering av Excel till PDF](/cells/sv/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatera skärva](/cells/sv/python-net/formatting-slicer/)
- [Ta bort slicer](/cells/sv/python-net/removing-slicer/)
- [Rendering slicer](/cells/sv/python-net/rendering-slicer/)
- [Uppdatera slicer](/cells/sv/python-net/updating-slicer/)
{{< app/cells/assistant language="python-net" >}}
