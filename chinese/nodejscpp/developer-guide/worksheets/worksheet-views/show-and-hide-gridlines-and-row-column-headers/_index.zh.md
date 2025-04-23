---  
title: 通过Node.js和C++显示与隐藏网格线及行列标题  
linktitle: 显示和隐藏网格线以及行列标题  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: 本文提供了使用Node.js API通过C++编程隐藏或显示Excel工作表的网格线、行和列标题的示例代码。  
---  

{{% alert color="primary" %}}  
Aspose.Cells支持隐藏和显示工作表中默认情况下可见的网格线。它还提供了控制工作表的行列标题的可见性。  
{{% /alert %}}  

## **显示和隐藏网格线**  

所有Excel工作表默认情况下都有网格线。它们有助于划分单元格，便于将数据输入特定的单元格。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都易于识别。  

### **控制网格线的可见性**  

Aspose.Cells提供了一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许开发者访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供了丰富的属性和方法管理工作表。若要控制网格线的显示，请使用[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)属性。[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)是一个布尔型属性，只能存储true或false值。  

#### **使网格线可见**  

通过将[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)属性设置为**true**，使网格线可见。  

#### **隐藏网格线**  

通过将[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)属性设置为**false**，隐藏网格线。  

下面给出一个完整示例，展示如何通过打开Excel文件（book1.xls）、隐藏第一个工作表上的网格线，并将修改后的文件另存为output.xls，来使用[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)属性。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **显示和隐藏行列标题**  

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都有用于标识它们和单个单元格的唯一值。例如，行编号为1、2、3、4等，列按字母顺序排列为A、B、C、D等。行和列值显示在标题中。使用Aspose.Cells，开发人员可以控制这些行和列标题的可见性。  

### **控制工作表的可见性**  

Aspose.Cells提供了一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许开发者访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供了丰富的属性和方法管理工作表。若要控制行列标题的可见性，请使用[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)属性。[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)是一个布尔型属性，只能存储true或false值。  

#### **使行/列标头可见**  

通过将[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)属性设置为**true**，使行和列标题可见。  

#### **隐藏行/列标头**  

通过将[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)属性设置为**false**，隐藏行列标题。  

下例展示了如何通过打开Excel文件（book1.xls）、隐藏第一个工作表的行列标题，并将修改后的文件另存为output.xls，来使用[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)属性。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
也可以使用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)类的[**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-)和[**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-)方法，使多行或多列变得可见。  
{{% /alert %}}  

