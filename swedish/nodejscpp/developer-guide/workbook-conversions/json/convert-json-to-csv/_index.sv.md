---  
title: Konvertera JSON till CSV med Node.js via C++  
linktitle: Konvertera JSON till CSV  
type: docs  
weight: 210  
url: /sv/nodejs-cpp/convert-json-to-csv/  
description: Lär dig hur man konverterar JSON data till CSV med Aspose.Cells for Node.js via C++.  
---  

## **Konvertera JSON till CSV**  

Aspose.Cells stöder konvertering av enkel och inbäddad JSON till CSV. För detta tillhandahåller API:n [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)-klasser. [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)-klassen tillhandahåller alternativen för JSON-layout som [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (behandlar arrayen som en tabell). [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)-klassen bearbetar JSON:en med layoutalternativen som anges med [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)-klassen.  

Följande kodexempel visar användningen av klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) för att ladda [käljsonfil](104398869.json) och generera [utdata CSV-fil](104398870.csv).  

### **Exempelkod**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
