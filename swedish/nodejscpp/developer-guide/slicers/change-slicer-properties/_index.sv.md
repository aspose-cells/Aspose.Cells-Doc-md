---
title: Ändra slicer egenskaper med Node.js via C++
linktitle: Ändra sliceregenskaper
type: docs
weight: 70
url: /sv/nodejs-cpp/change-slicer-properties/
---

## **Möjliga användningsscenario**

Det kan finnas situationer där du vill ändra egenskaper för slicern, såsom placering eller radhöjd. Aspose.Cells for Node.js via C++ ger dig möjlighet att uppdatera dessa egenskaper.

## **Ändra Slicer-egenskaper**

Var god se följande exempelkod. Den laddar in den [exempel-Excel-filen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Den skapar sedan slicern baserat på den första kolumnen och ändrar dess egenskaper som radhöjd, bredd, är utskrivbar, titel, osv. Den sparar arbetsboken som [utdataChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
