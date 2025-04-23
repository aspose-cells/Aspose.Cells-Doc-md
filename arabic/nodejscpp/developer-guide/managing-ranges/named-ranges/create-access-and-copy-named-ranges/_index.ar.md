---  
title: إنشاء والوصول ونسخ النطاقات المسماة باستخدام Node.js عبر C++  
linktitle: إنشاء الوصول ونسخ نطاقات الأسماء  
type: docs  
weight: 200  
url: /ar/nodejs-cpp/create-access-and-copy-named-ranges/  
description: تعلم كيفية إنشاء والوصول ونسخ النطاقات المسماة في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

## **مقدمة**  

عادةً، يتم استخدام تسميات الأعمدة والصفوف للإشارة إلى خلايا فردية. من الممكن إنشاء أسماء وصفية لتمثيل الخلايا، والنطاقات، والصيغ، أو القيم الثابتة. قد يشير الكلمة **اسم** إلى سلسلة من الأحرف تمثل خلية أو نطاق خلايا، أو صيغة، أو قيمة ثابتة. تعيين اسم لنطاق يعني أن هذا النطاق من الخلايا يمكن الإشارة إليه باسمه. استخدم أسماء سهلة الفهم، مثل منتجات، للإشارة إلى النطاقات التي يصعب فهمها، مثل المبيعات!C20:C30. يمكن استخدام العلامات في الصيغ التي تشير إلى البيانات على نفس ورقة العمل؛ إذا كنت تريد تمثيل نطاق على ورقة عمل أخرى، يمكنك استخدام اسم. *النطاقات المُعرفة باسم من بين أقوى ميزات Microsoft Excel، خاصة عند استخدامها كمصدر لنطاق لقوائم الاختيارات، والجداول المحورية، ومخططات البيانات، وغيرها.*  

## **العمل مع النطاق المسمى باستخدام Microsoft Excel**  

### **إنشاء نطاقات مسماة**  

الخطوات التالية تصف كيفية تسمية خلية أو نطاق خلايا باستخدام **MS Excel**. ينطبق هذا الأسلوب على **Microsoft Office Excel 2003**، **Microsoft Excel 97**، 2000، و 2002.  

1. حدد الخلية أو النطاق الذي ترغب في تسميته.  
2. انقر على **مربع الاسم** عند الطرف الأيسر من شريط الصيغة.  
3. اكتب اسم الخلايا.  
4. اضغط على ENTER.  

{{% alert color="primary" %}}  
لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.  
{{% /alert %}}  

## **العمل مع نطاق مسمى باستخدام Aspose.Cells**  

هنا، نستخدم واجهة برمجة التطبيقات Aspose.Cells للقيام بالمهمة.  
توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

### **إنشاء نطاق مسمى**  

من الممكن إنشاء نطاق مسمى عن طريق استدعاء [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) الزائدة من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). إصدار نموذجي لـ [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) يأخذ المعلمات التالية:  

- اسم الخلية العلوية اليسرى، اسم الخلية العلوية اليسرى في النطاق.  
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.  

عند استدعاء [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-)، فإنه يُرجع نطاق المصنوع حديثًا كنموذج من فئة [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). استخدم هذا [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) لتكوين النطاق المسمى. على سبيل المثال، قم بتعيين اسم النطاق باستخدام خاصية [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). يوضح المثال التالي كيفية إنشاء نطاق مسمّى للخلايا التي تمتد عبر B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **إدخال البيانات في الخلايا في النطاق المسمى**  

يمكنك إدخال البيانات في الخلايا الفردية لنطاق وفق النمط  

- **جافا سكريبت**: نطاق [صف،عمود]  

على سبيل المثال، لديك مجموعة مسماة من الخلايا التي تمتد بين A1:C4. تجعل المصفوفة 4 * 3 = 12 خلية. تتم ترتيب الخلايا الفردية في النطاق بشكل تسلسلي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

استخدم الخصائص التالية لتحديد الخلايا في المدى:  

- firstRow يعيد مؤشر أول صف في النطاق المسمي.  
- firstColumn يعيد مؤشر أول عمود في النطاق المسمي.  
- rowCount يعيد إجمالي عدد الصفوف في النطاق المسمي.  
- columnCount يعيد إجمالي عدد الأعمدة في النطاق المسمي.  

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **تحديد الخلايا في النطاق المسمى**  

يمكنك إدراج البيانات في الخلايا الفردية في المجموعة وفق النمط التالي:  

- **جافا سكريبت**: نطاق [صف،عمود]  

إذا كان لديك مدى يحمل اسم يمتد من A1:C4. المصفوفة تجعل 4 * 3 = 12 خلية. ترتب الخلايا في المدى الفردي بشكل متسلسل: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

استخدم الخصائص التالية لتحديد الخلايا في المدى:  

- firstRow يعيد مؤشر أول صف في النطاق المسمي.  
- firstColumn يعيد مؤشر أول عمود في النطاق المسمي.  
- rowCount يعيد إجمالي عدد الصفوف في النطاق المسمي.  
- columnCount يعيد إجمالي عدد الأعمدة في النطاق المسمي.  

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **الوصول إلى المدى المسمى**  

#### **الوصول إلى نطاق مسمى محدد**  

استدعاء [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) الكائن [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) الميثود للحصول على مدى بالاسم المحدد. تأخذ الميثود النموذجية [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) الاسم للمدى المسمى وتعيد المدى المحدد كمثيل لفئة [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). يوضح المثال التالي كيفية الوصول إلى مدى محدد بالاسم.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **الوصول إلى كافة المدى المسمى في ورقة العمل**  

استدعِ طريقة [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) من مجموعة [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) للحصول على جميع النطاقات المعرفة في ورقة العمل. تقوم الطريقة [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) بإرجاع مصفوفة تحتوي على جميع النطاقات المعرفة في مجموعة [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).  

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **نسخ المدى المسمى**  

توفر Aspose.Cells [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) الميثود لنسخ مدى من الخلايا مع التنسيق في مدى آخر.  

المثال التالي يوضح كيفية نسخ مدى مصدر من الخلايا إلى مدى مسمى آخر.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

