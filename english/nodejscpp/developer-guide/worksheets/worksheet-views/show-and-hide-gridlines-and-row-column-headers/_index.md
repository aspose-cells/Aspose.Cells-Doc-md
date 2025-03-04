---  
title: Show and Hide Gridlines and Row Column Headers with Node.js via C++  
linktitle: Show and Hide Gridlines and Row Column Headers  
type: docs  
weight: 30  
url: /nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: This article provides sample code for using the Node.js API via C++ to programmatically hide or show gridlines, row, and column headers of an Excel worksheet.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supports hiding and showing Gridlines of the worksheet which are visible by default. It also provides controlling visibility of Row Column Headers of the worksheet.  
{{% /alert %}}  

## **Show and Hide Gridlines**  

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.  

### **Controlling the Visibility of the Gridlines**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**IsGridlinesVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsGridlinesVisible) property. [**IsGridlinesVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsGridlinesVisible) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Gridlines Visible**  

Make the gridlines visible by setting the [**IsGridlinesVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsGridlinesVisible) property to **true**.  

#### **Hiding Gridlines**  

Hide gridlines by setting the [**IsGridlinesVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsGridlinesVisible) property to **false**.  

A complete example is given below that demonstrates the use of the [**IsGridlinesVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsGridlinesVisible) property by opening an excel file (book1.xls), hiding the gridlines on the first worksheet, and saving the modified file as output.xls.  

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

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsRowColumnHeadersVisible) property. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsRowColumnHeadersVisible) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Row/Column Headers Visible**  

Make row and column headers visible by setting the [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsRowColumnHeadersVisible) property to **true**.  

#### **Hiding Row/Column Headers**  

Hide row and column headers by setting the [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsRowColumnHeadersVisible) property to **false**.  

A complete example is given below that shows how to use the [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#IsRowColumnHeadersVisible) property by opening an excel file (book1.xls), hiding the row and column headers on the first worksheet, and saving the modified file as output.xls.  

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
It is also possible to use the [**UnhideRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/#UnhideRows) and [**UnhideColumns**](https://reference.aspose.com/cells/nodejs-cpp/cells/#UnhideColumns) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class to make multiple rows and columns visible.  
{{% /alert %}}  
  