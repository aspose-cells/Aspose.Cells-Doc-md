---  
title: Bild med Node.js via C++  
linktitle: Bild  
type: docs  
weight: 300  
url: /sv/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.  
{{% /alert %}}  

## Konvertering av arbetsbok till TIFF  

En Excel-fil kan innehålla flera blad med flera sidor. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) gör det möjligt att konvertera Excel till TIFF med flera sidor. Du kan också styra flera alternativ för TIFF, som [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Upplösning ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

Följande kodsnutt visar hur man konverterar Excel till TIFF med flera sidor. Den [källa Excel-filen](workbook-to-tiff-with-mulitiple-pages.xlsx) och [genererade TIFF-bilden](workbook-to-tiff-with-mulitiple-pages.tiff) är bifogade för din referens.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Konvertera Kalkylblad till Bild**  

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.  

Som utvecklare kan det hända att du behöver presentera kalkylblad som bilder. Till exempel kan det hända att du behöver använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Med andra ord vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

Klassen [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) representerar ett arbetsblad som ska renderas som bilder. Den har en överlagrad metod, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), som kan konvertera ett arbetsblad till bildfil(er) med olika attribut eller alternativ. Den returnerar ett Buffer-objekt och du kan spara en bildfil till disk eller ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.  

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
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
För närvarande stöder inte API:et för att konvertera kalkylblad till bilder 3D-bubble-diagram.  
{{% /alert %}}  

## **Konvertera Kalkylblad till SVG**  

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.  

Aspose.Cells for Node.js via C++ har kunnat konvertera arbetsblad till SVG-bild sedan version 7.1.0. Följande kodsnutt visar hur man konverterar ett arbetsblad i en Excel-fil till en SVG-bildfil.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Fortsatta ämnen**  
- [Konvertera ett Excel-diagram till bild](/cells/sv/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Konvertera diagram till bild i SVG-format](/cells/sv/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Spåra konverteringsframsteg för Excel till TIFF](/cells/sv/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

