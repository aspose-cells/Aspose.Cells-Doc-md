---  
title: تحويل CSV، TSV و TXT إلى Excel مع Node.js عبر C++  
linktitle: تحويل ملفات CSV، TSV و TXT إلى Excel  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
باستخدام Aspose.Cells، يمكنك تحويل ملفات CSV إلى Excel، OpenOffice، PDF، JSON، والعديد من الصيغ الأخرى.  
{{% /alert %}}  

## **فتح ملفات CSV**  

ملفات قيم مفصولة بفواصل (CSV) تحتوي على سجلات حيث تكون القيم مفصولة بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة وتقوم بتقديمه بواسطة الرمز التنصيصي من خلال الرمز مزدوج التنصيص. إذا كانت قيمة الحقل تحتوي على رمز تنصيصي مزدوج فإنه يتم الخروج منها بزوج من الرموز المزدوجة للتنصيص. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**  

عند فتح ملف CSV يحتوي على أحرف خاصة في Excel، يتم استبدال الأحرف تلقائيًا. يتم ذلك أيضًا بواسطة API Aspose.Cells والذي يُظهر في مثال الكود أدناه.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

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
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**  

ملفات القيم المفصولة بالعلامة (TSV) تحتوي على بيانات جدول بيانات ولكن بدون أي تنسيق. هي نفس ملف المفصولة بالعلامة حيث يتم ترتيب البيانات في الصفوف والأعمدة كما في الجداول والجداول الإلكترونية.  

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

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **مواضيع متقدمة**  
- [تحميل أو استيراد ملف CSV بالصيغ](/cells/ar/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [قراءة ملف CSV بعدة ترميزات](/cells/ar/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


