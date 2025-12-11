---  
title: Export print area range to HTML with Node.js via C++  
linktitle: Export print area range to HTML  
type: docs  
weight: 60  
url: /nodejs-cpp/export-print-area-range-to/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**

This is a common scenario where we need to export only the print area, i.e., a selected range of cells, instead of the entire sheet to HTML. This feature is already available for PDF rendering; however, now you can perform this task for HTML as well. First, set the print area in the page‑setup object of the worksheet. Later, use the [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) flag to export the selected range only.

## Sample Code

The following sample code loads a workbook and then exports the print area to HTML. A sample file for testing this feature can be downloaded from the link below:

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
