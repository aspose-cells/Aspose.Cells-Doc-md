---  
title: Bereich von Zellen in einem Arbeitsblatt mit Node.js via C++ in ein Bild exportieren  
linktitle: Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren  
type: docs  
weight: 60  
url: /de/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Mögliche Verwendungsszenarien**  

Sie können ein Arbeitsblatt mit Aspose.Cells for Node.js via C++ in ein Bild umwandeln. Manchmal ist es jedoch notwendig, nur einen Zellbereich in einem Arbeitsblatt in ein Bild zu exportieren. Dieser Artikel erklärt, wie man das erreicht.  

## **Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren**  

Um einen Bereich zu erfassen, setzen Sie den Druckbereich auf den gewünschten Bereich und stellen Sie alle Ränder auf 0. Setzen Sie außerdem [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) auf **true**. Der folgende Code erstellt ein Bild des Bereichs D8:G16. Unten ist ein Screenshot der [Beispieldatei Excel](47153160.xlsx), die im Code verwendet wird. Sie können den Code mit jeder Excel-Datei testen.  

## **Screenshot der Beispiels-Excel-Datei und des exportierten Bilds**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Die Ausführung des Codes erstellt lediglich ein Bild des Bereichs D8:G16.  

**![todo:image_alt_text](Output-Image.png)**  

## **Beispielcode**  

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

