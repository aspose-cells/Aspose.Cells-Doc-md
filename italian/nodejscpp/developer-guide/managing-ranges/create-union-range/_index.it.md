---  
title: Crea intervallo unito con Node.js via C++  
linktitle: Crea un intervallo di unione  
type: docs  
weight: 360  
url: /it/nodejs-cpp/create-union-range/  
description: Impara come creare un intervallo unito usando Aspose.Cells for Node.js via C++.  
keywords: Crea intervallo unito Node.js via C++, Intervallo unito Aspose.Cells Node.js, WorksheetCollection crea intervallo unito Node.js  
---  

## **Crea un intervallo di unione**  
Aspose.Cells fornisce la possibilità di creare un intervallo unito usando il metodo [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Il metodo [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) accetta due parametri, l'indirizzo per creare l'intervallo unito e l'indice del foglio di lavoro. Il metodo restituisce un oggetto [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange).  

Il seguente frammento di codice dimostra come creare un intervallo unito usando il metodo [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Il file di output generato dal codice è allegato per riferimento.  

- [File di output](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
