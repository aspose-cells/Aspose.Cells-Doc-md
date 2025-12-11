---  
title: Format Rows and Columns with Node.js via C++  
linktitle: Rows and Columns  
type: docs  
weight: 100  
url: /nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ can support changing row height or column width, as well as applying formatting on rows or columns.  
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  
When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or the width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells, developers can perform these operations at runtime.  
{{% /alert %}}  

## **Working with Rows**  

### **How to Adjust Row Height**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection that represents all cells in the worksheet.  

The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.  

### **How to Set the Height of a Row**  

It is possible to set the height of a single row by calling the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) method. The [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) method takes the following parameters:  

- **Row index** – the index of the row that you're changing the height of.  
- **Row height** – the row height to apply to the row.  

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
    });
} catch (e) {
    console.error(e);
}
```  

### **How to Set the Height of All Rows in a Worksheet**  

If developers need to set the same row height for all rows in the worksheet, they can do it by using the [**setStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setStandardHeight-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection.  

**Example:**  

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

// Note: Closing the file stream is unnecessary in this context as it's a
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure. If using fs.createReadStream, you would handle it accordingly.
```  

## **Working with Columns**  

### **How to Set the Width of a Column**  

Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) method. The [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) method takes the following parameters:  

- **Column index** – the index of the column that you're changing the width of.  
- **Column width** – the desired column width.  

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

// No explicit close needed for fs.readFileSync
```  

### **How to Set Column Width in Pixels**  

Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) method. The [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) method takes the following parameters:  

- **Column index** – the index of the column that you're changing the width of.  
- **Column width** – the desired column width in pixels.  

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

### **How to Set the Width of All Columns in a Worksheet**  

To set the same column width for all columns in the worksheet, use the [**setStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setStandardWidth-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection.  

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

// No explicit close needed in Node.js
```  

## **Advanced topics**  
- [AutoFit Rows and Columns](/cells/nodejs-cpp/autofit-rows-and-columns/)  
- [Convert Text to Columns using Aspose.Cells](/cells/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Copying Rows and Columns](/cells/nodejs-cpp/copying-rows-and-columns/)  
- [Delete Blank Rows and Columns in a Worksheet](/cells/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Grouping and Ungrouping Rows and Columns](/cells/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Hiding and Showing Rows and Columns](/cells/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Insert or Delete Rows in an Excel Worksheet](/cells/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Inserting and Deleting Rows and Columns of Excel file](/cells/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Remove duplicate rows in a Worksheet](/cells/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Update references in other worksheets while deleting blank columns and rows in a worksheet](/cells/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
