---
title: Caricamento e gestione di file Excel, OpenOffice, Json, Csv e Html
linktitle: Aprire i file
type: docs
weight: 20
url: /it/nodejs-cpp/loading-saving-and-managing/
description: Con Aspose.Cells, è semplice creare, aprire e gestire file Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Immagine, Mht e XPS usando Node.js tramite C++.
---

{{% alert color="primary" %}}

Con Aspose.Cells, è semplice creare, aprire e gestire file Excel, ad esempio per recuperare dati, o usare un modello di designer per accelerare lo sviluppo.

{{% /alert %}}

## **Creazione di un nuovo foglio di lavoro**
Il seguente esempio crea un nuovo workbook da zero.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Apertura e salvataggio di un file**
Con Aspose.Cells, è semplice aprire, salvare e gestire file Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Argomenti avanzati**
- [Diversi modi per aprire i file](/cells/it/nodejs-cpp/different-ways-to-open-files/)
- [Filtra i nomi definiti durante il caricamento del foglio di lavoro](/cells/it/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Filtra gli oggetti durante il caricamento del foglio di lavoro o del foglio di calcolo](/cells/it/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrare il tipo di dati durante il caricamento del libro di lavoro da file modello](/cells/it/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Ottieni avvisi durante il caricamento del file Excel](/cells/it/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Carica il file Excel di origine senza grafici](/cells/it/nodejs-cpp/load-source-excel-file-without-charts/)
- [Carica fogli di lavoro specifici in un libro di lavoro](/cells/it/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Carica il libro di lavoro con il formato di carta della stampante specificato](/cells/it/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Apertura di file di diverse versioni di Microsoft Excel](/cells/it/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Apertura di file con formati diversi](/cells/it/nodejs-cpp/opening-files-with-different-formats/)
- [Ottimizzazione dell'utilizzo della memoria durante il lavoro con file grandi che contengono grandi set di dati](/cells/it/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leggi i fogli di calcolo di Numbers sviluppati da Apple Inc. utilizzando Aspose.Cells](/cells/it/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo](/cells/it/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilizzo di API LightCells](/cells/it/nodejs-cpp/using-lightcells-api/)
- [Convertire CSV in JSON](/cells/it/nodejs-cpp/convert-csv-to-json/)
- [Converti Excel in JSON](/cells/it/nodejs-cpp/convert-excel-to-json/)
- [Convertire JSON in CSV](/cells/it/nodejs-cpp/convert-json-to-csv/)
- [Converti JSON in Excel](/cells/it/nodejs-cpp/convert-json-to-excel/)
- [Converti Excel in Html](/cells/it/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
