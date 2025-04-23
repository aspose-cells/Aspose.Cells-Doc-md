---
title: Excel إلى HTML  استخدم خيار تفضيل العرض لتحسين التخطيط باستخدام Node.js عبر C++
linktitle: Excel to HTML  استخدام خيار PresentationPreference لتحسين التخطيط
type: docs
weight: 220
url: /ar/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells خاصية HtmlSaveOptions.presentationPreference المفيدة للمطورين الذين يحتاجون إلى عرض تخطيط أفضل عند حفظ ملف Microsoft Excel إلى تنسيق HTML أو MHT. القيمة الافتراضية لهذه الخاصية هي false. نوصي بضبطها إلى true للحصول على عرض تقديمي أكثر جاذبية للتقارير Excel.

{{% /alert %}} 

يرجى مراجعة رمز المثال أدناه الذي يوضح كيفية عرض تقرير Excel باستخدام تفضيل العرض على.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
