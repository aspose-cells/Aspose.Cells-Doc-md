---  
title: Immagine con Node.js via C++  
linktitle: Immagine  
type: docs  
weight: 300  
url: /it/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells ti consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in formati diversi.  
{{% /alert %}}  

## Conversione del Workbook in TIFF  

Un file Excel può contenere più fogli con più pagine. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) ti permette di convertire Excel in TIFF con più pagine. Inoltre, puoi controllare molte opzioni per TIFF, come [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Risoluzione ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

Il seguente snippet di codice mostra come convertire Excel in TIFF con pagine multiple. Il [file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) e l'[immagine TIFF generata](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per il tuo riferimento.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Conversione del foglio di lavoro in immagine**  

I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.  

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di utilizzare un'immagine di un foglio di lavoro in un'applicazione o una pagina web. Potresti voler inserire un'immagine in un documento di Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, desideri un foglio di lavoro reso come immagine in modo che tu possa usarlo altrove.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) rappresenta un foglio di lavoro da rendere come immagini. Ha un metodo sovraccarico, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), che può convertire un foglio di lavoro in uno o più file immagine con attributi o opzioni diversi. Restituisce un oggetto Buffer e puoi salvare un file immagine su disco o streammarlo. Sono supportati diversi formati immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
Attualmente, l'API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.  
{{% /alert %}}  

## **Conversione del foglio di lavoro in SVG**  

SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.  

Aspose.Cells for Node.js via C++ è stato in grado di convertire i fogli di lavoro in immagini SVG dalla versione 7.1.0. Il seguente esempio mostra come convertire un foglio di lavoro di un file Excel in un’immagine SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Argomenti avanzati**  
- [Converti un Grafico Excel in Immagine](/cells/it/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Conversione del grafico in Immagine in formato SVG](/cells/it/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Monitora il progresso della conversione di Excel in TIFF](/cells/it/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

