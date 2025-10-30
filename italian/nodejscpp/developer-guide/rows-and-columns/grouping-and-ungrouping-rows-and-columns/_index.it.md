---
title: Gruppare e sgrouppare righe e colonne con Node.js tramite C++
linktitle: Raggruppamento e Sgrovigliamento di Righe e Colonne
type: docs
weight: 50
url: /it/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Scopri come raggruppare e separare righe e colonne in Excel usando Aspose.Cells for Node.js via C++.
--- 

## **Introduzione**

In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Riepilogo**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono riepiloghi o intestazioni per sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un riepilogo o intestazione individuale come mostrato di seguito nella figura:

|**Raggruppamento di Righe e Colonne**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestione gruppi di righe e colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) che rappresenta tutte le celle nel foglio di lavoro.

La collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in dettaglio.

### **Raggruppamento di Righe e Colonne**

È possibile raggruppare righe o colonne chiamando i metodi [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) e [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Entrambi i metodi accettano i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Impostazioni di raggruppamento**

Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Le colonne di riepilogo a destra del dettaglio.

Gli sviluppatori possono configurare queste impostazioni di raggruppamento utilizzando la proprietà [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

### **Riepiloghi delle Righe al di Sotto del Dettaglio**

È possibile controllare se le righe di riepilogo vengono visualizzate sotto i dettagli impostando la proprietà [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) della classe [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) su **true** o **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Colonne sommario a destra dei dettagli**

Gli sviluppatori possono anche controllare la visualizzazione delle colonne di riepilogo a destra dei dettagli impostando la proprietà [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) della classe [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) su **true** o **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Separazione delle righe e delle colonne**

Per slegare qualsiasi riga o colonna raggruppata, chiamare le funzioni [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) e [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Entrambi i metodi accettano due parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) ha una sovraccarico che accetta un terzo parametro Booleano. Impostarlo su **true** rimuove tutte le informazioni di gruppo. Altrimenti, viene rimossa solo l'informazione del gruppo esterno.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
