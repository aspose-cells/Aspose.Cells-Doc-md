---
title: تحويل دفتر عمل Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice calc) عبر Node.js
linktitle: Ods
type: docs
weight: 20
url: /ar/nodejs-cpp/convert-excel-to-ods/
description: كيفية تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc) أو تحويل Ods (OpenOffice / LibreOffice Calc) إلى Excel باستخدام Aspose.Cells for Node.js via C++.
---

## **حول OpenDocument**
[تنسيق OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) هو تنسيق ملف مجاني ومفتوح للوثائق المكتبية الإلكترونية الذي طوّره الأصل لـ OpenOffice suite. تنسيق الجدول الخلية OpenDocument (ODS) هو تنسيق الملفات لوثائق Excel. حاليًا يُعتبر OpenDocument معيارًا لـ OASIS و ISO.

## **تحويل Ods (OpenOffice / LibreOffice calc) إلى Excel**
يدعم Aspose.Cells for Node.js via C++ تحميل ملفات Ods، Sxc و Fods المدعومة من قبل OpenOffice / LibreOffice Calc، وتحويل [Ods](book1.ods)، [Sxc](book1.sxc) و [Fods](book1.fods) إلى ملفات Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc)**
يدعم Aspose.Cells for Node.js via C++ تحويل ملفات Excel إلى ملفات Ods، Sxc و Fods. يوضح المثال التالي كيفية تحويل [نموذج](book1.xlsx) إلى ملفات Ods و Sxc و Fods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **مواضيع متقدمة**
- [حفظ ملف ODS بمواصفات ODF 1.1 و 1.2](/cells/ar/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [العمل مع الخلفية في ملفات ODS](/cells/ar/nodejs-cpp/working-with-background-in-ods-files/)
