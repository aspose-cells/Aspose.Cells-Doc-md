---
title: Infoga Slicer
linktitle: Slicers
type: docs
weight: 170
url: /sv/nodejs-cpp/create-slicer/
description: Hantera slicers i Excel filer med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

En slicer används för att snabbt filtrera data. Den kan användas för att filtrera data i både ett bord och pivottabell. Microsoft Excel låter dig skapa slicer genom att välja ett bord eller pivottabell och klicka på *Infoga > Slicer*. Aspose.Cells for Node.js via C++ tillåter också att du skapar slicer med hjälp av [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-)-metoden.

## **Skapa skärva till en pivot-tabell**

Se följande exempel. Det laddar [exempel Excel-fil](67338470.xlsx) som innehåller pivottabellen. Sedan skapas slicern baserat på det första baspivåfältet. Slutligen sparas arbetsboken i [utdata XLSX](67338471.xlsx) och [utdata XLSB](67338472.xlsb) format. Följande skärmdump visar slicern som skapats av Aspose.Cells for Node.js via C++ i utdata Excel-fil.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Skapa skärva till Excel-tabell**

Vänligen se det följande provkoden. Den laddar [provmappen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Sedan skapar den en slicer baserad på den första kolumnen. Slutligen sparar den arbetsboken i [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
