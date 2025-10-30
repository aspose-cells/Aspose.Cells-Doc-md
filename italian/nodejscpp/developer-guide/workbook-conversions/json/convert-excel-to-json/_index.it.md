---  
title: Converti Excel in JSON con Node.js tramite C++  
linktitle: Convert Excel to JSON  
type: docs  
weight: 300  
url: /it/nodejs-cpp/convert-excel-to-json/  
description: Impara come convertire un file Excel in JSON usando Aspose.Cells for Node.js via C++.  
keywords: Esportando un Workbook in JSON Node.js tramite C++, Converti Excel in JSON Node.js tramite C++  
---  

{{% alert color="primary" %}}  
 Aspose.Cells supporta la conversione di un Workbook in file JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Converti Workbook Excel in JSON**  

 Non c'è bisogno di chiedersi come convertire un Workbook Excel in JSON, perché la libreria Aspose.Cells for Node.js via C++ fornisce la soluzione migliore. L'API Aspose.Cells offre supporto per la conversione di fogli di calcolo in formato JSON. Per esportare il workbook in JSON, passa [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) come secondo parametro del metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in JSON.  

 Il seguente esempio di codice dimostra l'esportazione di un Excel Workbook in JSON. Consulta il codice per convertire il [file sorgente](sample.xlsx) nel file JSON generato dal codice come riferimento.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

 Il seguente esempio di codice usa la classe JsonSaveOptions per specificare impostazioni aggiuntive e dimostra come esportare un Excel Workbook in JSON. Consulta il codice per convertire il [file sorgente](sample.xlsx) nel file JSON come riferimento.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
