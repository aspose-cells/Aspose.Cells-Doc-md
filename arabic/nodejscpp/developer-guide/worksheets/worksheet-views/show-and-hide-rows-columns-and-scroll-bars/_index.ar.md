---  
title: عرض وإخفاء الصفوف والأعمدة وأشرطة التمرير باستخدام Node.js عبر C++  
linktitle: إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: توضح هذه المقالة كيفية عرض وإخفاء صفوف و أعمدة ورقة عمل إكسل برمجياً باستخدام Node.js عبر C++. السيطرة على ظهور أشرطة التمرير وإخفاء عدة صفوف وأعمدة بكفاءة.  
---  

{{% alert color="primary" %}}  
توفر Aspose.Cells وسائل للتحكم في رؤية الصفوف، الأعمدة وأشرطة التمرير بورقة العمل.  
{{% /alert %}}  

## **إظهار وإخفاء الصفوف والأعمدة**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. بعض منها مذكور أدناه.  

### **إظهار الصفوف والأعمدة**  

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء الطريقتين [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) و [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) من مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) على التوالي. كلا الطريقتين تتطلب معلمات:  

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.  
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
عند جعل عمود مخفي مرئياً، إذا كنت بحاجة لاستعادته إلى عرضه السابق أو عرضه الأصلي، يرجى إلغاء إخفاء العمود بعرض سالب. على سبيل المثال: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **إخفاء الصفوف والأعمدة**  

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء الطريقتين [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) و [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) من مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) على التوالي. كلا الطريقتين يتطلب معلمة فهرس الصف والعمود لإخفاء الصف أو العمود المحدد.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.  
{{% /alert %}}  

### **إخفاء صفوف وأعمدة متعددة**  

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء الطريقتين [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) و [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) من مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) على التوالي. كلا الطريقتين يتطلبان فهرس الصف أو العمود الابتدائي وعدد الصفوف أو الأعمدة التي ينبغي إخفاؤها كمعلمات.  

```javascript
const fs = require('fs');
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **إظهار وإخفاء شريط التمرير**  

يُستخدم شريط التمرير للتنقل في محتويات أي ملف. عادة ما تكون هناك نوعين من شرائط التمرير:  

- شرائط التمرير العمودية  
- شرائط التمرير الأفقية  

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.  

### **التحكم في رؤية شرائط التمرير**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف إكسل. توفر فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في ظهور أشرطة التمرير، استخدم الخاصيتين [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) و [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) و [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) هما خصائص من نوع Boolean، مما يعني أن هذه الخصائص يمكنها فقط تخزين قيمة **true** أو **false**.  

#### **جعل أشرطة التمرير مرئية**  

اجعل أشرطة التمرير مرئية عن طريق تعيين خاصية [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) أو [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) للفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) إلى **صحيح**.  

#### **إخفاء أشرطة التمرير**  

إخف أشرطة التمرير عن طريق تعيين خاصية [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) أو [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) للفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) إلى **خطأ**.  

**كود عينة**  

بالأسفل يوجد شيفرة كاملة تفتح ملف إكسل، book1.xls، ثم تخفي كلتي الشريطين وتحفظ الملف المعدل بشكل output.xls.  

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

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

