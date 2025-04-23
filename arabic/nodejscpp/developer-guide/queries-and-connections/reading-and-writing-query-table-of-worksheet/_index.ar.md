---
title: قراءة وكتابة جدول الاستعلام من ورقة العمل باستخدام Node.js عبر C++
linktitle: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 40
url: /ar/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

توفر Aspose.Cells مجموعة Worksheet.QueryTables التي تعيد كائن نوع QueryTable عن طريق الفهرس. لديها الخاصيةان التالية

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

هذه قيم بوليانيتين. يمكنك مشاهدتها في Microsoft Excel عبر Data > Connections > Properties.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام لورقة العمل

يقرأ المثال التالي أول جدول استعلام من أول ورقة عمل ثم يطبع خصائص جدول الاستعلام. ثم يضبط خاصية preserveFormatting إلى true.

يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [ملف Excel المصدر](5115533.xlsx)
- [ملف Excel الناتج](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### إخراج الكونسول

إليك إخراج الكونسول للكود العيني أعلاه

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرداد نطاق نتيجة جدول الاستعلام

توفر Aspose.Cells خيار قراءة العنوان أي نطاق نتائج الخلايا لجدول الاستعلام. يُظهر الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل الملف النموذجي من [هنا](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
