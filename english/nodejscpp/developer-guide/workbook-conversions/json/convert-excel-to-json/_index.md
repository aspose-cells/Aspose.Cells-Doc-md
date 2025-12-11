---  
title: Convert-Excel-to-JSON with Node.js via C++  
linktitle: Convert-Excel-to-JSON  
type: docs  
weight: 300  
url: /nodejs-cpp/convert-excel-to-json/  
description: Learn how to convert an Excel file to JSON using Aspose.Cells for Node.js via C++.  
keywords: Exporting Workbook to JSON Node.js via C++, Convert Excel to JSON Node.js via C++  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Aspose.Cells supports converting a Workbook to JSON (JavaScript Object Notation) file.  
{{% /alert %}}  

## **Convert Excel Workbook to JSON**  

No need to wonder how to convert an Excel workbook to JSON, because the Aspose.Cells for Node.js via C++ library provides the best solution. The Aspose.Cells API offers support for converting spreadsheets to JSON format. To export the workbook to JSON, pass [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) as the second parameter of [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method. You may also use [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) class to specify additional settings for exporting the worksheet to JSON.  

The following code example demonstrates exporting an Excel Workbook to JSON. Please see the code that converts the [source file](sample.xlsx) to the generated JSON file for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to a JSON file.
workbook.save("sample_out.json");
```  

The following code example uses the JsonSaveOptions class to specify additional settings and demonstrates exporting an Excel Workbook to JSON. Please see the code that converts the [source file](sample.xlsx) to the generated JSON file for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options object for saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to a JSON file.
workbook.save("sample_out.json", options);
```  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
