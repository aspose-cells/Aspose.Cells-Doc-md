---
title: Enregistrer Excel en PDF avec taille standard ou minimale en utilisant Node.js via C++
linktitle: Enregistrer Excel en PDF avec une taille standard ou minimale
type: docs
weight: 340
url: /fr/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Apprenez comment sauvegarder des fichiers Excel au format PDF avec une taille standard ou minimale en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Par défaut, Aspose.Cells enregistre Excel en PDF avec une taille standard. Cependant, vous pouvez également l'enregistrer avec une taille minimale en utilisant la propriété [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). Elle accepte les valeurs suivantes :

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Enregistrer Excel en PDF avec taille standard ou minimale en utilisant Aspose.Cells for Node.js via C++**
Le code d'exemple suivant montre comment vous pouvez sauvegarder Excel en PDF avec une taille standard ou minimale en utilisant la propriété [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Load excel file into workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save into Pdf with Minimum size
const opts = new AsposeCells.PdfSaveOptions();
opts.setOptimizationType(AsposeCells.PdfOptimizationType.MinimumSize);

workbook.save(path.join(dataDir, "OptimizedOutput_out.pdf"), opts);
```
