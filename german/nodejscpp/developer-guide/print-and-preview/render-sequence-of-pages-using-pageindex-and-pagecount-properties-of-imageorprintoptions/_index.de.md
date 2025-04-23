---  
title: Sequentielle Seiten mit PageIndex und PageCount Eigenschaften von ImageOrPrintOptions mit Node.js via C++ rendern  
linktitle: Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions  
type: docs  
weight: 110  
url: /de/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Erfahren Sie, wie Sie bestimmte Seiten einer Excel Datei in Bilder mit Aspose.Cells for Node.js via C++ rendern.  
---  

## **Mögliche Verwendungsszenarien**  

Sie können eine Sequenz von Seiten Ihrer Excel-Datei in Bilder rendern, indem Sie Aspose.Cells mit [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--)- und [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--)-Eigenschaften verwenden. Diese Eigenschaften sind nützlich, wenn es beispielsweise Tausende von Seiten in Ihrem Arbeitsblatt gibt, aber Sie nur einige davon rendern möchten. Dies spart nicht nur die Verarbeitungszeit, sondern auch den Speicherverbrauch des Rendering-Prozesses.  

## **Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](55541781.xlsx) und rendert nur die Seiten 4, 5, 6 und 7 mithilfe der Eigenschaften [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) und [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Hier sind die vom Code generierten gerenderten Seiten.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Beispielcode**  

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

