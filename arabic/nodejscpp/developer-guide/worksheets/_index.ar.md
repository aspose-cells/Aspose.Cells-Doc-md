---  
title: إدارة أوراق العمل لملفات Microsoft Excel باستخدام Node.js عبر C++  
linktitle: أوراق العمل  
type: docs  
weight: 90  
url: /ar/nodejs-cpp/manage-worksheets/  
description: إضافة، إزالة، وتفعيل أوراق العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يمكن للمطورين إنشاء وإدارة أوراق العمل بشكل سهل في ملفات مايكروسوفت إكسل برمجيًا باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells. يصف هذا الموضوع الطرق لإضافة وإزالة أوراق العمل في ملفات مايكروسوفت إكسل.  
{{% /alert %}}  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) والتي تمثل ملف إكسل. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) والتي تتيح الوصول إلى كل ورقة عمل داخل ملف إكسل.  

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل.  

## **إضافة ورقات العمل إلى ملف Excel جديد**  

لإنشاء ملف Excel جديد برمجياً:  

1. إنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. استدعاء طريقة [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). يتم إضافة ورقة عمل فارغة تلقائياً إلى ملف إكسل. يمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--).  
1. الحصول على مرجع ورقة العمل.  
1. القيام بالعمل على أوراق العمل.  
1. حفظ ملف إكسل الجديد مع أوراق العمل الجديدة عن طريق استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **إضافة ورقات عمل إلى جدول التصميم**  

عملية إضافة أوراق العمل إلى جدول تصميمي هي نفسها عملية إضافة ورقة عمل جديدة، باستثناء أن ملف إكسل موجود مسبقًا ويجب فتحه قبل إضافة أوراق العمل. يمكن فتح ملف جدول التصميم بواسطة فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**  

الوصول إلى أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **إزالة الأوراق العمل باستخدام اسم الورقة**  

لإزالة أوراق العمل من ملف، استدعِ طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). مرر اسم الورقة إلى طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) لإزالة ورقة عمل محددة.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **إزالة الأوراق العمل باستخدام فهرس الورقة**  

إزالة أوراق العمل بواسطة الاسم تعمل بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا لم تعرف اسم ورقة العمل، استخدم نسخة محمّلة من طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) التي تأخذ فهرس الورقة بدلاً من اسمها.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **تنشيط الأوراق وجعل خلية نشطة في ورقة العمل**  

أحيانًا، تحتاج إلى أن تكون ورقة عمل معينة نشطة ومعروضة عند فتح مستخدم لملف إكسل من مايكروسوفت إكسل. بالمثل، قد ترغب في تفعيل خلية معينة وضبط أشرطة التمرير لعرض الخلية النشطة. قادر على Aspose.Cells على القيام بجميع هذه المهام.  

ورقة العمل النشطة هي الورقة التي تعمل عليها: اسم الورقة النشطة على علامة التبويب يكون سميك افتراضيًا.  

الخلية النشطة هي الخلية المحددة، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. تكون خلية واحدة فقط نشطة في وقت واحد. يتم تمييز الخلية النشطة بحد ثقيل.  

### **تفعيل الأوراق وجعل خلية نشطة**  

توفر Aspose.Cells استدعاءات API محددة لتفعيل ورقة وخلية. على سبيل المثال، خاصية [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) مفيدة لضبط الورقة النشطة في دفتر العمل. بالمثل، تُستخدم خاصية [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) لضبط والحصول على خلية نشطة في ورقة العمل.  

للتأكد من أن أشرطة التمرير الأفقية أو الرأسية في موضع الفهرس الصف والعمود الذي تريد إظهار البيانات المحددة، استخدم خاصيتي [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) و [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

تُظهر الشفرة المثالية التالية كيفية تفعيل ورقة عمل وجعل خلية نشطة فيها. في الناتج المولد، ستتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين لديها.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **مواضيع متقدمة**  
- [نسخ ونقل أوراق العمل](/cells/ar/nodejs-cpp/copying-and-moving-worksheets/)  
- [عدد الخلايا في ورقة العمل](/cells/ar/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [الكشف عن ورق العمل الفارغة](/cells/ar/nodejs-cpp/detecting-empty-worksheets/)  
- [العثور على ورقة العمل هل هي ورقة حوار](/cells/ar/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [الحصول على معرف فريد لورقة العمل](/cells/ar/nodejs-cpp/get-worksheet-unique-id/)  
- [إنشاء أو تلاعب أو إزالة السيناريوهات من ورقات العمل](/cells/ar/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [إدارة فواصل الصفحات](/cells/ar/nodejs-cpp/managing-page-breaks/)  
- [ميزات إعداد الصفحة](/cells/ar/nodejs-cpp/page-setup-features/)   
- [الاستفادة من خاصية Sheet.SheetId في الشكل المفتوحXML باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [عروض ورقة العمل](/cells/ar/nodejs-cpp/worksheet-views/)  


