---
title: Modi Diversi per Aprire File con Node.js tramite C++
linktitle: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/nodejs-cpp/different-ways-to-open-files/
description: Questo articolo spiega come aprire un file Excel usando l API Aspose.Cells for Node.js via C++.
keywords: Node.js Apri un file Excel senza Excel, Come apro un file Excel usando Node.js.
---

{{% alert color="primary" %}}

Con Aspose.Cells, è semplice aprire file, ad esempio, per recuperare dati, o usare un modello di progettazione per accelerare il processo di sviluppo.

{{% /alert %}}

## **Come aprire un file Excel tramite un percorso**

Gli sviluppatori possono aprire un file Microsoft Excel usando il percorso del file sul computer locale specificandolo nel costruttore della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Basta passare il percorso come *stringa* nel costruttore. Aspose.Cells rileva automaticamente il tipo di formato del file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Come aprire un file Excel tramite uno stream**

È anche semplice aprire un file Excel come stream. Per farlo, usa una versione sovraccaricata del costruttore che prende l'oggetto *Stream* che contiene il file.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Come aprire un file con solo dati**

Per aprire un file con solo dati, usa le classi [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) per impostare gli attributi e le opzioni correlate delle classi per il file modello da caricare.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Come caricare solo fogli visibili**

Mentre si carica un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), a volte potrebbe essere sufficiente avere solo i dati nelle fogli visibili di un workbook. Aspose.Cells permette di saltare i dati nelle fogli invisibili durante il caricamento di un workbook. Per farlo, crea una funzione personalizzata che eredita dalla classe [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) e passa la sua istanza alla proprietà [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Ecco l'implementazione della classe *CustomLoad* referenziata nel codice sopra.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file non nativi di Excel o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) usando Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Ci sono buone possibilità che il costruttore [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) possa generare *OutOfMemoryError* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile è insufficiente per caricare completamente il foglio di calcolo in memoria; pertanto, il foglio di calcolo deve essere caricato abilitando le Preferenze di Memoria.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
