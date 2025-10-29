---
title: تعطيل CSS عند الحفظ إلى HTML باستخدام Node.js عبر C++
linktitle: تعطيل CSS عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/nodejs-cpp/disable-css-while-saving-to-html/
description: تعلم كيفية تعطيل CSS عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك كصفحة HTML واحدة، عادةً ستكون عناصر CSS مضمنة داخل ملف HTML وستكون موجودة في قسم HEAD. إذا قمت بإرفاق هذا الملف كمحتوى/جسم لرسالة بريد إلكتروني، فسيتم مسح عناصر CSS بواسطة معظم عملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. تقدم نسخة 24.12 من Aspose.Cells خيارًا يسمح بك إلغاء تفعيل CSS بشكل اختياري، مما يتيح تطبيق الأنماط مباشرة داخل عناصر HTML نفسها. إذا كنت تريد تعيين HTML كمحتوى/جسم للبريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) وتعيينها إلى **true**.

## **تعطيل CSS عند الحفظ إلى HTML**

يعرض مثال الكود التالي استخدام الخاصية [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
