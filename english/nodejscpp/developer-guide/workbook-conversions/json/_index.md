---  
title: Json with Node.js via C++  
linktitle: Json  
type: docs  
weight: 300  
url: /nodejs-cpp/convert-workbook-to-json/  
description: Learn how to convert Excel Workbook to JSON using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supports converting a workbook to Json (JavaScript Object Notation) file.  
{{% /alert %}}  

## **Convert Excel Workbook to JSON**  

The Aspose.Cells API provides support for converting spreadsheets to JSON format. To export the workbook to JSON, pass [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method. You may also use [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) class to specify additional settings for exporting worksheet to JSON.  

The following code example demonstrates exporting the active worksheet to JSON by using [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json) enumeration member. Please see the code to convert [source file](book1.xlsx) to the [output Json file](book1.Json) generated by the code for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Advance topics**  
- [Convert CSV to JSON](/cells/nodejs-cpp/convert-csv-to-json/)  
- [Convert-Excel-to-JSON](/cells/nodejs-cpp/convert-excel-to-json/)  
- [Convert JSON to CSV](/cells/nodejs-cpp/convert-json-to-csv/)  
- [Convert-JSON-to-Excel](/cells/nodejs-cpp/convert-json-to-excel/)  
  