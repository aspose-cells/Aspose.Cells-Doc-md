---  
title: Mostra e Nascondi Righe, Colonne e Barre di Scorrimento con Node.js tramite C++  
linktitle: Mostra e Nascondi Righe Colonne e Barre di Scorrimento  
type: docs  
weight: 20  
url: /it/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Questo articolo dimostra come mostrare e nascondere programmaticamente le righe e le colonne del foglio di lavoro di Excel utilizzando Node.js tramite C++. Controlla la visibilità delle barre di scorrimento e nascondi più righe e colonne in modo efficiente.  
---  

{{% alert color="primary" %}}  
Aspose.Cells fornisce modi per controllare la visibilità delle righe, colonne e barre di scorrimento di un foglio di lavoro.  
{{% /alert %}}  

## **Mostra e nascondi righe e colonne**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) che rappresenta tutte le celle nel foglio di lavoro. La collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.  

### **Mostra Righe e Colonne**  

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) e [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Entrambi i metodi richiedono due parametri:  

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.  
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
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
Durante la visualizzazione di una colonna nascosta, se hai bisogno di ripristinare la larghezza assegnata in precedenza o quella originale, sblocca la colonna con una larghezza negativa. Ad esempio: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Nascondi Righe e Colonne**  

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) e [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Entrambi i metodi richiedono come parametro l'indice di riga e colonna per nascondere la riga o colonna specifica.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.  
{{% /alert %}}  

### **Nascondi Più Righe e Colonne**  

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando i metodi [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) e [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Entrambi i metodi prendono come parametri l'indice di riga o colonna di partenza e il numero di righe o colonne da nascondere.  

```javascript
const fs = require('fs');
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Mostra e nascondi le barre di scorrimento**  

Le barre di scorrimento vengono utilizzate per navigare nei contenuti di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:  

- Barre di scorrimento verticali  
- Barre di scorrimento orizzontali  

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere i contenuti del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.  

### **Controllare la visibilità delle barre di scorrimento**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) offre un'ampia gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle barre di scorrimento, utilizza le proprietà [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) e [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) e [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) sono proprietà Boolean, il che significa che queste proprietà possono contenere solo valori **true** o **false**.  

#### **Rendere visibili le barre di scorrimento**  

Rendi visibili le barre di scorrimento impostando a **true** la proprietà [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) o [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

#### **Nascondere le barre di scorrimento**  

Nascondi le barre di scorrimento impostando a **false** la proprietà [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) o [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

**Codice di Esempio**  

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.  

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

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

