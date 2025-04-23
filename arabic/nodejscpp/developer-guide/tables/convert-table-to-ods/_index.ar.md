---  
title: تحويل الجدول إلى ODS باستخدام Node.js عبر C++  
linktitle: تحويل الجدول إلى ملف ODS  
type: docs  
weight: 70  
url: /ar/nodejs-cpp/convert-table-to-ods/  
description: تعلم كيفية تحويل ملف إكسل يحتوي على جدول إلى صيغة ODS باستخدام Aspose.Cells for Node.js via C++.  
---  

يدعم Aspose.Cells تحويل ملف Excel يحتوي على جدول إلى ملف ODS. عليك فقط حفظ الملف بتنسيق ODS وسيحتوي ملف ODS الناتج على جدول يعمل بشكل صحيح.

## كود عينة

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

الملف ODS الناتج من كود العينة مرفق للرجوع إليه.

[**Output ODS File**](ConvertTableToOds_out.ods)  

