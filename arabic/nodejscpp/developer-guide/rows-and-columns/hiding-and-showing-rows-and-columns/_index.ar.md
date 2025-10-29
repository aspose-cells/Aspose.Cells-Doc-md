---
title: إخفاء وعرض الصفوف والأعمدة باستخدام Node.js عبر C++
linktitle: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 60
url: /ar/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: تعلّم كيف تخفي وتظهر الصفوف والأعمدة في ورقة عمل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، من المنطقي إخفاء بعض الصفوف أو الأعمدة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

توفر Aspose.Cells for Node.js via C++ فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف مايكروسوفت إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) التي تسمح للمطورين بالوصول إلى كل ورقة عمل في الملف. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل، وسنناقش بعضها أدناه.

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء الطريقتين [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) و [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) على التوالي. كلا الطريقتين يتطلب معلمة فهرس الصف والعمود لإخفاء الصف أو العمود المحدد.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **عرض الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء الطريقتين [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) و [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) على التوالي. كلا الطريقتين تتطلب معلمات:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
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

عند جعل عمود مخفي مرئي، إذا كنت بحاجة إلى استعادته إلى عرضه السابق أو إلى عرضه الأصلي، يرجى إلغاء إخفاؤه بعرض سلبي. على سبيل المثال: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **إخفاء عدة صفوف وأعمدة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء الطريقتين [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) و [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) على التوالي. كلا الطريقتين يتطلبان فهرس الصف أو العمود الابتدائي وعدد الصفوف أو الأعمدة التي ينبغي إخفاؤها كمعلمات.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) و[**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) لجعل صفوف وأعمدة متعددة مرئية.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
