---
title: حذف الصفوف والأعمدة الفارغة في ورقة عمل باستخدام Node.js عبر C++
linktitle: حذف الصفوف والأعمدة الفارغة في ورقة العمل
type: docs
weight: 300
url: /ar/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: تعرف على كيفية حذف جميع الصفوف والأعمدة الفارغة من ورقة عمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. هذا مفيد عند إنشاء ملف PDF من ملف Microsoft Excel وترغب في تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائنات ذات علاقة فقط.

استخدم وسائل Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1. لحذف الصفوف الفارغة، استخدم الطريقة [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). يرجى ملاحظة أنه من الضروري للصفوف الفارغة التي سيتم حذفها أن يكون [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) صحيحًا، وأيضًا يجب ألا يكون هناك تعليق مرئي معرف لأي خلية في تلك الصفوف، ولا جدول محوري يتقاطع نطاقه معها.
2. لحذف الأعمدة الفارغة، استخدم الطريقة [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## كود Node.js لحذف الصفوف الفارغة

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## كود Node.js لحذف الأعمدة الفارغة

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
