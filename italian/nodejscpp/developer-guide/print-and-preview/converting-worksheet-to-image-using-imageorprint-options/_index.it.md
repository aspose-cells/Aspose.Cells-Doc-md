---  
title: Conversione di Foglio di Lavoro in Immagine utilizzando Opzioni ImageOrPrint con Node.js tramite C++  
linktitle: Conversone del Foglio di Lavoro in Immagine utilizzando le Opzioni Immagine o Stampa  
type: docs  
weight: 90  
url: /it/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Scopri come convertire un foglio di lavoro in un file immagine e applicare varie opzioni di immagine e stampa usando Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
Questo documento è progettato per fornire una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, come risoluzione, compressione TIFF, formato immagine e qualità della pagina.  
{{% /alert %}}  

## **Salvataggio Fogli di lavoro in Immagini - Diverse Approcci**  

A volte potresti aver bisogno di presentare i tuoi fogli di lavoro come rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint, o utilizzarle in qualche altro scenario. Semplicemente desideri un foglio di lavoro rappresentato come un'immagine in modo da poterlo utilizzare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta impostare diverse opzioni come formato immagine, risoluzione (sia verticale che orizzontale), qualità dell'immagine e altre opzioni di immagine e stampa.  

Potresti provare l'Automazione Office ma l'automazione Office ha i suoi svantaggi. Ci sono diverse ragioni e problemi coinvolti: ad esempio, sicurezza, stabilità, scalabilità e velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, con la principale che Microsoft stessa raccomanda fortemente di non utilizzare l'automazione Office da soluzioni software.  

Questo articolo mostra come creare un'applicazione console in Visual Studio .NET, eseguire la conversione di un foglio di lavoro in un'immagine utilizzando diverse opzioni di immagine e stampa con poche e semplici righe di codice utilizzando l'API Aspose.Cells.  

La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) rappresenta un foglio di lavoro per renderizzare immagini, dispone di un metodo [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) sovraccarico che può convertire direttamente un foglio di lavoro in uno o più file immagine specificati con i tuoi attributi o opzioni desiderate. Può restituire un oggetto su cui puoi salvare un file immagine su disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPEG, TIFF, EMF e altri.  

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint.**  

### **Creazione di un libro di lavoro modello in Microsoft Excel**  

Ho creato un nuovo libro di lavoro in MS Excel e aggiunto alcuni dati nel primo foglio di lavoro. Ora, convertirò il foglio di lavoro del file modello "Foglio1" in un file immagine "FoglioImmagine.tiff" e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, compressione Tiff, ecc.  

### **Scarica e installa Aspose.Cells**  

Prima, devi [scaricare](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Installa sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.  

### **Crea un Progetto**  

Avvia il tuo ambiente di sviluppo preferito (ad esempio, Visual Studio). Crea una nuova applicazione console.  

### **Aggiungi Riferimenti**  

Questo progetto utilizzerà Aspose.Cells. Quindi, devi aggiungere un riferimento al componente Aspose.Cells nel tuo progetto. Per esempio, aggiungi un riferimento a ….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **Convertire un foglio di lavoro in un file immagine**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Opzioni di conversione**  

È possibile salvare pagine specifiche in immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in un libro di lavoro in immagini JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Conversione dell'immagine utilizzando WorkbookRender**  

Un'immagine TIFF può contenere più di un frame. È possibile salvare l'intero workbook in un’unica immagine TIFF con più frame o pagine:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
