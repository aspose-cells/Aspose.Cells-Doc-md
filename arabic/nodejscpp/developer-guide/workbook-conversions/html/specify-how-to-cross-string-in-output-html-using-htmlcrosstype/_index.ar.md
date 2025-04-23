---
title: تحديد كيفية عبور السلسلة النصية في HTML الناتج باستخدام HtmlCrossType مع Node.js عبر C++
linktitle: تحديد كيفية عبور النص في ملف الـHTML الناتج باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: تعلم كيفية التحكم في تجاوز النص في HTML الناتج عن طريق تحديد HtmlCrossType في Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عندما يحتوي الخلية على نص أو سلسلة لكن أكبر من عرض الخلية، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو لا تحتوي على شيء. عند حفظ ملف Excel كـ HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تعداد [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). يحتوي على القيم التالية:

- **HtmlCrossType.Default**: عرض مثل MS Excel؛ يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، فإن النص سيعبر أو سيتم اقتطاعه.

- **HtmlCrossType.MSExport**: عرض النص كما في تصدير HTML من برنامج MS Excel.

- **HtmlCrossType.Cross**: عرض النص عبر HTML؛ الأداء لإنشاء ملفات HTML كبيرة سيكون أكثر من عشرة أضعاف أسرع من تعيين القيمة إلى Default أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض النص فقط ضمن عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](51740732.xlsx) وتخزينه بتنسيق HTML عن طريق تحديد قيم [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) المختلفة. يرجى تنزيل [ملفات HTML الناتجة](51740734.zip) التي تم إنشاؤها باستخدام هذه الشفرة. يحتوي ملف Excel النموذجي على صورة محاطة باللون الأحمر كما هو موضح في لقطة الشاشة التي توضح تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) على HTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
