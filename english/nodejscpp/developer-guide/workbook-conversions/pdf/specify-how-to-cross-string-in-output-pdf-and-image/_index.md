---  
title: Specify how to cross string in output PDF and image with Node.js via C++  
linktitle: Specify how to cross string in output PDF and image  
type: docs  
weight: 120  
url: /nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Learn to control text overflow in output PDF/Image by specifying the cross type using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**

When a cell contains text or a string but it is larger than the width of the cell, then the string overflows if the next cell in the next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross type using the [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) enumeration. It has the following values:

- **TextCrossType.Default**: Display text like MS Excel which depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

- **TextCrossType.CrossKeep**: Display the string like MS Excel exporting PDF/Image.

- **TextCrossType.CrossOverride**: Display all the text by crossing other cells and override the text of crossed cells.

- **TextCrossType.StrictInCell**: Only display the string within the width of the cell.

## **Specify how to cross string in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Sample Code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}