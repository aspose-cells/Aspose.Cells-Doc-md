---  
title: Export similar Border Style when Border Style is not supported by Web Browsers with Node.js via C++  
linktitle: Export similar Border Style when Border Style is not supported by Web Browsers  
type: docs  
weight: 70  
url: /nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Learn how to export borders that are not supported by web browsers when converting Excel files to HTML using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Microsoft Excel supports some types of dashed borders which are not supported by Web Browsers. When you convert such an Excel file into HTML using Aspose.Cells for Node.js via C++, such borders are removed. However, Aspose.Cells can also support the display of such borders with the [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) property. Please set its value as **true** and the unsupported borders will also be exported to the HTML file.  

## **Export similar Border Style when Border Style is not supported by Web Browsers**  

The following sample code loads the [sample Excel file](64716806.xlsx) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) property inside the [output HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
