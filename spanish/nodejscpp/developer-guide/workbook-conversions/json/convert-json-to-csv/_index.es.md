---  
title: Convertir JSON a CSV con Node.js a través de C++  
linktitle: Convertir JSON a CSV  
type: docs  
weight: 210  
url: /es/nodejs-cpp/convert-json-to-csv/  
description: Aprende cómo convertir datos JSON a CSV usando Aspose.Cells for Node.js via C++.  
---  

## **Convertir JSON a CSV**  

 Aspose.Cells soporta convertir JSON simple así como anidado a CSV. Para ello, la API proporciona las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility). La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) ofrece las opciones para el diseño JSON como [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (procesa el array como una tabla). La clase [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) procesa el JSON usando las opciones de diseño establecidas con la clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions).  

El siguiente ejemplo de código demuestra el uso de las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) para cargar el archivo [JSON fuente](104398869.json) y genera el [archivo CSV de salida](104398870.csv).  

### **Código de muestra**  

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
