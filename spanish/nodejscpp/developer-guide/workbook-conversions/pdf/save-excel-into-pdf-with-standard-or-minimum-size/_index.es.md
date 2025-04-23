---
title: Guardar Excel en PDF con tamaño estándar o mínimo usando Node.js vía C++
linktitle: Guardar Excel en PDF con Tamaño Estándar o Mínimo
type: docs
weight: 340
url: /es/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aprende cómo guardar archivos Excel en formato PDF con tamaño estándar o mínimo usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Por defecto, Aspose.Cells guarda Excel en PDF con tamaño estándar. Sin embargo, también puedes guardarlo con tamaño mínimo usando la propiedad [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). Acepta los siguientes valores:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Guardar Excel en PDF con tamaño estándar o mínimo usando Aspose.Cells for Node.js via C++**
El siguiente código de ejemplo muestra cómo puedes guardar Excel en PDF con tamaño estándar o mínimo usando la propiedad [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--).

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
