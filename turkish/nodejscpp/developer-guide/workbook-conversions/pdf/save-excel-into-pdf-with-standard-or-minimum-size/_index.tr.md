---
title: Standart veya En Küçük Boyut ile Excel i PDF olarak kaydetmek Node.js ve C++ kullanarak
linktitle: Excel i Standart veya Minimum Boyutlu PDF ye Kaydetme
type: docs
weight: 340
url: /tr/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını Standart veya En Küçük boyutta PDF formatında kaydetmeyi öğrenin.
---

{{% alert color="primary" %}} 

Varsayılan olarak, Aspose.Cells Excel'i Standart boyutta PDF olarak kaydeder. Ancak, minimum boyut için de kaydedebilirsiniz. [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) özelliğiyle kullanılır. Aşağıdaki değerleri kabul eder:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Excel'i Standart veya Minimum Boyutta PDF olarak kaydetmek Aspose.Cells for Node.js via C++ kullanarak**
Aşağıdaki örnek kod, [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) özelliği kullanılarak Excel'i Standart veya Minimum boyutta PDF'ye nasıl kaydedeceğinizi gösteriyor.

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
