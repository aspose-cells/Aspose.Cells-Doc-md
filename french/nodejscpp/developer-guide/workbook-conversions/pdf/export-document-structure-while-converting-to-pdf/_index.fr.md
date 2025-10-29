---
title: Exporter la structure du document lors de la conversion en PDF avec Node.js via C++
linktitle: Exporter la structure du document lors de la conversion en PDF
type: docs
weight: 360
url: /fr/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Apprenez comment exporter la structure du document lors de la conversion d un fichier Excel en PDF balisé en utilisant Aspose.Cells for Node.js via C++. 
---

Les facilités de structure logique PDF offrent un mécanisme pour intégrer des informations concernant la structure du contenu du document dans un fichier PDF. Aspose.Cells for Node.js via C++ conserve les informations sur la structure depuis un document Microsoft Excel, comme la cellule, la ligne, le tableau, la feuille de calcul, l'image, la forme, l'en-tête/pied de page, etc.

Avec l'option [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) vous pouvez enregistrer dans un PDF balisé avec la structure du document exportée.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
