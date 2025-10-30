---
title: Salva Excel in PDF con dimensione Standard o Minima usando Node.js tramite C++
linktitle: Salva Excel in PDF con dimensioni standard o minime
type: docs
weight: 340
url: /it/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Impara come salvare i file Excel in formato PDF con dimensione Standard o Minima usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Per impostazione predefinita, Aspose.Cells salva Excel in PDF con dimensione Standard. Tuttavia, puoi anche salvarlo con dimensione Minima usando la proprietà [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). Accetta i seguenti valori:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Salva Excel in PDF con dimensione Standard o Minima usando Aspose.Cells for Node.js via C++**
Il codice di esempio seguente mostra come puoi salvare Excel in PDF con dimensione Standard o Minima usando la proprietà [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
