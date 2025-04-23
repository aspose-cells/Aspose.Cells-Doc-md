---  
title: Renderizza sequenze di pagine usando le proprietà PageIndex e PageCount di ImageOrPrintOptions con Node.js tramite C++  
linktitle: Rendi sequenza di pagine usando le proprietà PageIndex e PageCount di ImageOrPrintOptions  
type: docs  
weight: 110  
url: /it/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Impara come renderizzare pagine specifiche di un file Excel in immagini usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Puoi rendere una sequenza di pagine del tuo file Excel in immagini usando Aspose.Cells con le proprietà [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) e [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Queste proprietà sono utili quando ci sono molte pagine, ad esempio migliaia, nel tuo foglio di lavoro, ma vuoi renderizzarne solo alcune. Questo non solo riduce il tempo di elaborazione, ma anche il consumo di memoria del processo di rendering.  

## **Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**  

Il seguente esempio di codice carica il [file Excel di esempio](55541781.xlsx) e renderizza solo le pagine 4, 5, 6 e 7 utilizzando le proprietà [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) e [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Ecco le pagine renderizzate generate dal codice.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"));
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Specify image or print options
// We want to print pages 4, 5, 6, 7
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageIndex(3);
opts.setPageCount(4);
opts.setImageType(AsposeCells.ImageType.Png);
// Create sheet render object
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);
// Print all the pages as images
for (let i = opts.getPageIndex(); i < sheetRender.getPageCount(); i++) {
sheetRender.toImage(i, path.join(outputDir, `outputImage-${i + 1}.png`));
}
```  

