---
title: Modifica proprietà slicer con Node.js tramite C++
linktitle: Cambia proprietà Slicer
type: docs
weight: 70
url: /it/nodejs-cpp/change-slicer-properties/
---

## **Possibili Scenari di Utilizzo**

Potrebbero esserci situazioni in cui desideri modificare le proprietà dello Slicer come la posizione o l'altezza della riga. Aspose.Cells for Node.js via C++ ti permette di aggiornare queste proprietà.

## **Modifica le proprietà dello slicer**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](sampleCreateSlicerToExcelTable.xlsx) che contiene una tabella. Quindi crea il slicer in base alla prima colonna e cambia le sue proprietà come altezza riga, larghezza, è stampabile, titolo, ecc. Salva il workbook come [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Codice di Esempio**

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
