---
title: Render Worksheet to Graphic Context with Node.js via C++
linktitle: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /nodejs-cpp/render-worksheet-to-graphic-context/
description: Learn how to render a worksheet to graphic context using Aspose.Cells for Node.js via C++. This includes rendering to image files, screens, and printers.
---

{{% alert color="primary" %}}

Aspose.Cells can now render worksheets to graphic context. Graphic context can be anything like an image file, screen, or printer, etc. Please use one of the following two methods to render a worksheet to graphic context.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

The following code illustrates how to use Aspose.Cells to render a worksheet to graphic context. Once you execute the code, it will print the entire worksheet and fill the leftover empty space with blue color in the graphic context and save the image as **OutputImage_out_.png** file. You can use any source Excel file to try this code. Please also read the comments inside the code for better understanding.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
