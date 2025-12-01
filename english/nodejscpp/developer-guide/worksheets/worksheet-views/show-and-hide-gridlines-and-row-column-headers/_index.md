---  
title: Show and Hide Gridlines and Row Column Headers with Node.js via C++  
linktitle: Show and Hide Gridlines and Row Column Headers  
type: docs  
weight: 30  
url: /nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: This article provides sample code for using the Node.js API via C++ to programmatically hide or show gridlines, row, and column headers of an Excel worksheet.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Aspose.Cells supports hiding and showing Gridlines of the worksheet which are visible by default. It also provides controlling visibility of Row Column Headers of the worksheet.  
{{% /alert %}}  

## **Show and Hide Gridlines**  

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.  

### **Controlling the Visibility of the Gridlines**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) property. [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Gridlines Visible**  

Make the gridlines visible by setting the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) property to **true**.  

#### **Hiding Gridlines**  

Hide gridlines by setting the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) property to **false**.  

A complete example is given below that demonstrates the use of the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) property by opening an excel file (book1.xls), hiding the gridlines on the first worksheet, and saving the modified file as output.xls.  

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

## **Show and Hide Row Column Headers**  

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.  

### **Controlling the Visibility of the Worksheets**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) property. [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Row/Column Headers Visible**  

Make row and column headers visible by setting the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) property to **true**.  

#### **Hiding Row/Column Headers**  

Hide row and column headers by setting the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) property to **false**.  

A complete example is given below that shows how to use the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) property by opening an excel file (book1.xls), hiding the row and column headers on the first worksheet, and saving the modified file as output.xls.  

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
It is also possible to use the [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) and [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class to make multiple rows and columns visible.  
{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
