---
title: Spara Excel till PDF med Standard eller Minsta storlek med Node.js via C++
linktitle: Spara Excel som PDF med standard eller minsta storlek
type: docs
weight: 340
url: /sv/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Lär dig hur man sparar Excel filer till PDF format med standard eller minsta storlek med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Som standard sparar Aspose.Cells Excel till PDF med standardstorlek. Du kan dock också spara det med minsta storlek med hjälp av egenskapen [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). Den accepterar följande värden:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Spara Excel till PDF med standard- eller minsta storlek med Aspose.Cells for Node.js via C++**
Följande exempel visar hur du kan spara Excel till PDF med standard- eller minsta storlek med hjälp av egenskapen [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--).

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
