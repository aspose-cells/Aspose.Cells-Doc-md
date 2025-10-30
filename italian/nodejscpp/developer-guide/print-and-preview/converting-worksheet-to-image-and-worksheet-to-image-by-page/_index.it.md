---  
title: Conversione di Foglio di lavoro in immagine e in immagini per pagina con Node.js tramite C++  
linktitle: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina  
type: docs  
weight: 80  
url: /it/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e anche come gestire più pagine di un foglio di lavoro convertendole in immagini separate.  

A volte potresti dover presentare i fogli elettronici come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In sostanza, desideri rendere il foglio elettronico come un'immagine. Aspose.Cells supporta la conversione dei fogli in file Microsoft Excel in immagini. Inoltre, Aspose.Cells supporta la conversione di un libro di lavoro in più file immagine, uno per pagina.  

Potresti usare l'automazione di Office per ottenere questo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In sintesi, ci sono molte ragioni, ma la principale è che Microsoft stessa sconsiglia fortemente l'automazione di Office.  
{{% /alert %}}  

## **Utilizzando Aspose.Cells for Node.js via C++ per Convertire Foglio di lavoro in File immagine**  

Questo articolo mostra come creare un'applicazione console, convertire un foglio di lavoro in un'immagine e trasformare un foglio di lavoro in una singola immagine per ogni foglio con poche linee di codice semplici utilizzando l'API di Aspose.Cells.  

Hai bisogno di importare diverse classi di valore correlate alle funzionalità di rendering nel tuo programma o progetto, come [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/), e così via. La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) rappresenta un foglio di lavoro per rendere immagini per il foglio di lavoro e ha un metodo sovraccarico [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) che può convertire un foglio di lavoro in file immagine direttamente con qualsiasi attributo o opzione impostata. Può restituire un oggetto immagine e puoi salvare un file immagine su disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF e altri.  

Questo articolo spiega come:  

- Convertire un foglio di lavoro in un'immagine  
- Convertire ogni pagina in un foglio di lavoro in un'immagine  

Questo compito mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro in un file di immagine.  

### **Progetto di installazione**  

1. Prima, [scarica Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installalo sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità valutazione. La modalità valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti. Ora avvia il tuo ambiente di sviluppo e crea una nuova applicazione console. Questo esempio utilizza un'applicazione console Node.js, ma puoi usare qualsiasi configurazione che si integri con Node.js. Aggiungi un riferimento a Aspose.Cells nel progetto creato.  

### **Converti Foglio di Lavoro in File Immagine**  

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello chiamato Sheet1 in un file immagine chiamato SheetImage.jpg.  

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in **Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Utilizzo di Aspose.Cells for Node.js via C++ per Convertire un Foglio di Lavoro in File Immagine per Pagina**  

Questo esempio mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro che ha diverse pagine in un file immagine per pagina.  

### **Convertire Foglio di Lavoro in Immagine per Pagina**  

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook2.xlsx** (1 foglio di lavoro).  

Ora, converti il foglio di lavoro del file modello in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire il compito di copia, salterò quei passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.  

Di seguito è riportato il codice utilizzato dalla componente per completare il compito. Converte Sheet1 in Testbook2.xlsx in file immagine per pagina.  

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
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
