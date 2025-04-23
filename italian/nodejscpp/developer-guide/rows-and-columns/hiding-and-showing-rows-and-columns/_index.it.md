---
title: Nascondere e mostrare righe e colonne con Node.js tramite C++
linktitle: Nascondere e mostrare righe e colonne
type: docs
weight: 60
url: /it/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Impara come nascondere e mostrare righe e colonne in un foglio di lavoro usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

A volte ha senso nascondere alcune righe o colonne in un foglio di lavoro e mostrarle successivamente. Microsoft Excel fornisce questa funzione e anche Aspose.Cells.

{{% /alert %}}

## **Controllo della visibilità di righe e colonne**

Aspose.Cells for Node.js via C++ offre una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che consente ai sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) che rappresenta tutte le celle nel foglio di lavoro. La collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

### **Nascondere righe e colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) e [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Entrambi i metodi richiedono come parametro l'indice di riga e colonna per nascondere la riga o colonna specifica.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

### **Mostrare righe e colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) e [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Entrambi i metodi richiedono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

Durante la visualizzazione di una colonna nascosta, se si necessita di ripristinarla alla larghezza precedentemente assegnata o alla sua larghezza originale, si prega di sbloccare la colonna con una larghezza negativa. Per esempio: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Nascondere più righe e colonne**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando i metodi [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) e [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Entrambi i metodi prendono come parametri l'indice di riga o colonna di partenza e il numero di righe o colonne da nascondere.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

È anche possibile usare i metodi [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) e [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) della classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
