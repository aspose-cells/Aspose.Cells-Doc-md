---  
title: نسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline باستخدام Node.js عبر C++  
linktitle: نسخة الشرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط  
type: docs  
weight: 300  
url: /ar/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: تعلم كيفية نسخ خط فاصل في إكسل عن طريق تحديد نطاق البيانات وموقع مجموعة خطوط الفاصل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يسمح Microsoft Excel لك بنسخ شرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط. تدعم Aspose.Cells هذه الميزة.  
{{% /alert %}}  

لنسخ الشرارة إلى خلايا أخرى في Microsoft Excel:  

1. حدد الخلية التي تحتوي على الشرارة.  
1. حدد **Edit Data** من **قسم Sparkline** من **tDesign** علامة التبويب.  
1. حدد **Edit Group Location & Data**.  
1. حدد نطاق البيانات والموقع.  
1. انقر على **موافق**.  

توفر Aspose.Cells طريقة `SparklineCollection.add(dataRange, row, column)` لتحديد نطاق البيانات وموقع مجموعة خطوط الفاصل. ترفع الكود النموذجي التالي ملف إكسل المصدر كما هو موضح في الصورة أعلاه، ثم يصل إلى مجموعة خطوط الفاصل الأولى ويضيف نطاقات البيانات والمواقع في مجموعة خطوط الفاصل. وأخيرًا، يكتب ملف إكسل الناتج على القرص والذي يظهر أيضًا في الصورة أعلاه.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

