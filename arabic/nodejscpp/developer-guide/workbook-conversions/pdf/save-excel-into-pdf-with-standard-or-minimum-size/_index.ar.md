---
title: حفظ ملف Excel كملف PDF باستخدام الحجم القياسي أو الأدنى باستخدام Node.js عبر C++
linktitle: حفظ Excel إلى PDF بحجم قياسي أو حد أدنى
type: docs
weight: 340
url: /ar/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: تعلم كيف تحفظ ملفات Excel بصيغة PDF بالحجم القياسي أو الأدنى باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

 بشكل افتراضي، يحفظ Aspose.Cells Excel إلى PDF بالحجم القياسي. ومع ذلك، يمكنك أيضًا حفظه بالحجم الأدنى باستخدام خاصية [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--). يقبل القيم التالية:

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **حفظ Excel كملف PDF بالحجم القياسي أو الأدنى باستخدام Aspose.Cells for Node.js via C++**
يعرض الكود النموذجي التالي كيف يمكنك حفظ Excel كملف PDF بالحجم القياسي أو الأدنى باستخدام خاصية [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--).

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
