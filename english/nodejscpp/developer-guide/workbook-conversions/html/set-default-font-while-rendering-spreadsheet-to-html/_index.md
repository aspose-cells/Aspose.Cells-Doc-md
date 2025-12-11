---  
title: Set Default Font while Rendering Spreadsheet to HTML with Node.js via C++  
linktitle: Set Default Font while Rendering Spreadsheet to HTML  
type: docs  
weight: 370  
url: /nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  
Aspose.Cells allows you to set a default font while rendering a spreadsheet to HTML. Please use the [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) for this purpose. This property is useful when some cells in a spreadsheet have invalid or non‑existing fonts; those cells will be rendered using the font specified via the [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) property.  
{{% /alert %}}  

## Set Default Font while Rendering Spreadsheet to HTML  

The following sample code creates a workbook, adds some text to cell **B4** of the first worksheet, and sets its font to an unknown/non‑existing font. It then saves the workbook to HTML using different default font names such as **Courier New**, **Arial**, **Times New Roman**, etc.  

The screenshot shows the effect of setting different default font names via the [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) property.  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

The code generates an output HTML file with **Courier New**, another with **Arial**, and a third with **Times New Roman**.  

## Sample Code  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object and access the first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 to an unknown font.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Save the workbook in HTML format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Save the workbook in HTML format again, this time setting the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Save the workbook in HTML format once more, setting the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
