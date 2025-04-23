---
title: Rendre des lignes de grille solides lors de la conversion d Excel en PDF avec Node.js via C++
linktitle: Rendre la grille solide lors de la conversion d Excel en PDF
type: docs
weight: 390
url: /fr/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Apprenez comment rendre des lignes de grille solides lors de la conversion d Excel en PDF en utilisant Aspose.Cells for Node.js via C++. 
keywords: Rendre une ligne de grille solide en PDF Node.js via C++, convertir Excel en PDF avec ligne de grille solide via Node.js, PdfSaveOptions pour ligne de grille solide en Node.js via C++ 
---

Pour assurer la compatibilité avec les versions antérieures, Aspose.Cells rend par défaut les lignes de grille en traitillé lors de la conversion d'Excel en PDF. Cependant, les versions modernes d'Excel rendent les lignes de grille en trait plein aujourd'hui.

Avec l'option [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), Aspose.Cells for Node.js via C++ peut également rendre les lignes de grille en trait plein.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an empty Workbook
const wb = new AsposeCells.Workbook();

// Prepare data
wb.getWorksheets().get(0).getCells().get("D9").putValue("gridline");

// Enable to print gridline
wb.getWorksheets().get(0).getPageSetup().setPrintGridlines(true);

// Set to render gridline as solid line
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setGridlineType(AsposeCells.GridlineType.Hair);

// Save the pdf file with PdfSaveOptions
wb.save(path.join(dataDir, "test_Cs.pdf"), pdfSaveOptions);
```

![solid-gridline.png](solid-gridline.png)

