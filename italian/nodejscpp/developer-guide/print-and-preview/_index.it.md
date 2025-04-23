---  
title: Anteprima del workbook con Node.js tramite C++  
linktitle: Anteprima del workbook 
type: docs  
weight: 70  
url: /it/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells supporta la stampa e l anteprima di file Excel senza installazione di Microsoft Excel usando Node.js tramite C++.  
---  

## **Anteprima di stampa**  

Potrebbero esserci casi in cui file Excel con milioni di pagine devono essere convertiti in PDF o immagini. L'elaborazione di tali file richiederà molto tempo e risorse. In questi casi, la funzione di anteprima di stampa del Workbook e del Worksheet potrebbe essere utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e decidere se convertire o meno il file. Questo articolo si concentra sull'uso delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) per scoprire il numero totale di pagine.  

Aspose.Cells fornisce la funzione di anteprima di stampa. A tal fine, l'API fornisce le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/). Per creare l'anteprima di stampa dell'intero workbook, crea un'istanza della classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) passando gli oggetti [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) al costruttore. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) fornisce un metodo [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) che restituisce il numero di pagine nell'anteprima generata. Come la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) viene usata per generare un'anteprima di stampa di un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, crea un'istanza della classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) passando gli oggetti [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) al costruttore. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) fornisce anche un metodo [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) che restituisce il numero di pagine dell'anteprima generata.  

Il seguente frammento di codice dimostra l'uso di entrambe le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) usando il [file excel di esempio](94896177.xlsx).  

### **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Quello che segue è l'output generato eseguendo il codice sopra.  

### **Output della console**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Argomenti avanzati**  
- [Configurare i font per la resa dei fogli di calcolo](/cells/it/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertire il foglio di lavoro in un'immagine - Rimuovere gli spazi vuoti intorno ai dati](/cells/it/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Convertire il foglio di lavoro in un'immagine e Foglio di lavoro in un'immagine per pagina](/cells/it/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Convertire il foglio di lavoro in un'immagine utilizzando le opzioni ImageOrPrint](/cells/it/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Esportare un intervallo di celle in un foglio di lavoro in un'immagine](/cells/it/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Estrarre immagini dai fogli di lavoro utilizzando ImageOrPrintOptions](/cells/it/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generare l'anteprima del foglio di lavoro](/cells/it/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Output Pagina Bianca quando non c'è Nulla da Stampare](/cells/it/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Impostazioni di layout pagina e stampa](/cells/it/nodejs-cpp/page-setup-and-printing-options/)  
- [Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Renderizzare il foglio di lavoro al contesto grafico](/cells/it/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Specificare un insieme individuale o privato di caratteri per la rappresentazione del foglio di lavoro](/cells/it/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

