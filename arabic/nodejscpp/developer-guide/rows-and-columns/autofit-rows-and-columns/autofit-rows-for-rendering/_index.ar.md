---  
title: التمطيط التلقائي للصفوف للعرض باستخدام Node.js عبر C++  
linktitle: تحجيم الصفوف تلقائيًا للتقديم  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/autofit-rows-for-rendering/  
description: تعلم كيفية التمطيط التلقائي للصفوف للعرض في إكسل باستخدام Aspose.Cells for Node.js via C++. يمنع تقطيع النص في ملفات PDF المحفوظة.  
---  

عموماً، عندما تريد عرض كل النص في خلية، يمكنك التمطيط التلقائي للصف في العرض العادي باستخدام تكبير 100% في مايكروسوفت إكسل. هذا يسمح برؤية النص بالكامل بشكل كامل في العرض العادي، وحتى عند الطباعة أو حفظ الملف كـ PDF، سيتم عرض النص بشكل صحيح.

ومع ذلك، في بعض الحالات، يعمل التمطيط التلقائي للصف بشكل جيد في العرض العادي، ولكن عند التبديل إلى عرض الطباعة أو حفظ الملف كـ PDF، يتم قطع النص. يرجى مراجعة الملف المصدر [Book1.xlsx](Book1.xlsx) ولقطات الشاشة.

![تم قص النص في عرض الطباعة](text_clipped_in_printview.png)

إذا كنت ترغب في منع قطع النص في ملف PDF المحفوظ، يمكنك التمطيط التلقائي للصف باستخدام خيار [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

الآن، لم يتم قص النص في ملف PDF الناتج.

![النص لم يتم قصه في ملف PDF المحفوظ](text_not_clipped_in_saved_pdf.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
