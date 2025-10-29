---  
title: تجاهل الأخطاء أثناء عرض إكسيل على PDF عبر Node.js باستخدام C++  
linktitle: تجاهل الأخطاء أثناء تحويل Excel إلى PDF  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: تعلم كيفية تجاهل الأخطاء أثناء تحويل ملفات إكسيل إلى PDF باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

أحيانًا عند تحويل ملف إكسيل إلى PDF، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل جميع هذه الأخطاء أثناء عملية التحويل باستخدام خاصية [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--). وبهذا، ستكتمل عملية التحويل بسلاسة دون إظهار أي خطأ أو استثناء، ولكن قد يحدث فقدان للبيانات. لذا، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات مهمًا بالنسبة لك.  

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**  

الكود التالي يحمل ملف إكسيل نمونه (sample Excel file) ولكن الملف يحتوي على أخطاء ويثير خطأ أثناء التحويل إلى PDF في 17.11، ولكن نظرًا لاستخدامنا خاصية [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--)، فلا يثير الخطأ. ومع ذلك، فإن شكل سهم أحمر مستدير مماثل كما في لقطة الشاشة يُفقد.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
