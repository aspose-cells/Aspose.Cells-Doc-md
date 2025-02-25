---  
title: Show and Hide Rows Columns and Scroll Bars with Node.js via C++  
linktitle: Show and Hide Rows Columns and Scroll Bars  
type: docs  
weight: 20  
url: /nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: This article demonstrates how to programmatically display and hide Excel worksheet rows and columns using Node.js via C++. Control the visibility of scroll bars and hide multiple rows and columns efficiently.  
---  

{{% alert color="primary" %}}  
Aspose.Cells provides ways to control the visibility of Rows, Column and Scroll Bars of a worksheet.  
{{% /alert %}}  

## **Show and Hide Rows and Columns**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/properties/worksheets) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.  

### **Show Rows and Columns**  

Developers can show any hidden row or column by calling the [**unhideRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/unhiderow) and [**unhideColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/unhidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection respectively. Both methods take two parameters:  

- **Row or column index** - the index of a row or column that is used to show the specific row or column.  
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

{{% alert color="primary" %}}  
While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Hide Rows and Columns**  

Developers can hide a row or column by calling the [**hideRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/hiderow) and [**hideColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/hidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

{{% alert color="primary" %}}  
It is also possible to hide a row or column by setting the row height or column width to 0 respectively.  
{{% /alert %}}  

### **Hide Multiple Rows and Columns**  

Developers can hide multiple rows or columns at once by calling the [**hideRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/hiderows) and [**hideColumns**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/hidecolumns) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.  

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

## **Show and Hide Scroll Bars**  

Scroll bars are used to navigate the contents of any file. Normally, there are two kinds of scroll bars:  

- Vertical scroll bars  
- Horizontal scroll bars  

Microsoft Excel also provides horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells, developers can control the visibility of both types of scroll bars in Excel files.  

### **Controlling the Visibility of Scroll Bars**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class provides a wide range of properties and methods for managing an Excel file. To control the visibility of scroll bars, use the [**WorkbookSettings.isVScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/isvscrollbarvisible) and [**WorkbookSettings.isHScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/ishscrollbarvisible) properties. [**WorkbookSettings.isVScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/isvscrollbarvisible) and [**WorkbookSettings.isHScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/ishscrollbarvisible) are Boolean properties, which means that these properties can only store **true** or **false** values.  

#### **Making Scroll Bars Visible**  

Make scroll bars visible by setting the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**WorkbookSettings.isVScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/isvscrollbarvisible) or [**WorkbookSettings.isHScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/ishscrollbarvisible) property to **true**.  

#### **Hiding Scroll Bars**  

Hide scroll bars by setting the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**WorkbookSettings.isVScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/isvscrollbarvisible) or [**WorkbookSettings.isHScrollBarVisible**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/ishscrollbarvisible) property to **false**.  

**Sample Code**  

Below is a complete code that opens an Excel file, book1.xls, hides both scroll bars and then saves the modified file as output.xls.  

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

// Closing the file stream to free all resources
fstream.close();
```  
  