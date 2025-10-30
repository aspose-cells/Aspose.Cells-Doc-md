---  
title: Konvertieren Sie JSON nach CSV mit Node.js via C++  
linktitle: Konvertieren Sie JSON in CSV  
type: docs  
weight: 210  
url: /de/nodejs-cpp/convert-json-to-csv/  
description: Lernen Sie, wie Sie JSON Daten mithilfe von Aspose.Cells for Node.js via C++ in CSV konvertieren.  
---  

## **JSON in CSV konvertieren**  

Aspose.Cells unterstützt die Konvertierung von einfachem und verschachteltem JSON in CSV. Dafür bietet die API die Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) und [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility). Die [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)-Klasse bietet Optionen für das JSON-Layout wie [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (verarbeitet das Array als Tabelle). Die [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)-Klasse verarbeitet JSON unter Verwendung der mit der [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)-Klasse gesetzten Layout-Optionen.  

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) und [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility), um die [Quelldatei JSON](104398869.json) zu laden und die [Ausgabedatei CSV](104398870.csv) zu generieren.  

### **Beispielcode**  

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
