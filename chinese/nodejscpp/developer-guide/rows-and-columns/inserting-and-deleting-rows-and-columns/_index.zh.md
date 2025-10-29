---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: 本文演示如何使用 Aspose.Cells for Node.js via C++ API 在 Excel 中插入和删除行列。
keywords: Aspose.Cells Node.js 通过 C++ 管理行和列，插入行列，删除行列
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上操作，我们可能需要添加额外的行或列来容纳更多数据。反之，我们可能还需要从工作表中的指定位置删除行或列。 
为了满足这些需求，Aspose.Cells for Node.js via C++ 提供了一组非常简单的类和方法，详述如下。

### **管理行和列**

Aspose.Cells for Node.js via C++ 提供了一个 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类，代表一个 Microsoft Excel 文件。. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 集合，可以访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合，表示工作表中的所有单元格。

 [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合提供多种用于管理工作表中的行和列的方法。以下介绍一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动；删除行或列时，内容会向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **如何插入行**

通过调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-)方法，在工作表中的任何位置插入一行。[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-)方法接受新行将被插入的行索引。

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

### **如何插入多行**

要向工作表中插入多行，调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)方法。[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)方法接受两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

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

### **如何插入带有格式的行**

要插入带有格式选项的行，使用接受[**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions)参数的[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)重载。将[**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions)类的[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)属性与[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)枚举设置。[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)枚举有以下三个成员。

- SameAsAbove: 格式与上方行相同。
- SameAsBelow: 格式与下方行相同。
- Clear: 清除格式。

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

### **如何插入列**

开发人员还可以通过调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-)方法在工作表的任何位置插入列。[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-)方法接受将插入新列的列的索引。

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

## **删除行和列**

### **如何删除多行**

要从工作表删除多行，请调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)方法。[**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)方法接受两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

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


### **如何删除列**

要从工作表的任何位置删除列，请调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-)方法。[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-)方法接受要删除的列的索引。

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
