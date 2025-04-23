---
title: فتح الملفات بصيغ مختلفة باستخدام Node.js عبر C++
linktitle: فتح الملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/nodejs-cpp/opening-files-with-different-formats/
description: يتيح API Aspose.Cells for Node.js via C++ فتح/قراءة صيغ مختلفة مثل XLSX و HTML و CSV و ODS و TSV و SXC و FODS، وغيرها.
keywords: فتح ملفات xlsx، فتح ملفات html، قراءة ملفات fods، قراءة ملفات ods، قراءة ملفات sxc، فتح ملفات csv، ملفات قيم منفصلة بواسطة الفاصلة، صيغة SpreadsheetML، tsv، mhtml
---

{{% alert color="primary" %}}

باستخدام Aspose.Cells، يمكنك فتح ملفات بصيغ مختلفة. يمكن لـ **Aspose.Cells** فتح مجموعة من تنسيقات الملفات مثل جداول بيانات Microsoft Excel (XLS، XLSX، XLSM، XLSB)، SpreadsheetML، القيم مفصولة بفواصل (CSV)، ملفات مفصولة بعلامة تبويب (TSV)، وغيرها.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة، يرجى الرجوع إلى الصفحات التالية:
[الصيغ المدعومة للملفات](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **فتح الملفات بتنسيقات مختلفة**

تتيح Aspose.Cells للمطورين فتح ملفات جداول بيانات بتنسيقات مختلفة مثل SpreadsheetML، قيم منفصلة بواسطة الفاصلة (CSV)، قيم منفصلة بواسطة الفاصلة أو الفواصل (TSV)، ملفات ODS. يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات إصدارات مختلفة من Microsoft Excel لفتح مثل تلك الملفات.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات تتضمن كافة المعلومات عنها، مثل التنسيق والصيغ، وغيرها. منذ إصدار Microsoft Excel XP، أُضيف خيار تصدير XML إلى Microsoft Excel الذي يصدر جداول البيانات إلى ملفات SpreadsheetML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **فتح ملفات HTML**

يسمح Aspose.Cells لك بفتح ملف HTML إلى كائن Workbook. يجب أن يكون ملف HTML موجهًا نحو Microsoft Excel، أي أن MS-Excel يجب أن يكون قادرًا على فتحه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **فتح ملفات CSV**

ملفات القيم المفصولة بفواصل (CSV) تحتوي على سجلات تفصل بين القيم بواسطة الفاصلة. تُخزن البيانات في جدول حيث يتم فصل كل عمود بواسطة الحرف الفاصلة ويوضع بين علامتي اقتباس مزدوجتين. إذا احتوى حقل على علامة اقتباس مزدوجة، يتم الهروب منها بمزوج من علامتي اقتباس مزدوجتين. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات الجدول إلى CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

عند فتح ملف CSV يحتوي على أحرف خاصة في Excel، يتم استبدال الأحرف تلقائيًا. يتم ذلك أيضًا بواسطة API Aspose.Cells والذي يُظهر في مثال الكود أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```

### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```

### **فتح ملفات النصوص المفصولة بواسطة الألسنة**

ملفات النص مفصولة بعلامة تبويب (Text) تحتوي على بيانات جدول بيانات ولكن بدون تنسيق. تُرتب البيانات في صفوف وأعمدة كما في الجداول وجداول البيانات. بشكل أساسي، ملف المفصول بعلامة تبويب هو نوع خاص من ملفات النص العادي مع وجود علامة تبويب بين كل عمود.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

ملف القيم المفصولة بعلامة تبويب (TSV) يحتوي على بيانات جدول بيانات ولكن بدون تنسيق. هو نفسه الملف المفصول بعلامة تبويب حيث تُرتب البيانات في صفوف وأعمدة كما في الجداول وجداول البيانات.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **فتح ملفات SXC**

برنامج StarOffice Calc مشابه لـ Microsoft Excel ويدعم الصيغ والرسوم البيانية والوظائف والماكروز. تُحفظ جداول البيانات التي أنشئت باستخدام هذا البرنامج بملف بامتداد SXC. يُستخدم ملف SXC أيضًا لملفات جداول بيانات OpenOffice.org Calc. يمكن لـ Aspose.Cells قراءة ملفات SXC كما يظهر في عينة الكود التالية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات محفوظ بصيغة OpenDocument XML بدون ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما يظهر في عينة الكود التالية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

