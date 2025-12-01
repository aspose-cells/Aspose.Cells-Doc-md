---
title: Save Excel into PDF with Standard or Minimum Size using Node.js via C++
linktitle: Save Excel into PDF with Standard or Minimum Size
type: docs
weight: 340
url: /nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Learn how to save Excel files into PDF format with Standard or Minimum size using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

By default, Aspose.Cells saves Excel into PDF with Standard size. However, you can also save it with Minimum size using the [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) property. It accepts the following values:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Save Excel into PDF with Standard or Minimum Size using Aspose.Cells for Node.js via C++**
The following sample code shows how you can save Excel into PDF with Standard or Minimum size using the [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) property.

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
