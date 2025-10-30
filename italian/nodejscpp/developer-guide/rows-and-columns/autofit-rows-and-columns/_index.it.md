---  
title: Adatta automaticamente righe e colonne con Node.js tramite C++  
linktitle: Adatta automaticamente righe e colonne  
type: docs  
weight: 20  
url: /it/nodejs-cpp/autofit-rows-and-columns/  
description: Questo articolo mostra come adattare automaticamente righe, colonne, righe di celle unite e righe in un intervallo di celle usando Aspose.Cells for Node.js via C++.  
keywords: Adattamento automatico di righe con Node.js tramite C++, adattamento automatico di colonne con Node.js tramite C++, adattamento automatico di riga in un intervallo di celle con Node.js tramite C++, adattamento automatico di righe di celle unite con Node.js tramite C++  
---  

{{% alert color="primary" %}}  
 Microsoft Excel consente agli utenti di ridimensionare automaticamente la larghezza e l'altezza delle celle in base al contenuto. Questa funzionalità è disponibile anche tramite Aspose.Cells for Node.js via C++, quindi gli sviluppatori possono impostare automaticamente le dimensioni di una cella durante l'esecuzione.  
{{% /alert %}}  

## **Adattamento automatico**  

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo analizza l'uso della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) per adattare automaticamente righe o colonne.  

### **Adatta automaticamente la riga - Semplice**  

L'approccio più semplice per adattare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Il metodo [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) accetta come parametro un indice di riga (della riga da ridimensionare).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Come adattare automaticamente la riga in un intervallo di celle**  

Una riga è composta da molte colonne. Aspose.Cells permette agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata del metodo [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-). Prende i seguenti parametri:  

- **Indice riga**, l'indice della riga da adattare automaticamente.  
- **Primo indice colonna**, l'indice della prima colonna della riga.  
- **Ultimo indice colonna**, l'indice dell'ultima colonna della riga.  

Il metodo [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) verifica i contenuti di tutte le colonne della riga e quindi la adatta automaticamente.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Come adattare automaticamente la colonna in un intervallo di celle**  

Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto in un intervallo di celle della colonna chiamando una versione sovraccaricata del metodo [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) che accetta i seguenti parametri:  

- **Indice colonna**, l'indice della colonna da adattare automaticamente.  
- **Primo indice riga**, l'indice della prima riga della colonna.  
- **Ultimo indice di riga**, l'indice dell'ultima riga della colonna.  

Il metodo [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) verifica i contenuti di tutte le righe nella colonna e quindi adatta automaticamente la colonna.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Come adattare automaticamente le righe per le celle unite**  

 Con Aspose.Cells, è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) fornisce la proprietà [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) che può essere usata per adattare automaticamente le righe delle celle unite. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) accetta un enumerabile [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) che ha i seguenti membri.  

- Nessuno: Ignora le celle unite.  
- PrimaLinea: espande solo l'altezza della prima riga.  
- UltimaLinea: espande solo l'altezza dell'ultima riga.  
- OgniLinea: espande solo l'altezza di ogni riga.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
Puoi anche provare a usare le versioni sovraccariche dei metodi [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) che accettano un intervallo di righe/colonne e un'istanza di [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) per adattare automaticamente le righe/colonne selezionate con il [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) desiderato.  

Le firme dei metodi sopra indicati sono le seguenti:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Importante sapere**  

{{% alert color="primary" %}}  
Se una cella è unita, i metodi autoFit non verranno applicati, lo stesso comportamento di Microsoft Excel. Puoi aggirare questo problema usando l'API di autofiltro. Inoltre, se il testo in una cella è avvolto, anche il metodo [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) non verrà applicato. Un'altra cosa importante da sapere è che i metodi *autoFit* sono dispendiosi in termini di tempo. Pertanto, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.  
{{% /alert %}}  

## **Argomenti avanzati**  
- [Adattare automaticamente le righe per le celle unite](/cells/it/nodejs-cpp/autofit-rows-for-merged-cells/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
