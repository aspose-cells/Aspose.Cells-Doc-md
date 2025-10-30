---  
title: Converti CSV, TSV e TXT in Excel con Node.js tramite C++  
linktitle: Converti CSV, TSV e TXT in Excel  
type: docs  
weight: 30  
url: /it/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Usando Aspose.Cells, puoi convertire file CSV in Excel, OpenOffice, PDF, JSON e molti altri formati.  
{{% /alert %}}  

## **Apertura dei file CSV**  

I file di valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati sono memorizzati come una tabella in cui ciascuna colonna è separata dal carattere virgola e citata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di virgoletta doppia, viene eseguito l'escape con una coppia di caratteri virgoletta doppia. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Apertura dei file CSV e sostituzione dei caratteri non validi**  

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto dall'API Aspose.Cells che è mostrata nell'esempio di codice qui sotto.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```  


### **Apertura dei file di testo con separatore personalizzato**  

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```  

### **Apertura dei file delimitati da tabulazione**  

I file delimitati da tabulazione (Testo) contengono dati di fogli di calcolo senza alcuna formattazione. I dati sono disposti in righe e colonne come in tabelle e fogli di calcolo. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Apertura dei file di valori separati da tabulazione (TSV)**  

I file di valori separati da tab (TSV) contengono dati di fogli di calcolo senza formattazione. È uguale a un file Tab Delimited dove i dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Argomenti avanzati**  
- [Carica o importa file CSV con formule](/cells/it/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Lettura del file CSV con codifiche multiple](/cells/it/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
