---  
title: Mostra e Nascondi Fogli di Lavoro e Schede con Node.js tramite C++  
linktitle: Mostrare e Nascondere Fogli e Schede  
type: docs  
weight: 10  
url: /it/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Questo articolo fornisce codice di esempio per utilizzare l API Node.js o la libreria Node.js per visualizzare e nascondere programmaticamente un foglio di lavoro di Excel. Inoltre, come mostrare e nascondere le schede del workbook di Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells consente all'utente di mostrare e nascondere elementi di un documento, inclusi fogli e schede.  
{{% /alert %}}  

## **Mostra e nascondi un foglio di lavoro**  

Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dagli altri fogli di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte gli sviluppatori possono richiedere di nascondere alcuni fogli di lavoro e rendere visibili altri fogli di lavoro nel file Excel per il proprio interesse. Quindi, **Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei propri file Excel.  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette l'accesso a ogni foglio di lavoro nel file Excel.  

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per controllare la visibilità di un foglio, usa la proprietà [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) è una proprietà booleana, che significa che può contenere solo un valore **true** o **false**.  

### **Rendere un foglio di lavoro visibile**  

Rendi visibile un foglio impostando la proprietà [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a **true**.  

### **Nascondere un foglio di lavoro**  

Nascondi un foglio impostando la proprietà [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a **false**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Mostrare e Nascondere Schede**  

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:  

- Schede del foglio.  
- Pulsanti di scorrimento delle schede.  

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.  

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede del foglio e dei pulsanti di scorrimento delle schede nei file di Excel.  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono usare la proprietà [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) è una proprietà booleana, che significa che può contenere solo un valore **true** o **false**.  

### **Rendere visibili le schede con il metodo {1} della classe {0}.**  

Rendi le schede visibili impostando la proprietà [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) a **true**.  

### **Nascondere le schede**  

Nascondi le schede in un file Excel impostando la proprietà [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) a **false**.  

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede del documento sono nascoste.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Controllare la larghezza della barra delle schede**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

