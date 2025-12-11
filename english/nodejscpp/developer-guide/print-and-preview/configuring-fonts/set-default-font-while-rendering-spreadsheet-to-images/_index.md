---
title: Set Default Font while rendering a spreadsheet to images with Node.js via C++
linktitle: Set Default Font while rendering spreadsheet to images
type: docs
weight: 360
url: /nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Learn how to set the default font while rendering spreadsheets to images using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Please use the [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property to set the default font while rendering spreadsheets to images. This property will only be effective when the default font of the workbook cannot render your characters. The default font specified with [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property is used for all those cells which have invalid or non‑existent fonts.

{{% /alert %}}

## Set Default Font while rendering a spreadsheet to images

The following sample code creates a workbook, adds some text in cell A4 of the first worksheet, and sets its font to an invalid or non‑existent font. Then, it takes two images of the worksheet. The first image is taken by setting the [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property to *Courier New* and the second image is taken by setting the [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property to *Times New Roman*.

This is the output image after setting the [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property to *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

This is the output image after setting the [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property to *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Sample Code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 to an unknown font.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set the first column's width and the fourth row's height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create ImageOrPrintOptions.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

 // Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
