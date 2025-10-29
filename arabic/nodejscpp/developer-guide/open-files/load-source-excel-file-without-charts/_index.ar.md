---
title: تحميل ملف Excel المصدر بدون مخططات باستخدام Node.js عبر C++
linktitle: تحميل ملف Excel المصدر بدون رسوم بيانية
type: docs
weight: 420
url: /ar/nodejs-cpp/load-source-excel-file-without-charts/
description: تعلم كيفة تحميل ملف Excel بدون مخططات باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يسمح Aspose.Cells لك بتحميل ملف Excel الخاص بك بدون مخططات. يرجى استخدام الخاصية [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) لهذا الغرض.

{{% /alert %}}

## **تحميل جدول بيانات بدون رسوم بيانية**

يقوم الكود النموذجي التالي بتحميل ملف Excel النموذجي بدون مخططات وحفظه بتنسيق PDF الناتج.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
