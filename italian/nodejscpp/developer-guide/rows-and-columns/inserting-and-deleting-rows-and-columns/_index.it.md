---
title: Inserimento ed eliminazione di righe e colonne del file Excel
linktitle: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 70
url: /it/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Questo articolo mostra come inserire e eliminare righe e colonne tramite l API Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js tramite C++ gestisce righe e colonne, inserisce righe e colonne, elimina righe e colonne
---

## **Introduzione**

Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo dover aggiungere righe o colonne aggiuntive per ospitare più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro. 
Per soddisfare questi requisiti, Aspose.Cells for Node.js via C++ fornisce una serie molto semplice di classi e metodi, discussi di seguito.

### **Gestire righe e colonne**

Aspose.Cells for Node.js via C++ fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) che rappresenta tutte le celle nel foglio di lavoro.

 La collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}}

Quando si aggiungono righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso o a destra, e se si rimuovono righe o colonne, il contenuto viene spostato verso l'alto o a sinistra.

{{% /alert %}}


## **Inserire righe e colonne**

### **Come inserire una riga**

Inserire una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) della raccolta [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) richiede l'indice della riga in cui verrà inserita la nuova riga.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Come inserire più righe**

Per inserire più righe in un foglio di lavoro, chiamare il metodo [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) richiede due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, il numero totale di righe da inserire.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Come inserire una riga con formattazione**

Per inserire una riga con opzioni di formattazione, utilizzare il sovraccarico [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) che richiede [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) come parametro. Impostare la proprietà [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) della classe [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) con l'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/). L'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) ha tre membri come indicato di seguito.

- Uguale a sopra: Formatta la riga come la riga precedente.
- UgualeAlSotto: Formatta la riga come la riga sottostante.
- Cancella: Cancella la formattazione.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Come inserire una colonna**

Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) richiede l'indice della colonna in cui verrà inserita la nuova colonna.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Eliminare righe e colonne**

### **Come eliminare più righe**

Per eliminare più righe da un foglio di lavoro, chiamare il metodo [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) richiede due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, il numero totale di righe da eliminare.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Come eliminare una colonna**

Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) richiede l'indice della colonna da eliminare.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
