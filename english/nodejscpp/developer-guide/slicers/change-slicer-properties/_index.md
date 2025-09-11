---
title: Change Slicer Properties with Node.js via C++
linktitle: Change Slicer Properties
type: docs
weight: 70
url: /nodejs-cpp/change-slicer-properties/
---

## **Possible Usage Scenarios**

There might be situations where you may want to change the properties of the Slicer such as placement or row height. Aspose.Cells for Node.js via C++ provides you with the option to update these properties.

## **Change Slicer Properties**

Please see the following sample code. It loads the [sample Excel file](sampleCreateSlicerToExcelTable.xlsx) that contains a table. It then creates the slicer based on the first column and changes its properties like row height, width, is printable, title, etc. It saves the workbook as [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Sample Code**

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
{{< app/cells/assistant language="nodejs-cpp" >}}