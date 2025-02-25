---  
title: Export Excel Data to DataTable without any Formatting with Node.js via C++  
linktitle: Export Excel Data to DataTable without any Formatting  
type: docs  
weight: 280  
url: /nodejs-cpp/export-excel-data-to-datatable-without-any-formatting/  
description: Learn how to export Excel data to DataTable without any formatting using Aspose.Cells for Node.js via C++.  
keywords: Export Excel Data to DataTable without any Formatting Node.js via C++, Specify Cell Value Format Strategy Node.js via C++, Add Format Strategy When Exporting Data to DataTable Node.js via C++.  
---  

{{% alert color="primary" %}}  
Sometimes users want to export Excel data into a data table without any formatting. For example, if some cell has a value 0.012345 and it is formatted to display two decimal places, then when the user exports Excel data to a data table, it will be exported as 0.01 and not as 0.012345. To deal with this problem, Aspose.Cells has provided [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions/#formatStrategy) property which can take one of these three values  

- CellValueFormatStrategy.CellStyle  
- CellValueFormatStrategy.DisplayStyle  
- CellValueFormatStrategy.None  

If you set it to [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy), then it will export the data without any formatting.  
{{% /alert %}}  

## Sample Code  

The following sample explains the use of [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions/#formatStrategy) property to export Excel data with and without any formatting.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const cell = worksheet.getCells().get("A1");

// Put value inside the cell
cell.putValue(0.012345);

// Format the cell that it should display 0.01 instead of 0.012345
const style = cell.getStyle();
style.setNumber(2);
cell.setStyle(style);

// Display the cell values as it displays in excel
console.log("Cell String Value: " + cell.getStringValue());

// Display the cell value without any format
console.log("Cell String Value without Format: " + cell.getStringValue(AsposeCells.CellValueFormatStrategy.None));

// Export Data Table Options with FormatStrategy as CellStyle
const opts = new AsposeCells.ExportTableOptions();
opts.setExportAsString(true);
opts.setFormatStrategy(AsposeCells.CellValueFormatStrategy.CellStyle);

// Export Data Table
let dt = worksheet.getCells().exportDataTable(0, 0, 1, 1, opts);

// Display the value of very first cell
console.log("Export Data Table with Format Strategy as Cell Style: " + dt.getRows().get(0).get(0).toString());

// Export Data Table Options with FormatStrategy as None
opts.setFormatStrategy(AsposeCells.CellValueFormatStrategy.None);
dt = worksheet.getCells().exportDataTable(0, 0, 1, 1, opts);

// Display the value of very first cell
console.log("Export Data Table with Format Strategy as None: " + dt.getRows().get(0).get(0).toString());
```  

## **Console Output**  

Below is the console debug output of the above sample code  

{{< highlight javascript >}}  
Cell String Value: 0.01  

Cell String Value without Format: 0.012345  

Export Data Table with Format Strategy as Cell Style: 0.01  

Export Data Table with Format Strategy as None: 0.012345  
{{< /highlight >}}  
  