---  
title: Gestisci i fogli di lavoro dei file Microsoft Excel con Node.js tramite C++  
linktitle: Fogli di lavoro  
type: docs  
weight: 90  
url: /it/nodejs-cpp/manage-worksheets/  
description: Aggiungi, rimuovi e attiva fogli di lavoro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
I programmatori possono creare e gestire facilmente i fogli di lavoro nei file di Microsoft Excel in modo programmatico utilizzando l'API flessibile di Aspose.Cells. Questo argomento descrive gli approcci per aggiungere e rimuovere i fogli di lavoro nei file di Microsoft Excel.  
{{% /alert %}}  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ogni foglio di lavoro nel file Excel.  

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre un'ampia gamma di proprietà e metodi per gestire i fogli di lavoro.  

## **Aggiungere fogli di lavoro a un nuovo file Excel**  

Per creare un nuovo file Excel in modo programmatico:  

1. Crea un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. Chiama il metodo [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel. Può essere riferito passando l'indice del foglio di lavoro al [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collezione.  
1. Ottenere un riferimento al foglio di lavoro.  
1. Lavorare sui fogli di lavoro.  
1. Salva il nuovo file Excel con fogli di lavoro nuovi chiamando il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**  

Il processo di aggiunta di fogli di lavoro a un foglio di lavoro di progettazione è lo stesso di aggiungere un nuovo foglio di lavoro, tranne per il fatto che il file Excel esiste già e deve essere aperto prima di aggiungere i fogli di lavoro. Un file di progettazione può essere aperto dalla classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Accesso ai fogli di lavoro utilizzando il nome del foglio**  

Accedi a qualsiasi foglio di lavoro specificando il suo nome o indice.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Rimozione dei fogli di lavoro utilizzando il nome del foglio**  

Per rimuovere fogli di lavoro da un file, chiama il metodo [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Passa il nome del foglio al metodo [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) per rimuovere un foglio di lavoro specifico.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**  

Rimuovere fogli di lavoro per nome funziona bene quando si conosce il nome del foglio di lavoro. Se non si conosce il nome, usare una versione sovraccaricata del metodo [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) che prende l'indice del foglio di lavoro invece del suo nome.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Attivare fogli e fare di una cella attiva nel foglio di lavoro**  

A volte, è necessario attivare e visualizzare un foglio di lavoro specifico quando un utente apre un file Microsoft Excel in Excel. Allo stesso modo, si potrebbe voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva. Aspose.Cells è in grado di eseguire tutte queste operazioni.  

Un **foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.  

Una **cella attiva** è una cella selezionata, la cella in cui i dati vengono inseriti quando si inizia a digitare. Solo una cella è attiva alla volta. La cella attiva è evidenziata da un bordo spesso.  

### **Attivare fogli e rendere una cella attiva**  

Aspose.Cells fornisce chiamate API specifiche per attivare un foglio e una cella. Ad esempio, la proprietà [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) è utile per impostare il foglio attivo in una cartella di lavoro. Allo stesso modo, la proprietà [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) viene utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.  

Per assicurarti che le barre di scorrimento orizzontali o verticali siano posizionate alla riga e alla colonna di indice desiderati per mostrare dati specifici, usa le proprietà [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) e [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

L'esempio seguente mostra come attivare un foglio di lavoro e rendere una cella attiva in esso. Nell'output generato, le barre di scorrimento verranno scorrere per fare in modo che la seconda riga e la seconda colonna siano la loro prima riga e colonna visibile.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Argomenti avanzati**  
- [Copia e Sposta Fogli di Lavoro](/cells/it/nodejs-cpp/copying-and-moving-worksheets/)  
- [Contare il numero di celle nel foglio di lavoro](/cells/it/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Rilevamento di fogli di lavoro vuoti](/cells/it/nodejs-cpp/detecting-empty-worksheets/)  
- [Trova se il foglio di lavoro è un foglio di dialogo](/cells/it/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Ottieni l'ID univoco del foglio di lavoro](/cells/it/nodejs-cpp/get-worksheet-unique-id/)  
- [Creare, Manipolare o Rimuovere scenari dai fogli di lavoro](/cells/it/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Gestione interruzioni di pagina](/cells/it/nodejs-cpp/managing-page-breaks/)  
- [Funzionalità Impostazioni pagina](/cells/it/nodejs-cpp/page-setup-features/)   
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Visualizzazioni del foglio di lavoro](/cells/it/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
