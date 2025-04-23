---  
title: تحجيم تلقائي للصفوف والأعمدة باستخدام Node.js عبر C++  
linktitle: ضبط تلقائي للصفوف والأعمدة  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/autofit-rows-and-columns/  
description: يوضح هذا المقال كيفية التحجيم التلقائي للصفوف والأعمدة والصفوف للخلايا المدمجة وصف من الخلايا باستخدام Aspose.Cells for Node.js via C++.  
keywords: التحجيم التلقائي للصفوف باستخدام Node.js عبر C++، التحجيم التلقائي للأعمدة باستخدام Node.js عبر C++، التحجيم التلقائي لصف في نطاق خلايا باستخدام Node.js عبر C++، التحجيم التلقائي لصفوف الخلايا المدمجة باستخدام Node.js عبر C++  
---  

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بتحديد عرض وارتفاع الخلايا تلقائيًا وفقًا لمحتواها. تتوفر هذه الميزة أيضًا من خلال Aspose.Cells for Node.js via C++، بحيث يمكن للمطورين ضبط أبعاد الخلايا تلقائيًا أثناء التشغيل.  
{{% /alert %}}  

## **ضبط تلقائي**  

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. يستعرض هذا المقال استخدام الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) للتحجيم التلقائي للصفوف أو الأعمدة.  

### **ضبط تلقائي للصف - بسيط**  

أبسط طريقة لضبط عرض وارتفاع الصف تلقائيًا هي استدعاء طريقة [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) لفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). تأخذ طريقة [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) مؤشر صف (للصف الذي سيتم تغيير حجمه) كمعامل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **كيفية ضبط صف تلقائيًا في مجموعة من الخلايا**  

 يتكون الصف من العديد من الأعمدة. يسمح Aspose.Cells للمطورين بضبط صف تلقائيًا استنادًا إلى المحتوى في نطاق خلايا داخل الصف عن طريق استدعاء إصدار محمل زائد من طريقة [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-). وهي تأخذ المعاملات التالية:  

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.  
- **فهرس العمود الأول**, فهرس العمود الأول للصف.  
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.  

 تتحقق طريقة [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) من محتويات جميع الأعمدة في الصف ثم تضبط الصف تلقائيًا.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **كيفية ضبط العمود تلقائيًا في مجموعة من الخلايا**  

 العمود يتكون من العديد من الصفوف. من الممكن التحقق من التحجيم التلقائي لعمود استنادًا إلى المحتوى في نطاق من الخلايا في العمود من خلال استدعاء نسخة مفرطة التحميل من أسلوب [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) الذي يأخذ المعلمات التالية:  

- **فهرس العمود**: فهرس العمود الذي سيتم تلائم حجمه تلقائياً.  
- **فهرس الصف الأول**: فهرس أول صف في العمود.  
- **فهرس الصف الأخير**: فهرس آخر صف في العمود.  

 تتحقق طريقة [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) من محتويات جميع الصفوف في العمود ثم تضبط العمود تلقائيًا.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **كيفية تلائم حجم الصفوف للخلايا المدمجة**  

 مع Aspose.Cells، من الممكن التحجيم التلقائي للصفوف حتى للخلايا المدمجة باستخدام واجهة برمجة التطبيقات [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). توفر فئة [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) الخاصية [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) التي يمكن استخدامها لتحجيم الصفوف للخلايا المدمجة. يقبل [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) مجموعة [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) القابلة للعد التي تحتوي على الأعضاء التالية.  

- لا شيء: تجاهل الخلايا المدمجة.  
- السطر الأول: فقط يوسع ارتفاع الصف الأول.  
- السطر الأخير: فقط يوسع ارتفاع الصف الأخير.  
- كل سطر: يوسع ارتفاع كل صف.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
يمكنك أيضًا محاولة استخدام النسخ المفرطة التحميل لأساليب [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) و [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) لقبول نطاق من الصفوف/الأعمدة ونسخة من [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) لتحجيم الصفوف/الأعمدة المختارة حسب [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) المرغوب.  

التواقيع للطرق المذكورة سابقًا هي كما يلي:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **مهم معرفته**  

{{% alert color="primary" %}}  
إذا تم دمج خلية، فلن يتم تطبيق أساليب التحجيم التلقائي، وهو نفس السلوك في Microsoft Excel. يمكنك تجاوز ذلك باستخدام واجهة برمجة تطبيقات autofilter. علاوة على ذلك، إذا كان النص في خلية ملتفًا، فلن يتم تطبيق أسلوب [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) أيضًا. شيء آخر تحتاج إلى معرفته هو أن أساليب *autoFit* تتطلب وقتًا. لذا، يجب استدعاؤها بأقل قدر ممكن لضمان كفاءة تطبيقك.  
{{% /alert %}}  

## **مواضيع متقدمة**  
- [تلائم حجم الصفوف للخلايا المدمجة](/cells/ar/nodejs-cpp/autofit-rows-for-merged-cells/)  

