---
title: 在 Node.js 和 C++ 中隐藏与显示行列
linktitle: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: 学习如何在工作表中隐藏和显示行列，使用 Aspose.Cells for Node.js via C++。
---

{{% alert color="primary" %}}

有时，隐藏工作表中的某些行或列，稍后再显示它们是有意义的。Microsoft Excel提供了此功能，Aspose.Cells也是。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells for Node.js via C++ 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)，允许开发者访问每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合提供多种管理行列的方法，以下对部分进行了介绍。

### **隐藏行和列**

开发者可以通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-)和[**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-)方法，隐藏某一行或列。两个方法都接受行或列的索引作为参数以隐藏对应的行或列。

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

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **显示行和列**

开发者可以通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-)和[**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-)方法，显示任何隐藏的行或列。两个方法都接受两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

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

在显示隐藏列时，如果需要恢复为之前设置的宽度或原始宽度，请用负宽度取消隐藏该列。例如：worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **隐藏多行和列**

开发者还可以一次隐藏多行或多列，通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-)和[**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-)方法，两个方法都接受起始行或列索引和隐藏的行或列数目作为参数。

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

也可以使用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 类的 [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) 和 [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) 方法，将多行和多列设为可见。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
