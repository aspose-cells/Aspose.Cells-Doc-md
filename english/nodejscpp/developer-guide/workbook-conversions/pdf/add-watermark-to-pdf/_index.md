---
title: Add Watermark To PDF with Node.js via C++
linktitle: Add Watermark To PDF
type: docs
weight: 9
url: /nodejs-cpp/add-watermark-to-pdf/
description: Learn how to add text and image watermarks to PDF while converting Excel to PDF using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

While converting an Excel file to PDF, you may have requirements to add a watermark to the PDF file. The following examples show how to add text and image watermarks to the PDF while rendering.

## **Add text watermark to PDF**

You can easily add a text watermark to a PDF by specifying the text and the corresponding font. You can also set alignment, offset, rotation, opacity, foreground or background, and scale to the page in [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Prepare a workbook with three pages.
const wb = new AsposeCells.Workbook();
wb.getWorksheets().get(0).getCells().get("A1").putValue("Page1");
let index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page2");
index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page3");
wb.getWorksheets().get(index).getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);

// Create a font for the watermark and specify bold, italic, and color.
const font = new AsposeCells.RenderingFont("Calibri", 68);
font.setItalic(true);
font.setBold(true);
font.setColor(AsposeCells.Color.Blue);

// Create a watermark from text and the specified font.
const watermark = new AsposeCells.RenderingWatermark("Watermark", font);

// Specify horizontal and vertical alignment
watermark.setHAlignment(AsposeCells.TextAlignmentType.Center);
watermark.setVAlignment(AsposeCells.TextAlignmentType.Center);

// Specify rotation
watermark.setRotation(30);

// Specify opacity
watermark.setOpacity(0.6);

// Specify the scale to the page (e.g., 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// Specify watermark for rendering to PDF.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_text_watermark.pdf", options);
```

## **Add image watermark to PDF**

You can add an image watermark to a PDF by specifying the image bytes. You can also set alignment, offset, rotation, opacity, foreground or background, and scale to the page in [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
const fs = require("fs");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Prepare a workbook with three pages.
const wb = new AsposeCells.Workbook();
wb.getWorksheets().get(0).getCells().get("A1").putValue("Page1");
let index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page2");
index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page3");
wb.getWorksheets().get(index).getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);

// Create a watermark from image (you need to prepare image bytes).
const imageBytes = fs.readFileSync(path.join(dataDir, "icon.svg"));
const watermark = new AsposeCells.RenderingWatermark(imageBytes);

// Specify offset for alignment.
watermark.setOffsetX(100);
watermark.setOffsetY(200);

// Specify rotation.
watermark.setRotation(30);

// Specify the watermark as background.
watermark.setIsBackground(true);

// Specify opacity.
watermark.setOpacity(0.6);

// Specify the scale to the page (e.g., 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// Specify watermark for rendering to PDF.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_image_watermark.pdf", options);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
