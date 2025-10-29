---
title: تحميل وإدارة ملفات إكسل، OpenOffice، Json، Csv و Html
linktitle: فتح الملفات
type: docs
weight: 20
url: /ar/nodejs-cpp/loading-saving-and-managing/
description: مع Aspose.Cells، من السهل إنشاء، فتح، وإدارة ملفات إكسل، CSV، TSV، ODS، HTML، Numbers، Json، XML، Pdf، Jpg، Tiff، صورة، Mht، وXPS باستخدام Node.js عبر C++.
---

{{% alert color="primary" %}}

 مع Aspose.Cells، من السهل إنشاء، فتح، وإدارة ملفات إكسل، على سبيل المثال، لاسترجاع البيانات، أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **إنشاء مصنف جديد**
يُظهر المثال التالي إنشاء دفتر عمل جديد من الصفر.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **فتح وحفظ ملف**
 مع Aspose.Cells، من السهل فتح، حفظ، وإدارة ملفات إكسل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **مواضيع متقدمة**
- [طرق مختلفة لفتح الملفات](/cells/ar/nodejs-cpp/different-ways-to-open-files/)
- [تصفية أسماء محددة أثناء تحميل المصنف](/cells/ar/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [تصفية الكائنات أثناء تحميل مصنف العمل أو ورقة العمل](/cells/ar/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [تصفية نوع البيانات أثناء تحميل مصنف العمل من ملف القالب](/cells/ar/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [الحصول على تحذيرات أثناء تحميل ملف إكسل](/cells/ar/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [تحميل ملف Excel المصدر دون الرسوم البيانية](/cells/ar/nodejs-cpp/load-source-excel-file-without-charts/)
- [تحميل الأوراق العمل المحددة في كتيب عمل](/cells/ar/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [تحميل الدفتر بحجم ورقة الطابعة المحدد](/cells/ar/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [فتح ملفات Microsoft Excel مختلفة الإصدارات](/cells/ar/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [فتح الملفات بتنسيقات مختلفة](/cells/ar/nodejs-cpp/opening-files-with-different-formats/)
- [تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة](/cells/ar/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [قراءة جدول بيانات الأرقام المطور من قبل Apple Inc. باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً](/cells/ar/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [استخدام واجهة برمجة التطبيقات LightCells](/cells/ar/nodejs-cpp/using-lightcells-api/)
- [تحويل CSV إلى JSON](/cells/ar/nodejs-cpp/convert-csv-to-json/)
- [تحويل إكسل إلى JSON](/cells/ar/nodejs-cpp/convert-excel-to-json/)
- [تحويل JSON إلى CSV](/cells/ar/nodejs-cpp/convert-json-to-csv/)
- [تحويل JSON إلى إكسل](/cells/ar/nodejs-cpp/convert-json-to-excel/)
- [تحويل إكسل إلى Html](/cells/ar/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
