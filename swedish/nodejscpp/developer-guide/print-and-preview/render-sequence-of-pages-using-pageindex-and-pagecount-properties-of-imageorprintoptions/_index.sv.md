---  
title: Renderingssekvens av sidor med PageIndex och PageCount egenskaper av ImageOrPrintOptions med Node.js via C++  
linktitle: Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions  
type: docs  
weight: 110  
url: /sv/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Lär dig hur man renderar specifika sidor i en Excel fil till bilder med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Du kan rendera en sekvens av sidor i din Excel-fil till bilder genom att använda Aspose.Cells med [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) och [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--) egenskaper. Dessa egenskaper är användbara när det finns många t.ex. tusentals sidor i ditt kalkylblad men du vill rendera endast några av dem. Detta sparar inte bara processningstid utan minskar också minnesanvändningen under rendering.  

## **Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions**  

Följande exempel kod laddar den [provexemplet Excel-fil](55541781.xlsx) och renderar endast sidorna 4, 5, 6 och 7 med hjälp av [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) och [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--) egenskaper. Här är de renderade sidorna som genererats av koden.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Exempelkod**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
