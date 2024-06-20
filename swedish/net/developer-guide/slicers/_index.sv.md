---
title: Infoga Slicer
linktitle: Slicers
type: docs
weight: 170
url: /sv/net/create-slicer/
description: Hantera slicers av Excel filer med Aspose.Cells.
---

## **Möjliga användningsscenario**

En slicer används för att filtrera data snabbt. Den kan användas för att filtrera data både i en tabell eller pivottabell. Microsoft Excel tillåter dig att skapa slicer genom att markera en tabell eller pivottabell och sedan klicka på *Infoga > Slicer*. Aspose.Cells tillåter också att du skapar slicer med hjälp av [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index) -metoden.

## **Skapa skärva till en pivot-tabell**

Se följande exempelkod. Den laddar den [prov-Excel-filen](67338470.xlsx) som innehåller pivottabellen. Den skapar sedan slicern baserad på det första baspivottfältet. Slutligen sparar den arbetsboken i [utmatnings-XLSX](67338471.xlsx) och [utmatnings-XLSB](67338472.xlsb) format. Följande skärmbild visar slicern skapad av Aspose.Cells i den utmatnings-Excel-filen.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Skapa skärva till Excel-tabell**

Vänligen se det följande provkoden. Den laddar [provmappen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Sedan skapar den en slicer baserad på den första kolumnen. Slutligen sparar den arbetsboken i [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Fortsatta ämnen**
- [Ändra Slicer-egenskaper](/cells/sv/net/change-slicer-properties/)
- [Rita Slicer vid rendering av Excel till PDF](/cells/sv/net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatera skärva](/cells/sv/net/formatting-slicer/)
- [Ta bort slicer](/cells/sv/net/removing-slicer/)
- [Rendering slicer](/cells/sv/net/rendering-slicer/)
- [Uppdatera slicer](/cells/sv/net/updating-slicer/)
