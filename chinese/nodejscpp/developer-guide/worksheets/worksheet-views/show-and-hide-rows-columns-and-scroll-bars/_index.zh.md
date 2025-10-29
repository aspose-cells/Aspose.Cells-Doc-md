---  
title: 通过Node.js和C++显示与隐藏行列和滚动条  
linktitle: 显示和隐藏行、列和滚动条  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: 本文演示如何通过Node.js和C++编程控制Excel工作表的行和列的显示与隐藏。有效控制滚动条的显示，以及批量隐藏或显示多行多列。  
---  

{{% alert color="primary" %}}  
Aspose.Cells提供了一种控制工作表的行、列和滚动条可见性的方法。  
{{% /alert %}}  

## **显示和隐藏行和列**  

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许开发者访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供一个[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合，表示工作表中的所有单元格。[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合提供多种管理工作表中行或列的方法，这里简要介绍几种。  

### **显示行和列**  

开发者可以通过调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-)和[**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-)方法，显示任何隐藏的行或列。两个方法都接受两个参数：  

- 行或列索引 - 用于显示特定行或列的索引。  
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。  

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
在还原隐藏列时，如果需要恢复到之前设置的宽度或原始宽度，请使用负宽度取消隐藏列。例如：worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **隐藏行和列**  

开发者可以通过调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-)和[**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-)方法，隐藏某一行或列。两个方法都接受行或列的索引作为参数以隐藏对应的行或列。  

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
还可以通过将行高或列宽设置为0来隐藏行或列。  
{{% /alert %}}  

### **隐藏多个行和列**  

开发者还可以一次隐藏多行或多列，通过调用[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合的[**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-)和[**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-)方法，两个方法都接受起始行或列索引和隐藏的行或列数目作为参数。  

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

## **显示和隐藏滚动条**  

滚动条用于浏览任何文件的内容。通常有两种类型的滚动条：  

- 垂直滚动条  
- 水平滚动条  

Microsoft Excel还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用Aspose.Cells，开发人员可以控制Excel文件中两种类型滚动条的可见性。  

### **控制滚动条的可见性**  

Aspose.Cells提供了一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类提供了丰富的属性和方法用以管理Excel文件。若要控制滚动条的显示，请使用[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)和[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)属性。[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)和[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)是布尔型属性，只能存储true或false。  

#### **显示滚动条**  

通过将[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)类的[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)或[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)属性设置为**true**，使滚动条可见。  

#### **隐藏滚动条**  

通过将[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)类的[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)或[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)属性设置为**false**，隐藏滚动条。  

**示例代码**  

下面是一个完整的代码，打开一个Excel文件book1.xls，隐藏两个滚动条，然后将修改后的文件保存为output.xls。  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
