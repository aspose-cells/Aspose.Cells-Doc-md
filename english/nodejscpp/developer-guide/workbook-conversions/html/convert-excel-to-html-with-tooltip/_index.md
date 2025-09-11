---  
title: Convert Excel to HTML with tooltip using Node.js via C++  
linktitle: Convert Excel to HTML with tooltip  
type: docs  
weight: 200  
url: /nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Learn how to convert Excel files to HTML format with tooltips for complete text display using Aspose.Cells for Node.js via C++.  
---  

## **Convert Excel to HTML with tooltip**

There might be cases where the text is cut off in the generated HTML and you want to display the complete text as a tooltip on the hover event. Aspose.Cells for Node.js via C++ supports this by providing [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) property. Setting the [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) property to **true** will add the complete text as a tooltip in the generated HTML.

The following image shows the tooltip in the generated HTML file.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

The following code sample loads the [source excel file](98107416.xlsx) and generates the [output HTML file](98107417.zip) with the tooltip.

Sample Code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}