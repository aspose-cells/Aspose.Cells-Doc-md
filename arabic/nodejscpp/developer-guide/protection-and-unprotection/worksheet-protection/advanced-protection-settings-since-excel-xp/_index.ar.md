---
title: إعدادات الحماية المتقدمة منذ Excel XP مع Node.js عبر C++
linktitle: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

منذ إصدار Excel 2002 أو XP، أضافت Microsoft العديد من إعدادات الحماية المتقدمة.

{{% /alert %}}


## **مقدمة**

تقييد أو السماح للمستخدمين بـ:

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج صفوف أو أعمدة أو روابط تشعبية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

يدعم Aspose.Cells for Node.js via C++ جميع إعدادات الحماية المتقدمة التي تقدمها Excel XP أو الإصدارات الأحدث.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **أدوات**, اختر **الحماية** ثم **حماية الورقة**. سيتم عرض مربع الحوار.

لعرض إعدادات الحماية المتاحة في Excel 2016:

1. من القائمة **ملف**, اختر **حماية الدفتر** ثم **حماية الورقة الحالية**.
1. حدد **حماية الورقة** في قائمة **مراجعة**.

سيؤدي اتباع الخطوات المذكورة أعلاه إلى إظهار مربع حوار يمكنك من خلاله السماح أو تقييد ميزات ورقة العمل أو تطبيق كلمة مرور على ورقة العمل.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells for Node.js via C++**

يدعم Aspose.Cells for Node.js via C++ جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) خاصية [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) التي تُستخدم لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) هي في الواقع كائن لفئة [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) التي تحتوي على عدة خصائص بوليانية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

يرجى عدم استدعاء طريقة [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) من فصل [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) عند استخدام الخاصية [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). أيضًا، قم بحفظ الملف بصيغة Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط من Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد تحرير المستخدمين للخلايا، يجب قفل الخلايا قبل تطبيق أي إعدادات حماية. وإلا، يمكن تحرير الخلايا حتى وإن كانت ورقة العمل محمية. في Microsoft Excel XP، يمكن قفل الخلايا من خلال مربع الحوار التالي:

|**مربع الحوار لقفل الخلايا في Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن قفل الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells أيضًا. يمكن أن تحوي كل خلية تنسيق [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) يحتوي على خاصية Boolean، [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). قم بضبط الخاصية [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) على **true** أو **false** لقفل الخلية أو إلغاء قفلها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
