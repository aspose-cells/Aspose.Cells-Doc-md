---
title: حساب عامل مقياس إعداد الصفحة باستخدام Node.js عبر C++
linktitle: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/nodejs-cpp/calculate-page-setup-scaling-factor/
description: يوفر هذا المقال رمزًا نموذجيًا يوضح كيفية استخدام واجهة برمجة تطبيقات Node.js مع C++ لحساب عامل مقياس إعداد الصفحة باستخدام خيار الملاءمة إلى ن صفحة(n) واسعة و م عالية من ورقة عمل Excel برمجياً.
keywords: الملاءمة إلى ن صفحة عرضية و م عالية لنظام Node.js عبر C++، حساب عامل مقياس إعداد الصفحة لنظام Node.js بواسطة C++
---

{{% alert color="primary" %}}

عند تعيين مقياس إعداد الصفحة باستخدام خيار **الملاءمة إلى ن صفحة(ات) عرضية و م عالية**، يقوم Microsoft Excel بحساب عامل مقياس إعداد الصفحة. يمكنك حساب الشيء نفسه باستخدام الخاصية [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--). تُرجع هذه الخاصية قيمة مزدوجة يمكن تحويلها إلى قيمة نسبة مئوية. على سبيل المثال، إذا كانت تُرجع 0.5 فهذا يعني أن عامل القياس هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
