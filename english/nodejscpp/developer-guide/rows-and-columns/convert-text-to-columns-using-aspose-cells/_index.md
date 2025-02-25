---  
title: Convert Text to Columns using Aspose.Cells for Node.js via C++  
linktitle: Convert Text to Columns  
type: docs  
weight: 30  
url: /nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Learn how to convert text to columns in Excel using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  

You can convert your Text to Columns using Microsoft Excel. This feature is available from *Data Tools* under the *Data* tab. In order to split the contents of a column to multiple columns, the data should contain a specific delimiter such as a comma (or any other character) based on which Microsoft Excel splits the contents of a cell to multiple cells. Aspose.Cells for Node.js via C++ also provides this feature via [**Worksheet.Cells.textToColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-string-number-).  

## **Convert Text to Columns using Aspose.Cells for Node.js via C++**  

The following sample code explains the usage of [**Worksheet.Cells.textToColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-string-number-) method. The code first adds some people names in column A of the first worksheet. The first and last name is separated by a space character. Then it applies [**Worksheet.Cells.textToColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-string-number-) method on column A and saves it as an output Excel file. If you open the [output Excel file](25395213.xlsx), you will see that first names are in column A while last names are in column B as shown in this screenshot.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  
  