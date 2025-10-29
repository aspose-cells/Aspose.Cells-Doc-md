---
title: تحويل Excel إلى CSV و TSV و Txt مع Node.js عبر C++
linktitle: حفظ كـ CSV و TSV و Txt
type: docs
weight: 40
url: /ar/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: تعلم كيف تقوم بتحويل ملفات Excel إلى تنسيقات CSV و TSV و TXT باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يجعل Aspose.Cells من الممكن تحويل ملفات Excel و ODS و JSON والتنسيقات الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان، تريد تحويل أو حفظ دفتر عمل يتضمن أوراق عمل متعددة إلى صيغة نصية. بالنسبة للتنسيقات النصية (على سبيل المثال TXT، TabDelim، CSV، إلخ)، يقوم كل من Microsoft Excel و Aspose.Cells بشكل افتراضي بحفظ محتوى ورقة العمل النشطة فقط.

يوضح المثال التالي كيف تحفظ مصنفًا بالكامل بصيغة نصية. قم بتحميل المصنف المصدر، الذي يمكن أن يكون أي ملف جدول بيانات من Microsoft Excel أو OpenOffice (بما في ذلك XLS، XLSX، XLSM، XLSB، ODS، وغيرها) بعدد أوراق عمل مختلف.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بتنسيق CSV. بشكل افتراضي، [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) هو فاصلة، لذلك لا تحدد فاصل إذا كنت تريد الحفظ بتنسيق CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **مواضيع متقدمة**
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
