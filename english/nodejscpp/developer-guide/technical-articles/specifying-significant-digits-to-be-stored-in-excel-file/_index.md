---  
title: Specifying Significant Digits to be Stored in Excel File with Node.js via C++  
linktitle: Specifying Significant Digits to be Stored in Excel File  
type: docs  
weight: 30  
url: /nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Learn how to specify significant digits to be stored in an Excel file using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

By default, Aspose.Cells for Node.js via C++ stores 17 significant digits of double values inside the Excel file, unlike MS-Excel which stores only 15 significant digits. You can change the default behavior of Aspose.Cells from 17 significant digits to 15 significant digits using the [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) property.  

## **Specifying Significant Digits to be stored in Excel file**  

The following sample code enforces Aspose.Cells to use 15 significant digits while storing double values inside the Excel file. Please check the [output excel file](22774105.xlsx). Change its extension to .zip and unzip it and you will see, only 15 significant digits are stored inside the Excel file. The following screenshot explains the effect of [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) property on the output Excel file.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
