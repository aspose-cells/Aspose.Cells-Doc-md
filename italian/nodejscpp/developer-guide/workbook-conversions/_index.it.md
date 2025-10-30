---  
title: Converti Excel in Pdf, immagine e altri formati  
linktitle: Conversione di cartelle di lavoro  
type: docs  
weight: 65  
url: /it/nodejs-cpp/convert-workbook-to-different-formats/  
description: Converti file Excel in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML e altro ancora usando Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporta la conversione tra molti formati. Tecnicamente, la conversione significa caricare una cartella di lavoro in un formato di file e salvarla in un altro.  
{{% /alert %}}  

## **Converti il foglio di lavoro di Excel in PDF**  
I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.  

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Converti cartella di lavoro Excel in JPG**  
Aspose.Cells supporta la conversione di file Excel in JPG. L'esempio di codice sotto mostra come salvare un workbook come JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Converti cartella di lavoro Excel in immagine**  
Aspose.Cells supporta la conversione di file Excel in immagini. L'esempio di codice sottostante mostra come salvare un workbook come immagini.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Conversione della cartella di lavoro Excel in XPS**  
Il formato del documento XPS consiste in markup XML strutturato che definisce la disposizione di un documento e l'aspetto visuale di ogni pagina, insieme alle regole di rendering per distribuire, archiviare, rendere, elaborare e stampare documenti.  

Il linguaggio di markup per XPS è un sottoinsieme di XAML che consente di incorporare elementi grafici vettoriali nei documenti, utilizzando XAML per contrassegnare i primitivi della Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altri primitivi geometrici.  

Un file XPS è, in realtà, un archivio ZIP unicode utilizzando le Convenzioni per l'Imballaggio Aperto, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, font integrati, immagini raster, grafica vettoriale 2D, nonché le informazioni sulla gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un'applicazione che supporta file ZIP.  

A partire da Aspose.Cells 6.0.0, è supportata la conversione di Microsoft Excel in XPS.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Converti Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells supporta la conversione di file Excel in Ods, Sxc e Fods. L'esempio di codice sotto mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Conversione della cartella di lavoro Excel in file MHTML**  
MHTML combina HTML normale con risorse esterne (cioè contenuti che di solito sono collegati, come immagini, animazioni, audio, e così via) in un unico file. Sono utilizzati per le email con l'estensione del file .mht.  

Aspose.Cells supporta la lettura e la scrittura dei file MHTML.  

L'esempio di codice sotto mostra come salvare un workbook come file MHTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Conversione di un Workbook Excel in HTML**  
L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.  

L'esempio di codice sotto mostra come salvare un workbook come file HTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Impostazione delle Preferenze Immagine per HTML**  
A partire dalla versione 8.0.2, Aspose.Cells ha esposto [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) per la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), consentendo agli sviluppatori di specificare le preferenze di immagine durante il salvataggio dei fogli di calcolo in formato HTML.  

Di seguito sono riportati i dettagli di alcune delle impostazioni delle immagini che possono essere applicate,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Specifica il tipo di immagine. Si noti che tutte le forme, inclusi grafici, vengono rappresentati come immagini nell'HTML di output.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Specifica la qualità dell'immagine tra 0 e 100, quando [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) è specificato come Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): Ottiene o imposta il tipo di compressione per le immagini quando [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) è specificato come Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.  

## **Converti Workbook Excel in Markdown**  
L'API Aspose.Cells offre supporto per esportare fogli di calcolo in formato Markdown. Per esportare il foglio attivo in Markdown, passa [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Puoi anche usare la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio in Markdown.  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in Markdown usando il membro di enumerazione [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Si prega di consultare il [file Markdown di output](md_sample.txt) generato dal codice per riferimento.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Converti Workbook Excel in JSON**  
Aspose.Cells supporta la conversione di un workbook in file Json (JavaScript Object Notation).  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in Json usando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Si prega di consultare il codice per convertire il [file sorgente](Book1.xlsx) nel [file Json di output](Book1.Json) generato dal codice di riferimento.  

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

## **Converti Excel in XML**  
Aspose.Cells supporta la conversione di un workbook in Excel 2003 Spreadsheet XML e dati XML semplici.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Converti Workbook di Excel in TIFF**  
Aspose.Cells supporta la conversione di un workbook in file TIFF.  

Il frammento di codice seguente mostra come convertire Excel in TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Converti Workbook di Excel in DOCX**  
L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato DOCX. Per esportare il workbook in DOCX, passa [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Puoi anche usare la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) per specificare impostazioni aggiuntive per l'esportazione in DOCX.  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in DOCX usando il membro di enumerazione [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Si prega di consultare il [file DOCX di output](Book1.docx) generato dal codice.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Converti Workbook di Excel in PPTX**  
L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato PPTX. Per esportare il workbook in PPTX, passa [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Puoi anche usare la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) per specificare impostazioni aggiuntive per l'esportazione in PPTX.  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in PPTX usando il membro di enumerazione [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Si prega di consultare il [file PPTX di output](Book1.pptx) generato dal codice.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Converti cartella di lavoro Excel in EPUB**  
L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato EPUB. Per esportare il workbook in EPUB, passa [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Puoi anche usare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) per specificare impostazioni aggiuntive per l'esportazione in Epub.  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in EPUB usando il membro di enumerazione [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Converti cartella di lavoro Excel in AZW3**  
L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato AZW3. Per esportare il workbook in AZW3, passa [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Puoi anche usare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) per specificare impostazioni aggiuntive per l'esportazione in AZW3.  

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in AZW3 usando il membro di enumerazione [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Argomenti avanzati**  
- [Converti la revisione di XLSB in XLSM](/cells/it/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/it/nodejs-cpp/convert-excel-to-html/)  
- [Immagine](/cells/it/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/it/nodejs-cpp/convert-workbook-to-json/)  
- [Converti il workbook Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc).](/cells/it/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/it/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Converti Excel in CSV, TSV e Txt](/cells/it/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Monitorare il progresso della conversione dei documenti](/cells/it/nodejs-cpp/track-document-conversion-progress/)  
- [Converti CSV, TSV e TXT in Excel](/cells/it/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
