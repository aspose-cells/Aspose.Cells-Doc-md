---
title: Diversi modi per salvare i file con Node.js tramite C++
linktitle: Salva file
type: docs
weight: 40
url: /it/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ può salvare file in formati diversi tra cui PDF, HTML, DOCX, PPTX, JSON e MHTML.
keywords: Aspose.Cells salva Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML e altri formati usando Node.js tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile creare e salvare file. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}}

## **Diversi modi per salvare i file**

Aspose.Cells fornisce il [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel e fornisce le proprietà e i metodi necessari per lavorare con i file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fornisce il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) usato per salvare i file Excel. Il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) ha molte sovraccarichi utilizzati per salvare i file in modi diversi.

Il formato del file in cui il file viene salvato è deciso dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
| CSV | Rappresenta un file CSV |
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx| Rappresenta un file Excel 2007 XLSX |
|Xlsm| Rappresenta un file Excel 2007 XLSM |
|Xltx| Rappresenta un modello di Excel 2007 XLTX |
|Xltm|Rappresenta un file XLTM abilitato per macro di Excel 2007|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007|
|SpreadsheetML|Rappresenta un file XML di fogli di calcolo|
|TSV|Rappresenta un file di valori separati da tabulazione|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|Html|Rappresenta file HTML|
|MHtml|Rappresenta file MHTML|
|Pdf|Rappresenta un file PDF|
|XPS|Rappresenta un documento XPS|
|TIFF|Rappresenta il formato di file immagine TIFF (Tagged Image File Format)|

## **Come Salvare File in Diversi Formati**

Per salvare i file in una posizione di archiviazione, specifica il nome del file (completo di percorso di archiviazione) e il formato del file desiderato (dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)) quando chiami il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Come Salvare un Workbook in Pdf**
Il formato PDF (Portable Document Format) è un tipo di documento creato da Adobe negli anni '90. Lo scopo di questo formato di file era introdurre uno standard per la rappresentazione di documenti e altro materiale di riferimento in un formato indipendente dal software applicativo, hardware e sistema operativo. Il formato PDF può contenere testo, immagini, hyperlink, campi modulo, media ricchi, firme digitali, allegati, metadati, caratteristiche geospaziali e oggetti 3D che possono far parte del documento di origine.

Il seguente codice mostra come salvare un workbook come file PDF con Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Come Salvare un Workbook in Formato Testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo.

Il seguente esempio di codice spiega come salvare un intero workbook in formato testo. Carica il workbook di origine, che può essere qualsiasi file di foglio di calcolo Microsoft Excel o OpenOffice (come XLS, XLSX, XLSM, XLSB, ODS, ecc.) con qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

Puoi modificare lo stesso esempio per salvare il file in CSV. Per impostazione predefinita, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) è la virgola, quindi non specificare un separatore se si salva in formato CSV. Nota: se si utilizza la versione di valutazione e anche se la proprietà [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) è impostata su true, il programma esporta ancora solo un foglio di lavoro.

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

## **Come salvare un file in file di testo con un separatore personalizzato**

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

## **Come salvare un file in uno stream**

Per salvare i file in un flusso, crea un oggetto *MemoryStream* o *FileStream* e salva il file in quell'oggetto stream chiamando il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Specifica il formato del file desiderato usando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) quando chiami il metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Come salvare un file di Excel in file Html e Mht**
Aspose.Cells può semplicemente salvare un file Excel, JSON, CSV o altri file che possono essere caricati da Aspose.Cells come file .html e .mht.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Come salvare un file di Excel in OpenOffice (ODS, SXC, FODS, OTS)**
Possiamo salvare i file nel formato OpenOffice: ODS, SXC, FODS, OTS, ecc.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Come salvare un file di Excel in JSON o XML**

JSON (JavaScript Object Notation) è un formato file standard aperto per la condivisione di dati che utilizza testo leggibile dall'uomo per memorizzare e trasmettere dati. I file JSON sono memorizzati con l'estensione .json. JSON richiede meno formattazione ed è una buona alternativa per XML. JSON deriva da JavaScript, ma è un formato di dati indipendente dal linguaggio. La generazione e l'analisi di JSON sono supportate da molti linguaggi di programmazione moderni. application/json è il tipo di supporto usato per JSON.

Aspose.Cells supporta il salvataggio dei file in JSON o XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **Argomenti avanzati**
- [Regola il livello di compressione del workbook](/cells/it/nodejs-cpp/adjust-workbook-compression-level/)
- [Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet](/cells/it/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Salvataggio del file nell'oggetto di risposta](/cells/it/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
