---
title: ضبط عرض العمود كوحدة قابلة للتكبير مثل em أو النسبة المئوية باستخدام Node.js عبر C++
linktitle: ضبط عرض العمود كوحدة قابلة للتكبير مثل em أو النسبة المئوية
type: docs
weight: 130
url: /ar/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: تعلم كيفية تعيين عرض العمود بوحدات قابلة للتطوير مثل em أو النسبة المئوية في Aspose.Cells for Node.js via C++. تحسين عرض جداول HTML المولدة.
---

إنشاء ملف HTML من جدول بيانات أمر شائع جدًا. حجم الأعمدة معرف بواسطة "نقطة"، والذي يعمل في العديد من الحالات. ومع ذلك، قد يكون هناك حالة لا يتطلب فيها هذا الحجم الثابت. على سبيل المثال، إذا كان عرض لوحة الحاوية هو 600 بكسل، حيث يتم عرض صفحة HTML هذه، فقد تحصل على شريط تمرير أفقي إذا كان عرض الجدول المولد أكبر. كان من المطلوب تحويل هذا الحجم الثابت إلى وحدة قابلة للتطوير مثل em أو النسبة المئوية للحصول على عرض أفضل. يمكن استخدام الشفرة النموذجية التالية حيث يتم تعيين [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) إلى **true** لإنشاء عرض قابل للتطوير.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
