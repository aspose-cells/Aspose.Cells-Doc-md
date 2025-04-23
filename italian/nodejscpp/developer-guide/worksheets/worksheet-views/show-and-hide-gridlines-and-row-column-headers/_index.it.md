---  
title: Mostra e Nascondi le linee della griglia e le intestazioni di righe e colonne con Node.js tramite C++  
linktitle: Mostra e nasconde le linee della griglia e gli intestazioni delle righe e delle colonne  
type: docs  
weight: 30  
url: /it/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: Questo articolo fornisce esempio di codice per usare l API Node.js via C++ per nascondere o mostrare programmaticamente le linee della griglia, le intestazioni di righe e colonne di un foglio di lavoro Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporta la visualizzazione e la modifica delle linee della griglia del foglio di calcolo che sono visibili per impostazione predefinita. Fornisce anche il controllo della visibilità delle intestazioni delle righe e delle colonne del foglio di calcolo.  
{{% /alert %}}  

## **Mostrare e nascondere le linee della griglia**  

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle in modo che sia facile inserire dati in celle specifiche. Le linee di griglia ci consentono di visualizzare un foglio di calcolo come una collezione di celle, in cui ogni cella è facilmente identificabile.  

### **Controllo della visibilità delle linee della griglia**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle linee della griglia, usa la proprietà [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) è una proprietà Booleana, il che significa che può memorizzare solo un valore **vero** o **falso**.  

#### **Rendere Visibili le Linee della Griglia**  

Rendi visibili le linee della griglia impostando la proprietà [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) su **true**.  

#### **Nascondere le Linee della Griglia**  

Nascondi le linee della griglia impostando la proprietà [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) su **false**.  

Un esempio completo è dato di seguito che dimostra l'uso della proprietà [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) aprendo un file Excel (book1.xls), nascondendo le linee della griglia sul primo foglio di lavoro e salvando il file modificato come output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Mostra e nasconde gli intestazioni delle righe e delle colonne**  

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare singole celle. Ad esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate in modo alfabetico – A, B, C, D, ecc. I valori delle righe e delle colonne sono visualizzati negli intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni delle righe e delle colonne.  

### **Controllo della visibilità dei fogli di lavoro**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle intestazioni di righe e colonne, usa la proprietà [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) è una proprietà Booleana, il che significa che può memorizzare solo un valore **vero** o **falso**.  

#### **Rendere visibili le intestazioni di riga/colonna**  

Rendi visibili le intestazioni di righe e colonne impostando la proprietà [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) su **true**.  

#### **Nascondere le intestazioni di riga/colonna**  

Nascondi le intestazioni di righe e colonne impostando la proprietà [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) su **false**.  

Esempio completo in basso che mostra come utilizzare la proprietà [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) aprendo un file excel (book1.xls), nascondendo le intestazioni di riga e colonna nel primo foglio di lavoro e salvando il file modificato come output.xls.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
È anche possibile usare i metodi [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) e [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) della classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) per rendere visibili più righe e colonne.  
{{% /alert %}}  

