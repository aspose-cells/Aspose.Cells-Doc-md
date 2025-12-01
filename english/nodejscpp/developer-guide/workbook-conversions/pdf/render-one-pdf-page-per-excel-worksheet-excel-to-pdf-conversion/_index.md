---  
title: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion with Node.js via C++  
linktitle: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion  
type: docs  
weight: 100  
url: /nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

When working with large Microsoft Excel files (for example a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

If the [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) option is set to **true**, all the sheet content will be rendered to one PDF page.  

{{% /alert %}} {{% alert color="primary" %}}  

If your spreadsheet contains formulas, it is best to call [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF. This ensures that the formula dependent values are recalculated, and the correct values are rendered in the PDF.  

{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
