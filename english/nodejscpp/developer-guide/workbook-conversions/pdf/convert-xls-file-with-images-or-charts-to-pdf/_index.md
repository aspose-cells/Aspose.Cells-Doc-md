---
title: Convert XLS File with Images or Charts to PDF with Node.js via C++
linktitle: Convert XLS File with Images or Charts to PDF
type: docs
weight: 50
url: /nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Node.js via C++ can work independently to convert a spreadsheet to PDF: Aspose.PDF for Node.js via C++ is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% /alert %}} 
## **Sample Code**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
