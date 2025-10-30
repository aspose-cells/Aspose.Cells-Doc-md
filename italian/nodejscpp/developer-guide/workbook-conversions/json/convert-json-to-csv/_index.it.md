---  
title: Converti JSON in CSV con Node.js tramite C++  
linktitle: Converti JSON in CSV  
type: docs  
weight: 210  
url: /it/nodejs-cpp/convert-json-to-csv/  
description: Impara come convertire dati JSON in CSV usando Aspose.Cells for Node.js via C++.  
---  

## **Convertire JSON in CSV**  

 Aspose.Cells supporta la conversione di JSON semplice e annidato in CSV. Per questo, l'API fornisce le classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) fornisce le opzioni per il layout JSON come [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (elabora l'array come tabella). La classe [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) elabora il JSON utilizzando le opzioni di layout impostate con la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions).  

 Il seguente esempio di codice dimostra l'uso delle classi [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) e [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) per caricare il [file JSON sorgente](104398869.json) e genera il [file CSV di output](104398870.csv).  

### **Codice di Esempio**  

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
