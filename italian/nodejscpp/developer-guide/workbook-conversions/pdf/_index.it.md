---
title: Pdf con Node.js via C++
linktitle: Pdf
type: docs
weight: 220
url: /it/nodejs-cpp/convert-excel-to-pdf/
description: Impara come convertire il Workbook Excel in PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione del workbook di Excel in PDF. In questo esempio, vedremo la completa conversione di un workbook di Excel in PDF.
{{% /alert %}}

## **Conversione di un Workbook Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ scrive direttamente le informazioni su API e Numero di Versione nei documenti di output. Per esempio, durante il rendering del Documento in PDF, Aspose.Cells for Node.js via C++ popola il campo **Produttore PDF** con il valore, ad esempio 'Aspose.Cells v23.2'.

Si noti che è possibile modificare queste informazioni nei documenti di output tramite la proprietà [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--).
{{% /alert %}}

### **Conversione Diretta**

Aspose.Cells for Node.js via C++ supporta la conversione di fogli di calcolo in PDF indipendentemente da altri software. Basta salvare un file Excel come PDF usando il metodo [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Il metodo [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) fornisce il membro di enumerazione [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) che converte i file Excel nativi in formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Istituire un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
3. Eseguire qualsiasi lavoro (inserire dati, applicare formattazione, inserire formule, inserire immagini o altri oggetti grafici, ecc.) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiama il metodo [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi selezionare *Pdf* (un valore predefinito) dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) per generare il documento PDF finale.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Conversione Avanzata**

È anche possibile optare per utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) per impostare attributi diversi per la conversione. Impostare diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) consente di esercitare il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output in PDF. 

La proprietà più importante è [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) che consente di impostare il livello di conformità agli standard PDF. Attualmente è possibile salvare in formati PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u. Si noti che con il formato PDF/A, le dimensioni del file di output sono più grandi rispetto a un normale file PDF.

#### **Salvataggio del foglio di lavoro in file PDF/A compilati**

Il frammento di codice fornito di seguito dimostra come utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) per salvare i file Excel in formato PDF/A conforme.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Si noti che la proprietà [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) è stata aggiunta con il rilascio di Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), è possibile ottenere o impostare l'ora di creazione del PDF. Il codice seguente dimostra l'uso della proprietà [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) per impostare l'ora di creazione del file PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), è possibile ottenere o impostare l'opzione [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) del PDF per controllare l'accesso ai contenuti nel PDF convertito.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), è possibile esportare le proprietà personalizzate nel foglio di lavoro di origine nel PDF. L'enumeratore [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) è fornito per specificare il modo in cui vengono esportate le proprietà. Queste proprietà possono essere visualizzate in Adobe Acrobat Reader facendo clic su File e poi sull'opzione proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per testare, e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per l'analisi.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Attributi di Conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cell ha ancora un paio di limitazioni. MapChart non è supportato quando si converte in formato PDF. Inoltre, alcuni oggetti grafici non sono ben supportati.

La tabella che segue elenca tutte le caratteristiche che sono completamente o parzialmente supportate durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo, ma identifica le funzionalità non supportate o parzialmente supportate per la conversione in PDF.

|**Elemento del Documento**|**Attributo**|**Supportato**|**Note**|
| :- | :- | :- | :- |
|Allineamento| |Sì| |
|Impostazioni sfondo| |Sì| |
|Bordo|Colore|Sì| |
|Bordo|Stile di linea|Sì| |
|Bordo|Spessore linea|Sì| |
|Dati della cella| |Sì| |
|Commenti| |Sì| |
|Formattazione condizionale| |Sì| |
|Proprietà del documento| |Sì| |
|Oggetti disegno| |Parzialmente|Effetti ombra e 3-D per gli oggetti di disegno non sono ben supportati; WordArt e SmartArt sono supportati parzialmente.|
|Carattere|Dimensione|Sì| |
|Carattere|Colore|Sì| |
|Carattere|Stile|Sì| |
|Carattere|Sottolineato|Sì| |
|Carattere|Effetti|Sì||
|Immagini| |Sì| |
|Collegamento ipertestuale| |Sì| |
|Grafici| |Parzialmente|MapChart non è supportato.|
|Celle unite| |Sì| |
|Interruzione di pagina| |Sì| |
|Impostazioni pagina|Intestazione/Piè di pagina|Sì| |
|Impostazioni pagina|Margini|Sì| |
|Impostazioni pagina|Orientamento pagina|Sì| |
|Impostazioni pagina|Formato pagina|Sì| |
|Impostazioni pagina|Area di stampa|Sì| |
|Impostazioni pagina|Titoli di stampa|Sì| |
|Impostazioni pagina|Scalatura|Sì| |
|Altezza riga/Larghezza colonna| |Sì| |
|Lingua RTL (da destra a sinistra)| |Sì| |

{{% alert color="primary" %}}
Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.
{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi Segnalibri PDF con Destinazioni con Nome](/cells/it/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare](/cells/it/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Modifica il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF](/cells/it/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Converti file XLSX in formato PDF](/cells/it/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Convertire file Excel in formato PDF compatibile con PDFA-1a](/cells/it/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per Chart Sheet](/cells/it/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di calcolo in una singola pagina PDF](/cells/it/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler](/cells/it/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Ottieni avvisi per la sostituzione del carattere mentre si rende il file Excel](/cells/it/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignora gli errori durante la conversione di Excel in PDF](/cells/it/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione da Excel a PDF](/cells/it/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti durante il salvataggio in PDF](/cells/it/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins durante la conversione di Excel in PDF](/cells/it/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendi una pagina PDF per ogni foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rende i Caratteri Unicode Supplementari nell'output PDF con Aspose.Cells](/cells/it/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ridimensionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ciascun foglio di calcolo in un file PDF separato](/cells/it/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensioni standard o minime](/cells/it/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva fogli specificati in PDF](/cells/it/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Documenti PDF sicuri](/cells/it/nodejs-cpp/secure-pdf-documents/)
- [Specificare come incrociare la stringa nel PDF e nell'immagine di output](/cells/it/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
