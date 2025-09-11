---  
title: Exclude Unused Styles during Excel to HTML conversion with Node.js via C++  
linktitle: Exclude Unused Styles during Excel to HTML conversion  
type: docs  
weight: 30  
url: /nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Learn how to exclude unused styles when converting Excel to HTML using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  

Microsoft Excel files may contain many unused styles. When you export the Excel file to HTML format, these unused styles are also exported. This can increase the size of the HTML. You can exclude the unused styles during the conversion of Excel files to HTML using the [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) property. When you set it **true**, all unused styles are excluded from the output HTML. The following screenshot displays a sample unused style inside the output HTML.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Exclude Unused Styles during Excel to HTML conversion**  

The following sample code creates a workbook and also creates an unused named style. Since the [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) is set to **true**, this unused named style will not be exported to [output HTML](61767778.zip). But if you set it to **false**, then this unused style will be present inside the output HTML which you can then see in HTML markup as shown in the above screenshot.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}