---
title: Modifier les propriétés du segment avec Node.js via C++
linktitle: Changer les propriétés de la trancheuse
type: docs
weight: 70
url: /fr/nodejs-cpp/change-slicer-properties/
---

## **Scénarios d'utilisation possibles**

Il peut arriver que vous souhaitiez modifier les propriétés du segment comme le placement ou la hauteur de ligne. Aspose.Cells for Node.js via C++ vous offre la possibilité de mettre à jour ces propriétés.

## **Modifier les propriétés du segmentateur**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite la trancheuse en fonction de la première colonne et modifie ses propriétés telles que la hauteur de ligne, la largeur, l'impression, le titre, etc. Il enregistre le classeur sous forme de [fichier Excel de sortie](outputChangeSlicerProperties.xlsx).

## **Code d'exemple**

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
