---
title: Excel in PDF mit Standard oder minimaler Größe speichern mit Node.js über C++
linktitle: Excel in PDF mit Standard oder Minimalgröße speichern
type: docs
weight: 340
url: /de/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Erfahren Sie, wie Sie Excel Dateien mit Standard oder Minimalgröße in das PDF Format mit Aspose.Cells for Node.js via C++ speichern.
---

{{% alert color="primary" %}} 

Standardmäßig speichert Aspose.Cells Excel als PDF im Standardformat. Sie können es jedoch auch mit Minimalgröße speichern, indem Sie die Eigenschaft [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) verwenden. Diese akzeptiert die folgenden Werte:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Excel in PDF mit Standard- oder Minimalgröße speichern mit Aspose.Cells for Node.js via C++**
Das folgende Beispiel zeigt, wie Sie Excel mit Standard- oder Minimalgröße mit der Eigenschaft [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) in PDF speichern können.

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
