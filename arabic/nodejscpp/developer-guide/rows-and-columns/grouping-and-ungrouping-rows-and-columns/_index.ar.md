---
title: تجميع وفك تجميع الصفوف والأعمدة باستخدام Node.js عبر C++
linktitle: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 50
url: /ar/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: اكتشف كيفية تجميع وفك تجميع الصفوف والأعمدة في Excel باستخدام Aspose.Cells for Node.js via C++.
--- 

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

|**تجميع الصفوف والأعمدة.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة تجميع الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف مايكروسوفت إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) الذي يسمح بالوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل، حيث سنناقش أدناه بعض هذه الطرق بمزيد من التفاصيل.

### **تجميع الصفوف والأعمدة**

من الممكن تجميع الصفوف أو الأعمدة عبر استدعاء طريقي [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) و[**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). كلا الطريقتين يقبل المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

يمكن للمطورين تكوين إعدادات التجميع هذه باستخدام خاصية [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

### **صفوف ملخصية أسفل التفاصيل**

من الممكن التحكم في ما إذا كانت صفوف الملخص تظهر أسفل التفاصيل عن طريق تعيين الخاصية [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) من فئة [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) إلى **true** أو **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **أعمدة ملخصية على يمين التفاصيل**

يمكن للمطورين أيضًا التحكم في عرض أعمدة الملخص إلى يمين التفاصيل من خلال تعيين الخاصية [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) من فئة [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) إلى **true** أو **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **إلغاء تجميع الصفوف والأعمدة**

لفك تجميع أي صفوف أو أعمدة مجمعة، استدعي طرق [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) و[**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). كلا الطريقتين يقبلان معلمين:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) لديه تحميل مفرط يأخذ معلمة ثالثة من نوع منطقي. تعيينها إلى **true** يزيل جميع المعلومات المجمعة. وإلا، يتم إزالة معلومات التجميع الخارجية فقط.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
