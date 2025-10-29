---
title: عرض خطوط الشبكة الصلبة أثناء تحويل إكسيل إلى PDF عبر Node.js باستخدام C++
linktitle: عرض خطوط الشبكة الصلبة أثناء تحويل إكسل إلى PDF
type: docs
weight: 390
url: /ar/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: تعلم كيفية عرض خطوط الشبكة الصلبة أثناء تحويل إكسيل إلى PDF باستخدام Aspose.Cells for Node.js via C++. 
keywords: عرض خطوط الشبكة الصلبة كـ PDF عبر Node.js باستخدام C++، تحويل إكسيل إلى PDF مع خطوط شبكة صلبة باستخدام Node.js عبر C++، خاصية PdfSaveOptions للخطوط الشبكية الصلبة عبر Node.js باستخدام C++ 
---

للتوافق مع الإصدارات القديمة، تقوم Aspose.Cells بشكل افتراضي برسم خطوط الشبكة كنقطة أثناء تحويل إكسيل إلى PDF. ومع ذلك، يعرّف إكسيل الحديثة خطوط الشبكة كخطوط صلبة اليوم.

باستخدام خيار [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)، يمكن لـ Aspose.Cells for Node.js via C++ أيضًا عرض خطوط الشبكة كخطوط صلبة.

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

{{< app/cells/assistant language="nodejs-cpp" >}}
