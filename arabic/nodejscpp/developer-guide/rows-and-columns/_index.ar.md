---  
title: تنسيق الصفوف والأعمدة باستخدام Node.js عبر C++  
linktitle: الصفوف والأعمدة  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/adjusting-row-height-and-column-width/  
description: يمكن لـ Aspose.Cells for Node.js via C++ دعم تغيير ارتفاع الصف أو عرض العمود، بالإضافة إلى تطبيق التنسيق على الصفوف أو الأعمدة.  
keywords: تعيين ارتفاع الصف وعرض العمود، ضبط ارتفاع الصف وعرض العمود، تغيير ارتفاع الصف أو عرض العمود، تنسيق الصفوف والأعمدة، كيفية تعيين ارتفاع الصف وعرض العمود.  
---  

{{% alert color="primary" %}}  
عند العمل مع جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. أحيانًا، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع أو العرض الحالي بحاجة إلى التغيير لعرض البيانات. عادةً، يقوم المستخدمون بضبط ارتفاعات الصفوف وعروض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن، مع Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.  
{{% /alert %}}  

## **العمل مع الصفوف**  

### **كيفية ضبط ارتفاع الصف**  

تقدم Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.  

توفر مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل. سيتم مناقشة بعضها بمزيد من التفصيل أدناه.  

### **كيفية ضبط ارتفاع الصف**  

من الممكن تعيين ارتفاع صف واحد من خلال استدعاء طريقة [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) لمجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). تأخذ طريقة [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) المعلمات التالية كما يلي:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.  
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **كيفية ضبط ارتفاع كل الصفوف في ورقة عمل**  

إذا احتاج المطورون إلى تعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل، يمكنهم القيام بذلك باستخدام خاصية [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) لمجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

**مثال:**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **العمل مع الأعمدة**  

### **كيفية ضبط عرض العمود**  

حدد عرض العمود من خلال استدعاء مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) وطريقة [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-). تتطلب طريقة [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) المعلمات التالية:  

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.  
- **عرض العمود**, العرض المطلوب للعمود.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **كيفية تعيين عرض العمود بالبكسل**  

حدد عرض العمود من خلال استدعاء مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) وطريقة [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-). تتطلب طريقة [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) المعلمات التالية:  

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.  
- **عرض العمود**, عرض العمود المطلوب بالبكسل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **كيفية ضبط عرض جميع الأعمدة في ورقة العمل**  

لضبط عرض العمود نفسه لجميع الأعمدة في ورقة العمل، استخدم خاصية [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) لمجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **مواضيع متقدمة**  
- [تكييف صفوف وأعمدة تلقائيًا](/cells/ar/nodejs-cpp/autofit-rows-and-columns/)  
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [نسخ الصفوف والأعمدة](/cells/ar/nodejs-cpp/copying-rows-and-columns/)  
- [حذف الصفوف والأعمدة الفارغة في ورقة العمل](/cells/ar/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [تجميع وفك تجميع الصفوف والأعمدة](/cells/ar/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [إدراج أو حذف الصفوف في ورقة عمل Excel](/cells/ar/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [إدراج وحذف الصفوف والأعمدة من ملف Excel](/cells/ar/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [إزالة الصفوف المكررة في ورقة العمل](/cells/ar/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

