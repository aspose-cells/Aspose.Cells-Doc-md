---  
title: Formatta righe e colonne con Node.js tramite C++  
linktitle: Righe e colonne  
type: docs  
weight: 100  
url: /it/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ può supportare modifiche all altezza delle righe o alla larghezza delle colonne, oltre ad applicare formattazioni su righe o colonne.  
keywords: Imposta l altezza della riga e la larghezza della colonna, regola l altezza della riga e la larghezza della colonna, cambia l altezza della riga o la larghezza della colonna, formatta righe e colonne, come impostare l altezza della riga e la larghezza della colonna.  
---  

{{% alert color="primary" %}}  
Quando si lavora con fogli di calcolo e si aggiungono dati a righe o colonne, potrebbe essere necessario cambiare l'altezza delle righe o la larghezza delle colonne. A volte, applicare formattazioni significa che l'altezza o la larghezza correnti devono cambiare per mostrare i dati. Normalmente, gli utenti regolano le altezze delle righe e le larghezze delle colonne in un ambiente WYSIWYG usando Microsoft Excel. Ma, con Aspose.Cells, gli sviluppatori possono eseguire queste operazioni in fase di runtime.  
{{% /alert %}}  

## **Lavorare con le righe**  

### **Come regolare l'altezza della riga**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che permette l’accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) che rappresenta tutte le celle nel foglio di lavoro.  

La collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi più dettagliatamente di seguito.  

### **Come impostare l'altezza di una riga**  

È possibile impostare l’altezza di una singola riga chiamando il metodo [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Il metodo [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) prende i seguenti parametri:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.  
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Come impostare l'altezza di tutte le righe in un foglio di lavoro**  

Se gli sviluppatori devono impostare la stessa altezza di riga per tutte le righe del foglio di lavoro, possono farlo utilizzando la proprietà [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

**Esempio:**  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Lavorare con colonne**  

### **Come impostare la larghezza di una colonna**  

Imposta la larghezza di una colonna chiamando il metodo [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Il metodo [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) accetta i seguenti parametri:  

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.  
- **Larghezza di colonna**, la larghezza desiderata della colonna.  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Come impostare la larghezza della colonna in pixel**  

Imposta la larghezza di una colonna chiamando il metodo [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Il metodo [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) accetta i seguenti parametri:  

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.  
- **Larghezza della colonna**, la larghezza della colonna desiderata in pixel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Come impostare la larghezza di tutte le colonne in un foglio di lavoro**  

Per impostare la stessa larghezza di colonna per tutte le colonne nel foglio di lavoro, usa la proprietà [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Argomenti avanzati**  
- [Adatta automaticamente righe e colonne](/cells/it/nodejs-cpp/autofit-rows-and-columns/)  
- [Converti testo in colonne utilizzando Aspose.Cells](/cells/it/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Copia righe e colonne](/cells/it/nodejs-cpp/copying-rows-and-columns/)  
- [Elimina righe e colonne vuote in un foglio di lavoro](/cells/it/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Raggruppa e scollega righe e colonne](/cells/it/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Nascondi e mostra righe e colonne](/cells/it/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Inserisci o elimina righe in un foglio di lavoro di Excel](/cells/it/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Inserimento ed eliminazione di righe e colonne di un file di Excel](/cells/it/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Rimuovere righe duplicate in un foglio di lavoro](/cells/it/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro](/cells/it/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
