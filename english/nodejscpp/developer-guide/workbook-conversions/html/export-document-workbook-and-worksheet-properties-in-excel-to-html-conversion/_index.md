---  
title: Export Document Workbook and Worksheet Properties in Excel to HTML conversion with Node.js via C++  
linktitle: Export Document Workbook and Worksheet Properties in Excel to HTML conversion  
type: docs  
weight: 50  
url: /nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Learn how to export Document, Workbook, and Worksheet properties in Excel to HTML using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

When a Microsoft Excel file is exported to HTML using Microsoft Excel or Aspose.Cells for Node.js via C++, it also exports various types of Document, Workbook, and Worksheet properties as shown in the following screenshot. You can avoid exporting these properties by setting the [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) and [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) as **false**. The default value of these properties is **true**. The following screenshot shows how these properties look in the exported HTML.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Export Document, Workbook and Worksheet Properties in Excel to HTML conversion**  

The following sample code loads the [sample Excel file](61767776.xlsx) and converts it to HTML without exporting the Document, Workbook, and Worksheet properties in the [output HTML](61767779.zip).  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export the document, workbook, and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
