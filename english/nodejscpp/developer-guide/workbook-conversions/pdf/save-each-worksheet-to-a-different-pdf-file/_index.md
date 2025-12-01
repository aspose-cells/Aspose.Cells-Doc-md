---  
title: Save Each Worksheet to a Different PDF File with Node.js via C++  
linktitle: Save Each Worksheet to a Different PDF File  
type: docs  
weight: 130  
url: /nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Aspose.Cells supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for Node.js via C++ can work independently to convert a spreadsheet to PDF, and you do not need to use Aspose.PDF for Node.js via C++ for the conversion. The conversion does not require the software to create or use any temporary files as the whole process can be done in memory.  
{{% /alert %}}  

## **Save Each Worksheet to a Different PDF File**  
If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to set one sheet index to [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) option at a time to render to PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.  
{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
