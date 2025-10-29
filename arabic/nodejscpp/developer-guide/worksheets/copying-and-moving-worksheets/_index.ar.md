---
title: نسخ ونقل أوراق العمل باستخدام Node.js عبر C++
linktitle: نسخ ونقل ورقات العمل
type: docs
weight: 10
url: /ar/nodejs-cpp/copying-and-moving-worksheets/
description: تتضمن هذه المقالة رمز نموذج وتصف كيفية نسخ ونقل أوراق العمل برمجياً داخل مصنف إكسل وعبر مصنفات إكسل باستخدام واجهة برمجة التطبيقات Node.js مع C++.
keywords: نسخ ورقة عمل Node.js، نقل ورقة عمل Node.js
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى عدد من ورقات العمل مع تنسيقات وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الفصلية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة لفعل ذلك: من خلال إنشاء ورقة واحدة ثم نسخها.

يدعم Aspose.Cells for Node.js via C++ نسخ ونقل أوراق العمل داخل أو بين المصنفات. يتم نسخ الورقة، مع البيانات والتنسيقات والجداول والمصفوفات والمخططات والصور وغيرها من الكائنات بأعلى درجات الدقة.

{{% /alert %}}

## **نقل أو نسخ الأوراق باستخدام Microsoft Excel**

فيما يلي الخطوات اللازمة لنسخ ونقل أوراق العمل داخل أو بين دفاتر العمل في Microsoft Excel.

1. لنقل أو نسخ الأوراق إلى دفتر العمل الآخر، افتح دفتر العمل الذي سيتلقى الأوراق.
1. انتقل إلى دفتر العمل الذي يحتوي على الأوراق التي ترغب في نقلها أو نسخها، ثم حدد الأوراق.
1. في قائمة **تحرير**، انقر فوق **نقل أو نسخ الصفحة**.
4. في مربع الحوار **إلى مصنف**، انقر فوق المصنف الذي سيستقبل الصفحات.
5. لنقل أو نسخ الصفحات المحددة إلى مصنف جديد، انقر فوق **مصنف جديد**.
1. في مربع **قبل الصفحة**، انقر فوق الصفحة التي ترغب في إدراج الصفحات المنقولة أو المنسوخة قبلها.
7. لنسخ الصفحات بدلاً من نقلها، حدد مربع الاختيار **إنشاء نسخة**.

### **نسخ أوراق العمل داخل مصنف باستخدام Aspose.Cells for Node.js via C++**

توفر Aspose.Cells طريقة متحملة، [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-)، يتم استخدامها لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إحدى الإصدارات من الطريقة تأخذ فهرس الورقة المصدر كمعلمة. الإصدار الآخر يأخذ اسم الورقة المصدر.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **نسخ أوراق العمل بين دفاتر العمل**

توفر Aspose.Cells طريقة [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) لنسخ البيانات والتنسيقات من ورقة عمل مصدر إلى ورقة أخرى داخل أو بين المصنفات. تأخذ الطريقة كائن ورقة عمل المصدر كمعامل.

يظهر المثال التالي كيفية نسخ ورقة عمل من دفتر عمل إلى دفتر عمل آخر.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

المثال التالي يوضح كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **نقل أوراق العمل داخل الدفتر**

توفر Aspose.Cells طريقة [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) التي تُستخدم لنقل ورقة عمل إلى موقع آخر في نفس جدول البيانات. تأخذ الطريقة فهرس ورقة العمل الهدف كمعامل.

المثال التالي يظهر كيفية نقل ورقة عمل إلى موقع آخر داخل سجل العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
