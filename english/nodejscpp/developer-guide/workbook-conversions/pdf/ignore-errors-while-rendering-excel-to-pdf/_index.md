---  
title: Ignore Errors while Rendering Excel to PDF with Node.js via C++  
linktitle: Ignore Errors while Rendering Excel to PDF  
type: docs  
weight: 80  
url: /nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Learn how to ignore errors during the conversion of Excel files to PDF using Aspose.Cells for Node.js via C++.  
---  
  
## **Possible Usage Scenarios**  
  
Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process by using the [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) property. This way, the conversion process will complete smoothly without throwing any error or exception but the loss of data may occur. Therefore, please use this property only if the loss of data is not critical for you.  
  
## **Ignore Errors while Rendering Excel to PDF**  
  
The following code loads the [sample Excel file](55541778.xlsx) but the sample Excel file is erroneous and throws an error during [conversion to PDF](55541779.pdf) in 17.11 but since we are using [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) property, it does not throw an error. However, one *rounded red arrow like shape* as shown in this screenshot is lost.  
  
![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  
  
## **Sample Code**  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  
  