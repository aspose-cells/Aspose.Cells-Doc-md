---
title: تعطيل تصدير إطارات البرمجيات وخصائص المستند مع Node.js عبر C++
linktitle: تعطيل تصدير الإطارات النصية وخصائص المستند
type: docs
weight: 310
url: /ar/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: تعلم كيفية تعطيل تصدير إطارات البرمجيات وخصائص المستند عند تحويل ملف Workbook إلى HTML باستخدام Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

يقوم Aspose.Cells بتصدير إطارات البرمجيات وخصائص المستند عند تحويل ملف Workbook إلى HTML. النسخة 8.6.0 من Aspose.Cells for Node.js via C++ تقدم خيارًا يتيح لك تعطيل تصدير إطارات البرمجيات وخصائص المستند بشكل اختياري. يرجى استخدام الخاصية `HtmlSaveOptions.exportFrameScriptsAndProperties` لتعطيل التصدير.

{{% /alert %}}

## **تعطيل تصدير الإطارات النصية وخصائص المستند**

الشيفرة النموذجية التالية تتيح لك تعطيل تصدير الإطارات النصية وخصائص المستند. بمجرد تحويل دفتر العمل إلى HTML، لن يحتوي الملف الناتج على أي إطارات نصية أو خصائص مستند.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
