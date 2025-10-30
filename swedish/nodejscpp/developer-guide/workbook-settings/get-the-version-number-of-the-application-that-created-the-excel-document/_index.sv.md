---  
title: Hämta versionsnumret för applikationen som skapade Excel dokumentet med Node.js via C++  
linktitle: Hämta versionssiffran för programmet som skapade Excel dokumentet  
type: docs  
weight: 210  
url: /sv/nodejs-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/  
---  

{{% alert color="primary" %}}  

Ofta måste du veta versionsnummer för applikationen som skapade ett Microsoft Excel-dokument. Aspose.Cells for Node.js via C++ tillhandahåller egenskapen [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) för detta ändamål.

{{% /alert %}}  

Följande kodexempel visar användningen av egenskapen [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--). Den laddar Excel-filer som skapats med Microsoft Excel 2003, 2007, 2010 och 2013 och skriver ut versionsnumret för applikationen som skapade dessa Excel-dokument.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Print the version number of Excel 2003 XLS file
let workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2003.xls"));
console.log("Excel 2003 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xls"));
console.log("Excel 2007 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xls"));
console.log("Excel 2010 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xls"));
console.log("Excel 2013 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xlsx"));
console.log("Excel 2007 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xlsx"));
console.log("Excel 2010 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xlsx"));
console.log("Excel 2013 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
