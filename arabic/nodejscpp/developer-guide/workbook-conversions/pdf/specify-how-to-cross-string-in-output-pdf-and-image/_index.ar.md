---  
title: تحديد كيفية عبور النص في PDF والصور المصدرة باستخدام Node.js عبر C++  
linktitle: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة  
type: docs  
weight: 120  
url: /ar/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: تعلم كيفية التحكم في تجاوز النص في ملف PDF/الصورة المصدرة عن طريق تحديد نوع العبور باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**

 عندما يحتوي خلية على نص أو سلسلة أكبر من عرض الخلية، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو غير موجودة. عند حفظ ملف Excel الخاص بك كـ PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). وله القيم التالية:

- **نوع تمرير النصافتراضي**: عرض النص مثل MS Excel يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، فسيتم تجاوز النص أو قطعه.

- **TextCrossType.CrossKeep**: عرض النص مثل تصدير MS Excel إلى PDF/صور.

- **TextCrossType.CrossOverride**: عرض كل النص عن طريق عبور خلايا أخرى وتجاوز نص الخلايا المعترضة.

- **TextCrossType.StrictInCell**: عرض السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يعرض الرمز النموذجي التالي تحميل ملف Excel النموذجي وحفظه إلى تنسيق PDF/صور عن طريق تحديد قيم مختلفة [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### مثال على الكود

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
