---
title: Fit All Worksheet Columns on Single PDF Page with Node.js via C++
linktitle: Fit All Worksheet Columns on Single PDF Page
type: docs
weight: 160
url: /nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you want to generate a PDF file that fits all of a worksheet's columns onto one page. The [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) property provides this feature in a very easy-to-use manner. Complex calculations such as the height and width of the output PDF are handled internally and are based on the data in the worksheet.

{{% /alert %}}

## **Fit Worksheet Columns on Single PDF Page**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) ensures that all columns in a worksheet are rendered to a single PDF page, although rows may expand to several pages depending on the data in the worksheet.

The sample code below shows how to use the [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) property to render a large worksheet of 100 columns.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

When a given worksheet has many columns, the rendered PDF file may display the content at a very small size. It remains readable when scaled up in a viewing application such as Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}} {{< app/cells/assistant language="nodejs-cpp" >}}
