---  
title: نسخ الصفوف والأعمدة باستخدام Node.js عبر C++  
linktitle: نسخ الصفوف والأعمدة  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/copying-rows-and-columns/  
description: يظهر هذا المقال كيفية نسخ الصفوف والأعمدة من خلال واجهة برمجة تطبيقات Aspose.Cells for Node.js via C++.  
keywords: Node.js عبر C++، كيفية نسخ الصفوف والأعمدة، نسخ الصفوف باستخدام Node.js، نسخ الأعمدة باستخدام Node.js، كيفية لصق الصفوف والأعمدة باستخدام Aspose.Cells for Node.js via C++، لصق صفوف وأعمدة متعددة، كيفية النسخ واللصق لصف واحد أو عمود.  
---  

## **مقدمة**  

في بعض الأحيان, قد تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ الورقة بأكملها. مع Aspose.Cells, من الممكن نسخ الصفوف والأعمدة داخل المصنف أو بين المصنفات.  
عند نسخ صف (أو عمود), يتم نسخ البيانات الموجودة فيه, بما في ذلك الصيغ - بالمراجع المحدثة - والقيم, التعليقات, التنسيق, الخلايا المخفية, الصور, وغيرها من الكائنات التوضيحية.  

## **كيفية نسخ الصفوف والأعمدة باستخدام Microsoft Excel**  

1. حدد الصف أو العمود الذي ترغب في نسخه.  
1. لنسخ الصفوف أو الأعمدة, انقر **نسخ** على شريط الأدوات **قياسي**, أو اضغط **CTRL**+**C**.  
1. حدد صفًا أو عمودًا أسفل أو إلى اليمين من المكان الذي تريد نسخ تحديدك.  
1. عند نسخ الصفوف أو الأعمدة, انقر **الخلايا المنسوخة** على قائمة **إدراج**.  

{{% alert color="primary" %}}  
إذا قمت بالنقر على **لصق** على شريط الأدوات **قياسي** أو ضغط **CTRL**+**V** بدلاً من النقر على أمر في قائمة **إدراج**, فإن أي محتويات خلايا الوجهة يتم استبدالها.  
{{% /alert %}}  

## **كيفية لصق الصفوف والأعمدة باستخدام خيارات اللصق مع Microsoft Excel**  

1. حدد الخلايا التي تحتوي على البيانات أو السمات الأخرى التي تريد نسخها.  
1. في علامة التبويب الرئيسية, انقر **نسخ**.  
1. انقر على الخلية الأولى في المنطقة التي ترغب في **لصق** ما نسخته.  
1. على علامة التبويب الرئيسية، انقر فوق السهم المجاور لـ **لصق**, ثم حدد **لصق** خاص.  
1. حدد **الخيارات** التي تريدها.  

## **كيفية نسخ الصفوف والأعمدة باستخدام Aspose.Cells for Node.js via C++**  

## **كيفية نسخ صفوف فردية**  

توفر Aspose.Cells أسلوب [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). هذا الأسلوب ينسخ جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الأخرى من الصف المصدر إلى الصف الوجهة.  

تأخذ طريقة [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) المعلمات التالية:  

- كائن [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المصدر،  
- فهرس الصف المصدر، و  
- فهرس الصف الوجهة.  

استخدم هذا الأسلوب لنسخ صف داخل ورقة أو إلى ورقة أخرى. يعمل أسلوب [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) بطريقة مماثلة لبرنامج Microsoft Excel. على سبيل المثال، لا تحتاج إلى تعيين ارتفاع الصف الوجهة بشكل صريح، حيث يتم نسخه أيضًا.  

يظهر المثال التالي كيفية نسخ صف في ورقة العمل. يستخدم ملف إكسل نموذج وينسخ الصف الثاني (بما في ذلك البيانات والتنسيق والتعليقات والصور وما إلى ذلك) ويلصقه في الصف 12 في نفس ورقة العمل.  

يمكنك تخطي الخطوة التي تحصل على ارتفاع صف المصدر باستخدام طريقة [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) ثم تعيين ارتفاع صف الوجهة باستخدام طريقة [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) حيث أن طريقة [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) تتولى الأمر تلقائيًا.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
عند نسخ الصفوف، من المهم ملاحظة الصور المتصلة، الرسوم البيانية أو العناصر الرسومية الأخرى لأن هذا هو نفس الأمر مع برنامج Microsoft Excel:  

1. إذا كان مؤشر الصف الأصلي هو 5، فإن الصورة، الرسم البياني، إلخ، تُنسخ إذا كانت موجودة في الثلاثة صفوف (مؤشر الصف البداية هو 4 ومؤشر الصف النهاية هو 6).  
1. لن يتم إزالة الصور الموجودة، الرسوم البيانية، إلخ في الصف الوجهة.  
{{% /alert %}}  

## **كيفية نسخ عدة صفوف**  

يمكنك أيضًا نسخ عدة صفوف إلى وجهة جديدة أثناء استخدام طريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) التي تأخذ معلمة إضافية من نوع صحيح لتحديد عدد الصفوف المصدر التي سيتم نسخها.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **كيفية نسخ الأعمدة**  

توفر Aspose.Cells طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)، هذه الطريقة تنسخ جميع أنواع البيانات، بما في ذلك الصيغ - مع المراجع المحدّثة - والقيم، والتعليقات، وتنسيقات الخلايا، والخلايا المخفية، والصور وغيرها من عناصر الرسم من عمود المصدر إلى عمود الوجهة.  

تأخذ طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) المعلمات التالية:  

- كائن [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المصدر،  
- فهرس العمود المصدر، و  
- فهرس العمود الوجهة.  

استخدم طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) لنسخ عمود داخل ورقة عمل أو إلى ورقة أخرى.  

هذا المثال ينسخ عمودًا من ورقة العمل ويلصقه في ورقة عمل في دفتر عمل آخر.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **كيفية نسخ عمود متعدد**  

مماثلة لطريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)، توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا طريقة [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) لنسخ عدة أعمدة مصدر إلى موقع جديد.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **كيفية لصق الصفوف والأعمدة مع خيارات اللصق**  

توفر Aspose.Cells الآن [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) أثناء استخدام الوظائف [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) و [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). يسمح بضبط خيار اللصق المناسب بشكل مماثل لبرنامج Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
