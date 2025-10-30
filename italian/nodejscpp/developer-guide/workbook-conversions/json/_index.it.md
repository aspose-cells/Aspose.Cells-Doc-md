---  
title: Json con Node.js via C++  
linktitle: Json  
type: docs  
weight: 300  
url: /it/nodejs-cpp/convert-workbook-to-json/  
description: Impara come convertire un Workbook Excel in JSON usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporta la conversione di un workbook in file Json (JavaScript Object Notation).  
{{% /alert %}}  

## **Converti Workbook Excel in JSON**  

L’API Aspose.Cells supporta la conversione dei fogli di calcolo in formato JSON. Per esportare il workbook in JSON, passa [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) per specificare ulteriori impostazioni per l’esportazione del foglio di lavoro in JSON.  

Il seguente esempio di codice dimostra come esportare il foglio attivo in JSON usando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json). Consulta il codice per convertire il [file sorgente](book1.xlsx) nel [file Json di output](book1.Json) generato dal codice come riferimento.  

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

## **Argomenti avanzati**  
- [Convertire CSV in JSON](/cells/it/nodejs-cpp/convert-csv-to-json/)  
- [Converti-Excel-in-JSON](/cells/it/nodejs-cpp/convert-excel-to-json/)  
- [Convertire JSON in CSV](/cells/it/nodejs-cpp/convert-json-to-csv/)  
- [Converti-JSON-in-Excel](/cells/it/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
