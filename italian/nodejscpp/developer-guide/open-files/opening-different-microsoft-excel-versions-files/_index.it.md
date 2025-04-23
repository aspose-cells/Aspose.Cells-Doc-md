---
title: Apri file di versioni diverse di Microsoft Excel con Node.js tramite C++
linktitle: Apri diversi file di Microsoft Excel in versioni diverse
type: docs
weight: 20
url: /it/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Questo articolo spiega come aprire file di diverse versioni di Excel usando Aspose.Cells for Node.js via C++.
keywords: Node.js Apri file di Microsoft Excel differenti tramite C++, come posso aprire file Excel crittografati Node.js tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Come aprire file di diverse versioni di Microsoft Excel**

Un’applicazione spesso deve poter aprire file Microsoft Excel creati in versioni differenti, per esempio Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potrebbe essere necessario caricare un file in uno dei vari formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e altri. Usa il costruttore, o specifica l’attributo di tipo [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che indica il formato usando l’enumerazione [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype).

L’enumerazione [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) contiene molti formati di file predefiniti, alcuni dei quali sono i seguenti.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|Csv|Rappresenta un file CSV|
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx|Rappresenta un file XLSX Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsm|Rappresenta un file XLSM Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltx|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltm|Rappresenta un file XLTM macro abilitato di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|SpreadsheetML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|Ods|Rappresenta un file ODS|
|Html|Rappresenta un file HTML|
|Mhtml|Rappresenta un file MHTML|

### **Apri file Microsoft Excel 95/5.0**

Per aprire un file Microsoft Excel 95/5.0, usa [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e imposta l'attributo correlato per la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) del file di modello da caricare. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[File di Excel95](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Apri file Microsoft Excel 97 - 2003**

Per aprire un file Microsoft Excel 97 - 2003, usa [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e imposta l'attributo correlato per la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) del file di modello da caricare.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Apri file XLSX di Microsoft Excel 2007/2010/2013/2016/2019 e Office 365**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specifica il percorso del file. Puoi anche usare [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e impostare gli attributi/opzioni correlati della classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) per il file di modello da caricare.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **Apri file Excel criptati**

È possibile creare file Excel crittografati usando Microsoft Excel. Per aprire un file crittografato, usa [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e imposta i suoi attributi e opzioni (ad esempio, fornisce una password) per il file di modello da caricare.
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


