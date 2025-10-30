---
title: Converti Foglio di lavoro in immagine  Rimuovi spazio bianco attorno ai dati con Node.js tramite C++
linktitle: Converti foglio elettronico in immagine  Rimuovi spazi vuoti intorno ai dati
type: docs
weight: 40
url: /it/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Scopri come convertire fogli di Microsoft Excel in immagini e rimuovere lo spazio bianco attorno ai dati usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A volte è necessario presentare immagini del foglio elettronico in applicazioni o pagine web. Ad esempio, potresti aver bisogno di inserire immagini in un documento di Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, desideri renderizzare un foglio elettronico come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells ti consente di convertire i fogli di lavoro di Microsoft Excel in immagini.

{{% /alert %}}

## **Rimuovi spazi vuoti intorno ai dati**

L'API [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) converte un foglio elettronico in un file immagine con eventuali attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati diversi formati di immagine, come BMP, GIF, JPG, TIFF e EMF.

Quando si utilizza la funzione foglio-in-immagine, l'immagine di output ha spazi vuoti, cioè un bordo, attorno ad essa per impostazione predefinita. È possibile rimuovere questo impostando i margini di impaginazione superiore, inferiore, sinistro e destro del foglio di lavoro di origine a 0 e specificando [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) attributi di conseguenza.

Il seguente frammento di codice rimuove gli spazi vuoti intorno ai dati nell'immagine di output.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
