---  
title: Esporta l intervallo di celle di un foglio di lavoro in immagine con Node.js tramite C++  
linktitle: Esporta un intervallo di celle in un foglio di lavoro in un immagine  
type: docs  
weight: 60  
url: /it/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Possibili Scenari di Utilizzo**  

Puoi creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells for Node.js via C++. Tuttavia, a volte è necessario esportare solo un intervallo di celle in un'immagine. Questo articolo spiega come realizzarlo.  

## **Esportare un intervallo di celle in un foglio di lavoro in un'immagine**  

Per catturare un'immagine di un intervallo, imposta l'area di stampa sull'intervallo desiderato e poi imposta tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) su **true**. Il seguente codice prende un'immagine dell'intervallo D8:G16. Di seguito uno screenshot del [file Excel di esempio](47153160.xlsx) usato nel codice. Puoi provare il codice con qualsiasi file Excel.  

## **Screenshot del file di Excel di esempio e la sua immagine esportata**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Eseguendo il codice viene creata un'immagine dell'intervallo D8:G16 soltanto.  

**![todo:image_alt_text](Output-Image.png)**  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
