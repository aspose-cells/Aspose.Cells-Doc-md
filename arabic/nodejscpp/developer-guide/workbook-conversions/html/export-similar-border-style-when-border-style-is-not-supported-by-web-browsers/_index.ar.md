---  
title: تصدير نمط حدود مماثل عندما لا يدعم نمط الحدود متصفحات الويب باستخدام Node.js عبر C++  
linktitle: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب  
type: docs  
weight: 70  
url: /ar/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: تعلم كيفية تصدير الحدود التي لا تدعمها متصفحات الويب عند تحويل ملفات Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يدعم Microsoft Excel بعض أنواع الحدود المنقطة التي لا تدعمها متصفحات الويب. عند تحويل مثل هذا الملف Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++، يتم إزالة هذه الحدود. ومع ذلك، يمكن لـ Aspose.Cells أيضًا دعم عرض مثل هذه الحدود باستخدام الخاصية [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--). يرجى تعيين قيمتها على **true** وستُصدر الحدود غير المدعومة أيضًا إلى ملف HTML.  

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**  

يوضح الكود النموذجي التالي تحميل [ملف إكسل النموذجي](64716806.xlsx) الذي يحتوي على بعض الحواف غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة بشكل إضافي تأثير خاصية [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) داخل [ملف HTML الناتج](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

