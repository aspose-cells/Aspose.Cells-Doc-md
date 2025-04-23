---
title: Apertura di file con formati diversi con Node.js tramite C++
linktitle: Apertura dei file con formati diversi
type: docs
weight: 30
url: /it/nodejs-cpp/opening-files-with-different-formats/
description: L API Aspose.Cells for Node.js via C++ consente di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: Aprire file xlsx, aprire file html, leggere file fods, leggere file ods, leggere file sxc, aprire file csv, Separato da tabulazione, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells, puoi aprire file con formati diversi. **Aspose.Cells** può aprire una vasta gamma di formati di file come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), file delimitati da tabulazione o valori separati da tab (TSV), ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati file supportati](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con formati diversi come SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazione o valori separati da tabulazione (TSV), file ODS. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per l'apertura di file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo che includono tutte le informazioni, come formattazione, formule, ecc. Dalla versione Microsoft Excel XP, viene aggiunta un'opzione di esportazione XML che consente di esportare i fogli di calcolo in file SpreadsheetML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **Apertura dei file HTML**

Aspose.Cells consente di aprire un file HTML in un oggetto Workbook. Il file HTML dovrebbe essere orientato a Microsoft Excel, cioè, MS-Excel dovrebbe essere in grado di aprirlo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record dove i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ogni colonna è separata dal carattere virgola e quotata con il carattere virgolette doppie. Se un valore di campo contiene un carattere virgolette doppie, viene escapato con una coppia di caratteri virgolette doppie. Puoi anche usare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto dall'API Aspose.Cells che è mostrata nell'esempio di codice qui sotto.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


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
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Apertura dei file di valori separati da tabulazione (TSV)**

Il file di valori separati da tabulazione (TSV) contiene dati di fogli di calcolo ma senza alcuna formattazione. È uguale a un file delimitato da tabulazioni dove i dati sono disposti in righe e colonne come in tabelle e fogli di calcolo.

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

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con estensione SXC. Il file SXC è anche usato per i file di fogli di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere file SXC come dimostrato dal seguente esempio di codice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Apertura dei file FODS**

Il file FODS è un foglio di calcolo salvato in XML OpenDocument senza compressione. Aspose.Cells può leggere file FODS come dimostrato dal seguente esempio di codice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

