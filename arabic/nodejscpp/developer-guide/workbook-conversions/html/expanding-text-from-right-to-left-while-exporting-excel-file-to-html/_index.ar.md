---  
title: توسيع النص من اليمين لليسار أثناء تصدير ملف Excel إلى HTML باستخدام Node.js عبر C++  
linktitle: توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells الآن تدعم توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML. تم تنفيذ هذه الميزة منذ الإصدار v8.9.0.0. الآن إذا كان ملف excel الخاص بك يحتوي على أي نص يتم توسيعه من اليمين إلى اليسار، فسيقوم Aspose.Cells بتصديره إلى HTML بشكل صحيح.  

{{% /alert %}}  
## **توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML**  
الشيفرة النموذجية التالية تحول [ملف excel عينة](5115502.xlsx) إلى HTML. تظهر هذه اللقطة الشاشة كيفية شكل ملف excel العينة في Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

تظهر هذه اللقطة الشاشة [HTML الناتج المولد بالإصدار القديم](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

تظهر هذه اللقطة الشاشة [HTML الناتج المولد بالإصدار الجديد](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

كما ترون في اللقطات الشاشة، الإصدار الجديد يوسع النص المُمحى إلى اليسار بشكل صحيح تماماً مثل Microsoft Excel.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

