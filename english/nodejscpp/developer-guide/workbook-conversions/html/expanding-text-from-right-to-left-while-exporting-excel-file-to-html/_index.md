---  
title: Expanding text from right to left while exporting Excel file to HTML with Node.js via C++  
linktitle: Expanding text from right to left while exporting Excel file to HTML  
type: docs  
weight: 60  
url: /nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Aspose.Cells now supports expanding text from right to left while exporting Excel file to HTML. This feature has been implemented since v8.9.0.0. If your source Excel file contains any text that expands from right to left, Aspose.Cells will export it to HTML correctly.  

{{% /alert %}}  
## **Expanding text from right to left while exporting Excel file to HTML**  
The following sample code converts the [sample Excel file](5115502.xlsx) into HTML. This screenshot shows how the sample Excel file looks in Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

This screenshot shows the [output HTML generated with an older version](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

This screenshot shows the [output HTML generated with a newer version](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

As you can see in the screenshots, the newer version expands right-aligned text to the left correctly, just like Microsoft Excel.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source Excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in HTML format
wb.save(
    path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`),
    AsposeCells.SaveFormat.Html
);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
