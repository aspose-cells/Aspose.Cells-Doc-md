---
title: Konvertera kalkylblad till bild  Ta bort marginaler runt data med Node.js via C++
linktitle: Konvertera kalkylblad till bild  Ta bort mellanrum runt data
type: docs
weight: 40
url: /sv/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Lär dig hur du konverterar Microsoft Excel kalkylblad till bilder och tar bort marginaler runt data med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I huvudsak vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells gör det möjligt att konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

## **Ta bort mellanrum runt data**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)-API:en konverterar ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidade kalkylblad, osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder funktionen ark-till-bild har den resulterande bilden ett mellanrum, det vill säga en ram, runt den som standard. Du kan ta bort detta genom att ställa in de översta, understa, vänstra och högra sidmarginalerna för källkalkylbladet till 0 och ange [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)-attribut därefter.

Följande kodsippa tar bort mellanrummet runt datan i den resulterande bilden.

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
