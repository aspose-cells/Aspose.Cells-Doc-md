---  
title: نقل نطاق الخلايا في ورقة العمل باستخدام Node.js عبر C++  
linktitle: نقل مجموعة من الخلايا في ورقة العمل  
type: docs  
weight: 370  
url: /ar/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: تعلم كيفية نقل نطاق من الخلايا في ورقة عمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يوضح هذا المقال كيفية نقل مجموعة من الخلايا في ورقة العمل.  
{{% /alert %}}  

## **نقل مجموعة من الخلايا في ورقة العمل**  
يستخدم الشفرة المثالية ملف قالب لتوضيح المهمة.  

**ملف الإدخال**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

يرجى الاطلاع على الملف الناتج التالي بالنطاق A1:B5 المحرك إلى C1:D5.  

ملف الإخراج  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
