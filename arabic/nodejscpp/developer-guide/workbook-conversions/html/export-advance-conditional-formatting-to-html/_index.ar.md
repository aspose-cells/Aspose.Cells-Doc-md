---  
title: تصدير DataBar و ColorScale و IconSet التنسيق الشرطي أثناء تحويل Excel إلى HTML باستخدام Node.js عبر C++  
linktitle: تصدير تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز أثناء تحويل ملف Excel إلى HTML  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

 يمكنك تصدير DataBar و ColorScale و IconSet التنسيق الشرطي أثناء تحويل ملف Excel إلى HTML. يدعم هذا الميزة جزئياً Microsoft Excel، لكن Aspose.Cells for Node.js via C++ يدعمها بشكل كامل.

{{% /alert %}}  

## **تصدير DataBar، ColorScale و IconSet لتنسيق الشروط أثناء تحويل Excel إلى HTML**  
توضح اللقطة الشاشية التالية [ملف Excel عينة](5115558.xlsx) مع تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز. يمكنك تنزيل [ملف Excel العينة](5115558.xlsx) من الرابط المعطى.  

![todo:image_alt_text](conversion_1.png)  

توضح اللقطة الشاشية التالية ملف HTML الناتج من Aspose.Cells الذي يظهر تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز. كما يمكنك رؤية أنه يبدو تمامًا مثل [ملف Excel العينة](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **الكود المثالي**  
 يوضح رمز المثال التالي تحويل ملف Excel النموذجي إلى HTML وهو مجرد تحويل [Excel إلى HTML] عادي (/cells/ar/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
