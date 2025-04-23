---
title: إنشاء معاينة مصغرة للورقة باستخدام Node.js عبر C++
linktitle: إنشاء صورة مصغرة لورقة العمل
type: docs
weight: 110
url: /ar/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: تعلم كيفية إنشاء صورة مصغرة من ورقة عمل باستخدام Aspose.Cells for Node.js via C++. لإنشاء صور صغيرة للمراجعات في المستندات والعروض التقديمية.
---

{{% alert color="primary" %}} 

يمكن أن يكون من المفيد إنشاء صور مصغرة من ورقة العمل. الصورة المصغرة هي صورة صغيرة يمكن لصقها في مستند Word أو عرض تقديمي بوربوينت لإعطاء معاينة لمحتوى ورقة العمل. يمكن إضافتها إلى صفحة الويب مع رابط لتنزيل الوثيقة الأصلية ولها العديد من الاستخدامات الأخرى.

{{% /alert %}} 

يمكّنك Aspose.Cells for Node.js via C++ من إخراج أوراق العمل إلى ملفات صور، مما يسهل عمل صورة مصغرة. يوضح لك رمز المثال أدناه كيف تُصدر أوراق العمل إلى ملفات صور.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
