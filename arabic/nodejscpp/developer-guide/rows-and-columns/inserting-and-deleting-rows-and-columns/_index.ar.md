---
title: إدراج وحذف الصفوف والأعمدة من ملف إكسل
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: يظهر هذا المقال كيفية إدراج وحذف الصفوف والأعمدة بواسطة واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: إدارة الصفوف والأعمدة باستخدام Aspose.Cells Node.js عبر C++، إدراج الصفوف والأعمدة، حذف الصفوف والأعمدة
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل. 
لتلبية هذه المتطلبات، يوفر Aspose.Cells for Node.js via C++ مجموعة بسيطة للغاية من الفئات والطرق، التي نوقشت أدناه.

### **إدارة الصفوف والأعمدة**

 يوفر Aspose.Cells for Node.js via C++ فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، والتي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) التي تمثل جميع الخلايا في ورقة العمل.

 توفر مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) طرقًا عدة لإدارة الصفوف والأعمدة في ورقة العمل. تم مناقشة بعض منها أدناه.

{{% alert color="primary" %}}

عند إضافة الصفوف أو الأعمدة، يتم إزاحة المحتوى في ورقة العمل إلى الأسفل أو إلى اليمين، وعند إزالة الصفوف أو الأعمدة، يتم إزاحة المحتوى للأعلى أو إلى اليسار.

{{% /alert %}}


## **إدراج الصفوف والأعمدة**

### **كيفية إدراج صف**

قم بإدراج صف في ورقة العمل في أي موقع عن طريق استدعاء ال[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) من مجموعة ال[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). يأخذ ال[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) المؤشر للصف الذي سيتم إدراج الصف الجديد فيه.

```javascript
const path = require("path");
const fs = require("fs");
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

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **كيفية إدراج عدة صفوف**

لإدراج عدة صفوف في ورقة العمل، اتصل بالطريقة [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) في تجميعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). طريقة [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **كيفية إدراج صف مع تنسيق**

لإدراج صف بخيارات تنسيق، استخدم الحمولة [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) التي تأخذ [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) كمعلمة. ثبّت خصية [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) لفئة [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) بقيمة الترقيم [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/). الفئة [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) لها ثلاثة أعضاء كما هو مدرج أدناه.

- SameAsAbove: ينسق الصف نفسه كصف الذي في الأعلى.
- SameAsBelow: ينسق الصف نفسه كصف الذي في الأسفل.
- Clear: يُمسح التنسيق.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **كيفية إدراج عمود**

يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي موقع عن طريق استدعاء الطريقة [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) في تجميعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). الطريقة [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) تأخذ مؤشر العمود حيث سيتم إدراج العمود الجديد.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **حذف الصفوف والأعمدة**

### **كيفية حذف عدة صفوف**

لحذف صفوف متعددة من ورقة العمل، اتصل بالطريقة [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) في تجميعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). الطريقة [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **كيفية حذف عمود**

لحذف عمود من ورقة العمل في أي موقع، اتصل بالطريقة [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) في تجميعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). الطريقة [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) تأخذ مؤشر العمود للحذف.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
{{< app/cells/assistant language="nodejs-cpp" >}}
