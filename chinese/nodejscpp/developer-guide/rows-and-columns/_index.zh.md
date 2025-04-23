---  
title: 按行和列格式化，使用Node.js via C++  
linktitle: 行和列  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++支持更改行高或列宽，还可以对行或列应用格式。  
keywords: 设置行高和列宽，调整行高和列宽，更改行高或列宽，格式化行和列，如何设置行高和列宽。  
---  

{{% alert color="primary" %}}  
在处理电子表格和向行或列添加数据时，可能需要调整行高或列宽。有时，应用格式意味着需要更改当前的高度或宽度以显示数据。通常，用户在Microsoft Excel中通过直观界面调整行高和列宽。但借助Aspose.Cells，开发者可以在运行时执行这些操作。  
{{% /alert %}}  

## **处理行**  

### **如何调整行高**  

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合，代表工作表中的所有单元格。  

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合提供若干方法，用于管理工作表中的行或列。以下是一些详细介绍。  

### **如何设置行的高度**  

可以通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)方法，设置单个行的高度。该[**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)方法的参数如下：

- **行索引**，要更改高度的行的索引。  
- **行高**，要应用于该行的行高。

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

### **如何设置工作表中所有行的高度**  

如果开发者需要为工作表中的所有行设置相同的行高，可以通过修改[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--)属性实现。  

**示例：**  

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

## **使用列**  

### **如何设置列的宽度**  

通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)方法来设置列宽。[**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)方法接受以下参数：  

- **列索引**，要更改其宽度的列的索引。  
- **列宽度**，所需的列宽度。  

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

### **如何以像素设置列宽**  

通过调用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)方法来设置列宽。[**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)方法接受以下参数：  

- **列索引**，要更改其宽度的列的索引。  
- **列宽**，以像素为单位的期望列宽。  

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

### **如何设置工作表中所有列的宽度**  

要为工作表中的所有列设置相同的列宽，请使用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的[**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--)属性。  

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

## **高级主题**  
- [自动调整行和列](/cells/zh/nodejs-cpp/autofit-rows-and-columns/)  
- [使用Aspose.Cells将文本转换为列](/cells/zh/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [复制行和列](/cells/zh/nodejs-cpp/copying-rows-and-columns/)  
- [在工作表中删除空白行和列](/cells/zh/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [分组和取消分组行和列](/cells/zh/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [隐藏和显示行和列](/cells/zh/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [在Excel工作表中插入或删除行](/cells/zh/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [插入和删除Excel文件的行和列](/cells/zh/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [在工作表中删除重复行](/cells/zh/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

