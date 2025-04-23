---
title: تحويل JSON إلى Excel باستخدام Node.js عبر C++
linktitle: تحويل JSON إلى Excel
type: docs
weight: 300
url: /ar/nodejs-cpp/convert-json-to-excel/
description: تعلم كيفية تحويل JSON إلى ملف Excel باستخدام Aspose.Cells for Node.js via C++.
keywords: استيراد JSON بدون استخدام Office 2013، Office 2016، Office 2019، و Office 365 باستخدام Node.js عبر C++.
---

{{% alert color="primary" %}}

 يدعم Aspose.Cells تحويل ملف JSON (ترميز كائن جافا سكريبت) إلى مصنف Excel.

{{% /alert %}}

## **تحويل-JSON-إلى-كتاب-عمل-Excel**
 لا حاجة للتساؤل عن كيفية تحويل JSON إلى ملف Excel، لأن Aspose.Cells for Node.js via C++ توفر الحل الأمثل. تقدم واجهة برمجة التطبيقات Aspose.Cells دعمًا لتحويل صيغة JSON إلى جداول بيانات. يمكنك استخدام فئة [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) لتحديد إعدادات إضافية لاستيراد JSON إلى المصنف.

يوضح المثال الكودي التالي استيراد JSON إلى دفتر عمل Excel. يرجى الرجوع إلى الكود الخاص بتحويل الملف المصدر إلى ملف xlsx الذي تم إنشاؤه بالكود للإحالة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

يوضح المثال التالي باستخدام فئة JsonLoadOptions لتحديد إعدادات إضافية، استيراد JSON إلى مصنف Excel. يرجى مراجعة الكود لتحويل [الملف المصدر](sample.json) إلى ملف xlsx الناتج بواسطة الكود.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

 يوضح المثال التالي استيراد سلسلة JSON إلى مصنف Excel. يمكنك أيضًا تحديد موقع التخطيط عند استيراد JSON. يرجى مراجعة الكود لتحويل سلسلة JSON إلى ملف xlsx الناتج بواسطة الكود.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
