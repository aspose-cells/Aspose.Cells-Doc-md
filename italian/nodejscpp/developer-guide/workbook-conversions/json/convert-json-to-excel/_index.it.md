---
title: Converti JSON in Excel con Node.js tramite C++
linktitle: Converti JSON in Excel
type: docs
weight: 300
url: /it/nodejs-cpp/convert-json-to-excel/
description: Impara come convertire JSON in file Excel con Aspose.Cells for Node.js via C++.
keywords: Importare JSON senza Office 2013, Office 2016, Office 2019 e Office 365 usando Node.js tramite C++.
---

{{% alert color="primary" %}}

 Aspose.Cells supporta la conversione di un file JSON (JavaScript Object Notation) in un Workbook Excel.

{{% /alert %}}

## **Converti JSON in Excel Workbook**
 Non c'è bisogno di chiedersi come convertire JSON in file Excel, perché Aspose.Cells for Node.js via C++ fornisce la soluzione migliore. L'API Aspose.Cells fornisce supporto per la conversione di JSON in fogli di calcolo. Puoi usare la classe [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) per specificare impostazioni aggiuntive per l'importazione di JSON in Workbook.

Il seguente esempio di codice dimostra l'importazione del JSON nel foglio di lavoro di Excel. Si prega di vedere il codice per convertire il [file di origine](sample.json) nel file xlsx generato dal codice a titolo di riferimento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

 Il seguente esempio di codice, che utilizza la classe JsonLoadOptions per specificare impostazioni aggiuntive, dimostra come importare JSON in un Excel Workbook. Consulta il codice per convertire [file sorgente](sample.json) nel file xlsx generato dal codice come riferimento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

 Il seguente esempio di codice dimostra l'importazione di una stringa JSON in un Excel Workbook. Puoi anche specificare la posizione del layout durante l'importazione di JSON. Consulta il codice per convertire una stringa JSON in un file xlsx generato dal codice come riferimento.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
