---
title: Cambiar propiedades del Segmentador con Node.js a través de C++
linktitle: Cambiar propiedades del rebanador
type: docs
weight: 70
url: /es/nodejs-cpp/change-slicer-properties/
---

## **Escenarios de uso posibles**

Podría darse la situación en la que desees cambiar las propiedades del Segmentador, como la ubicación o la altura de fila. Aspose.Cells for Node.js via C++ te ofrece la opción de actualizar estas propiedades.

## **Cambiar propiedades del rebanador**

Por favor, consulta el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego, crea el rebanador basado en la primera columna y cambia sus propiedades como altura de fila, ancho, es imprimible, título, etc. Guarda el libro de trabajo como [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Código de muestra**

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
