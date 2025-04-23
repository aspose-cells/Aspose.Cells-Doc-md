---
title: تلقائيًا وظيفة الأعمدة والصفوف أثناء تحميل HTML في Workbook باستخدام Node.js عبر C++
linktitle: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: تعرف على كيفية التلقائي لوضع الأعمدة والصفوف أثناء تحميل ملفات HTML في Workbook باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلقائيًا ضبط الأعمدة والصفوف أثناء تحميل ملف HTML الخاص بك داخل كائن Workbook. يرجى تعيين خاصية [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الرمز النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook دون خيارات تحميل ويحفظه بصيغة XLSX. ثم يعيد تحميل نفس HTML داخل Workbook ولكن هذه المرة مع تعيين خاصية [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) إلى **true**، ويحفظه بصيغة XLSX. الرجاء تنزيل كلا الملفين الناتجين، ملف إكسل بدون auto-fit وملف إكسل مع auto-fit. يظهر الشاشة التالية تأثير خاصية [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) على كلا الملفين.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

