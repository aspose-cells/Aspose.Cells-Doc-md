---
title: Converti Excel in CSV, TSV e Txt con Node.js tramite C++
linktitle: Salva come CSV, TSV e Txt
type: docs
weight: 40
url: /it/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Scopri come convertire file Excel in formati CSV, TSV e TXT usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile convertire file Excel, ODS, JSON e altri formati in CSV, TSV e TXT.

{{% /alert %}}

## **Salvataggio Workbook in formato testo o CSV**

A volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), di default, sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio attivo.

Il seguente esempio di codice spiega come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine, che può essere qualsiasi file di spreadsheet Microsoft Excel o OpenOffice (come XLS, XLSX, XLSM, XLSB, ODS, ecc.) con qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

Puoi modificare lo stesso esempio per salvare il tuo file in formato CSV. Di default, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) è una virgola, quindi non specificare un separatore se si salva in formato CSV

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Salvataggio file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Argomenti avanzati**
- [Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV](/cells/it/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
