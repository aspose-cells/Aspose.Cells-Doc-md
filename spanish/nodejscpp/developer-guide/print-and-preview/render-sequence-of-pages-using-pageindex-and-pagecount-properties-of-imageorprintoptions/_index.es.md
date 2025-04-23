---  
title: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions con Node.js vía C++  
linktitle: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions  
type: docs  
weight: 110  
url: /es/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Aprende cómo renderizar páginas específicas de un archivo de Excel a imágenes usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Puedes renderizar una secuencia de páginas de tu archivo de Excel a imágenes usando Aspose.Cells con las propiedades [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) y [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Estas propiedades son útiles cuando hay muchas, por ejemplo, miles de páginas en tu hoja de cálculo, pero solo quieres renderizar algunas de ellas. Esto no solo ahorra tiempo de procesamiento sino también el consumo de memoria del proceso de renderizado.  

## **Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](55541781.xlsx) y renderiza solo las páginas 4, 5, 6 y 7 usando las propiedades [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) y [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Aquí están las páginas renderizadas generadas por el código.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Código de muestra**  

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

