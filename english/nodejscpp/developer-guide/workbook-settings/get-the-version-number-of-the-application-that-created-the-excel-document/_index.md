---  
title: Get the Version Number of the Application that Created the Excel Document with Node.js via C++  
linktitle: Get the Version Number of the Application that Created the Excel Document  
type: docs  
weight: 210  
url: /nodejs-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Often you need to know the version number of the application that created a Microsoft Excel document. Aspose.Cells for Node.js via C++ provides the [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) property for this purpose.

{{% /alert %}}  

The following sample code demonstrates the use of the [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) property. It loads Excel files created with Microsoft Excel 2003, 2007, 2010 and 2013 and prints the version number of the application that created these Excel documents.

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
