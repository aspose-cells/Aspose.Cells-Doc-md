---  
title: Convert JSON to CSV with Node.js via C++  
linktitle: Convert JSON to CSV  
type: docs  
weight: 210  
url: /nodejs-cpp/convert-json-to-csv/  
description: Learn how to convert JSON data to CSV using Aspose.Cells for Node.js via C++.  
---  
  
## **Convert JSON to CSV**  
  
Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) class provides the options for JSON layout like  [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) class.  
  
The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) classes to load the [source JSON file](104398869.json) and generates the [output CSV file](104398870.csv).  
  
### **Sample Code**  
  
```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  
  