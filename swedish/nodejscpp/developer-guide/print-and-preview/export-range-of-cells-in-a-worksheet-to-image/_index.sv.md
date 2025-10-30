---  
title: Exportera cellområde i ett arbetsblad till bild med Node.js via C++  
linktitle: Exportera område av celler i en arbetsbok till bild  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Möjliga användningsscenario**  

Du kan skapa en bild av ett arbetsblad med Aspose.Cells for Node.js via C++. Men ibland behöver du bara exportera ett cellområde i ett arbetsblad till en bild. Denna artikel förklarar hur man gör detta.  

## **Exportera område av celler i en arbetsbok till bild**  

För att ta en bild av ett område, ställ in utskriftsområdet till önskat område och ställ därefter alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) till **true**. Följande kod tar en bild av området D8:G16. Nedan är en skärmdump av [exempel-Excel filen](47153160.xlsx) som används i koden. Du kan prova koden med valfri Excel-fil.  

## **Skärmbild av exempelfil i Excel och dess exporterade bild**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Genom att köra koden skapas en bild av området D8:G16 endast.  

**![todo:image_alt_text](Output-Image.png)**  

## **Exempelkod**  

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
