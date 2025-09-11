---  
title: Find Maximum Rows and Columns supported by XLS and XLSX formats with Node.js via C++  
linktitle: Find Maximum Rows and Columns supported by XLS and XLSX formats  
type: docs  
weight: 20  
url: /nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  
  
## **Possible Usage Scenarios**  
  
There are different numbers of rows and columns supported by Excel formats. For example, XLS supports 65536 rows and 256 columns while XLSX supports 1048576 rows and 16384 columns. If you want to know how many rows and columns are supported by a given format, you can use [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) and [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) properties.  
  
## **Find Maximum Rows and Columns supported by XLS and XLSX formats**  
  
The following sample code creates a workbook first in XLS and then in XLSX format. After creation, it prints the values of [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) and [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) properties. Please see the console output of the code given below for your reference.  
  
## **Sample Code**  
  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Print message about XLS format.
console.log("Maximum Rows and Columns supported by XLS format.");

// Create workbook in XLS format.
let wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Excel97To2003);

// Print the maximum rows and columns supported by XLS format.
let maxRows = wb.getSettings().getMaxRow() + 1;
let maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
console.log();

// Print message about XLSX format.
console.log("Maximum Rows and Columns supported by XLSX format.");

// Create workbook in XLSX format.
wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Print the maximum rows and columns supported by XLSX format.
maxRows = wb.getSettings().getMaxRow() + 1;
maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
```  
  
## **Console Output**  
  
{{< highlight java >}}  
  
Maximum Rows and Columns supported by XLS format.  
  
Maximum Rows: 65536  
  
Maximum Columns: 256  
  
Maximum Rows and Columns supported by XLSX format.  
  
Maximum Rows: 1048576  
  
Maximum Columns: 16384  
  
{{< /highlight >}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}