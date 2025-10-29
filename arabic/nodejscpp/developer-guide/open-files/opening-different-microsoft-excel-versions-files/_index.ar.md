---
title: فتح ملفات إكسل من إصدارات مختلفة باستخدام Node.js عبر C++
linktitle: فتح ملفات إكسل من إصدارات مايكروسوفت المختلفة
type: docs
weight: 20
url: /ar/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: يشرح هذا المقال كيفية فتح ملفات إكسل مختلفة الإصدارات باستخدام Aspose.Cells for Node.js via C++.
keywords: Node.js فتح ملفات إكسل مختلفة باستخدام C++، كيف أفتح ملفات إكسل مشفرة بواسطة Node.js عبر C++
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **كيفية فتح ملفات من إصدارات مايكروسوفت إكسل المختلفة**

غالبًا، يتوجب على التطبيق أن يكون قادرًا على فتح ملفات إكسل التي تم إنشاؤها بواسطة إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95، 97، أو Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365. قد تحتاج إلى تحميل ملف بصيغة من بين عدة تنسيقات، بما في ذلك XLS، XLSX، XLSM، XLSB، SpreadsheetML، TabDelimited أو TSV، CSV، ODS وغيرها. استخدم المنشئ، أو حدد سمة نوع [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) للفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تحدد الشكل باستخدام تعداد [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype).

تحتوي تعداد [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) على العديد من صيغ الملفات المعرفة مسبقًا، وأحدها مذكور أدناه.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|Csv| يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
|Xlsx| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSX|
|Xlsm| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSM|
|Xltx|يمثل ملف XLTX قالب Excel 2007/2010/2013/2016/2019 و Office 365|
|Xltm|يمثل ملف XLTM Excel 2007/2010/2013/2016/2019 و Office 365 القادر على تشغيل الماكرو|
|Xlsb|يمثل ملف XLSB بتنسيق Excel 2007/2010/2013/2016/2019 و Office 365|
|SpreadsheetML|يمثل ملف SpreadsheetML|
|Tsv|يمثل ملف بقيم مفصولة بواسطة علامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|Ods|يمثل ملف ODS|
|Html|يمثل ملف HTML|
|Mhtml|يمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) واضبط السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) لملف النموذج ليتم تحميله. يمكنك تنزيل ملف اختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) واضبط السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) لملف النموذج ليتم تحميله.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 بصيغة XLSX**

لفتح صيغة Microsoft Excel 2007/2010/2013/2016/2019 و Office 365، وهي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) وضبط السمة/الخيار ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) لملف النموذج ليتم تحميله.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **فتح ملفات Excel المشفرة**

من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) وضبط سماته وخياراته (على سبيل المثال، إعطاء كلمة مرور) لملف النموذج ليتم تحميله.
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

تدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel 2007، 2010، 2013، 2016، 2019، Office 365 المحمية بكلمة مرور.


{{< app/cells/assistant language="nodejs-cpp" >}}
