---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML with Node.js via C++
linktitle: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel, but when you change the cross type to [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), it hides all the strings on the right side of the cell that are overlaid or overlapping with cell strings.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.setHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#setHtmlCrossStringType--) to [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). The screenshot explains how [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) affects the output HTML compared with the default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to HTML
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
