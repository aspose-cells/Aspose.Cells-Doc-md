---
title: Ändern Sie Slicer Eigenschaften mit Node.js via C++
linktitle: Slicer Eigenschaften ändern
type: docs
weight: 70
url: /de/nodejs-cpp/change-slicer-properties/
---

## **Mögliche Verwendungsszenarien**

Es kann Situationen geben, in denen Sie die Eigenschaften des Slicers wie Position oder Zeilenhöhe ändern möchten. Aspose.Cells for Node.js via C++ bietet Ihnen die Möglichkeit, diese Eigenschaften zu aktualisieren.

## **Slicer-Eigenschaften ändern**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispieldatei](sampleCreateSlicerToExcelTable.xlsx), die eine Tabelle enthält. Dann erstellt er den Slicer basierend auf der ersten Spalte und ändert dessen Eigenschaften wie Zeilenhöhe, Breite, ist druckbar, Titel, etc. Er speichert die Arbeitsmappe als [Ausgabedatei zum Ändern der Slicer-Eigenschaften.xlsx](outputChangeSlicerProperties.xlsx).

## **Beispielcode**

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
