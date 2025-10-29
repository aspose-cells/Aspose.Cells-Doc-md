---
title: إزالة إعدادات الطابعة الموجودة في أوراق العمل في ملف Excel باستخدام Node.js عبر C++
linktitle: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 60
url: /ar/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: في هذه المقالة، ستتعلم كيفية إزالة إعدادات الطابعة الموجودة لورقة العمل داخل ملف Excel برمجيًا باستخدام Aspose.Cells for Node.js via C++.
keywords: إزالة إعدادات الطابعة لورقة العمل باستخدام Node.js عبر C++، إزالة إعدادات الطابعة لورقة عمل Excel باستخدام Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يرغب المطورون في منع Excel من تضمين ملفات *.bin* لإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *“[file "root"]\xl\printerSettings”.* يوضح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام واجهة برمجة التطبيقات Aspose.Cells.

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تتيح Aspose.Cells إزالة إعدادات الطابعة الحالية المحددة لورقات العمل المختلفة في ملف Excel. يوضح الكود العينات التالية كيفية إزالة إعدادات الطابعة الحالية لجميع ورقات العمل في الدفتر. يرجى الاطلاع على [ملف Excel عينة](45056020.xlsx)، [ملف Excel الناتج](45056021.xlsx)، الإخراج على وحدة التحكم، فضلاً عن اللقطة للإشارة.

## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **الكود المثالي**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");
const wb = new AsposeCells.Workbook(filePath);

// Get the sheet counts of the workbook
const sheetCount = wb.getWorksheets().getCount();

// Iterate all sheets
for (let i = 0; i < sheetCount; i++) {
// Access the i-th worksheet
const ws = wb.getWorksheets().get(i);

// Access worksheet page setup
const ps = ws.getPageSetup();

// Check if printer settings for this worksheet exist
if (ps.getPrinterSettings() != null) {
// Print the following message
console.log("PrinterSettings of this worksheet exist.");

// Print sheet name and its paper size
console.log("Sheet Name: " + ws.getName());
console.log("Paper Size: " + ps.getPaperSize());

// Remove the printer settings by setting them null
ps.setPrinterSettings(null);
console.log("Printer settings of this worksheet are now removed by setting it null.");
console.log("");
} // if
} // for

// Save the workbook
wb.save(path.join(outputDir, "outputRemoveExistingPrinterSettingsOfWorksheets.xlsx"));
```

## **مخرجات الوحدة**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
