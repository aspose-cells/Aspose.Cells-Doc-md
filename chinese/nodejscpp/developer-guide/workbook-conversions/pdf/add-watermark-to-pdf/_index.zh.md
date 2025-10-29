---
title: 使用Node.js via C++向PDF添加水印
linktitle: 向PDF添加水印
type: docs
weight: 9
url: /zh/nodejs-cpp/add-watermark-to-pdf/
description: 学习如何在将Excel转换为PDF时，向PDF添加文本和图像水印，使用Aspose.Cells for Node.js via C++。
---

在将Excel文件转换为PDF的同时，可能需要添加水印。以下示例演示如何添加文本和图像水印。

## **向PDF添加文本水印**

只需指定文本和相应的字体，就可以轻松向PDF添加文本水印。也可以设置对齐、偏移、旋转、不透明度、前景/背景和比例到页面，详见 [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/)。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// prepare a workbook with 3 pages.
const wb = new AsposeCells.Workbook();
wb.getWorksheets().get(0).getCells().get("A1").putValue("Page1");
let index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page2");
index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page3");
wb.getWorksheets().get(index).getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);

// create a font for watermark, and specify bold, italic, color.
const font = new AsposeCells.RenderingFont("Calibri", 68);
font.setItalic(true);
font.setBold(true);
font.setColor(AsposeCells.Color.Blue);

// create a watermark from text and the specified font.
const watermark = new AsposeCells.RenderingWatermark("Watermark", font);

// specify horizontal and vertical alignment
watermark.setHAlignment(AsposeCells.TextAlignmentType.Center);
watermark.setVAlignment(AsposeCells.TextAlignmentType.Center);

// specify rotation
watermark.setRotation(30);

// specify opacity
watermark.setOpacity(0.6);

// specify the scale to page(e.g. 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// specify watermark for rendering to pdf.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_text_watermark.pdf", options);
```

## **向PDF添加图像水印**

只需指定图像字节，就可以向PDF添加图像水印。也可以设置对齐、偏移、旋转、不透明度、前景/背景和比例到页面，详见 [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/)。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
const fs = require("fs");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Prepare a workbook with 3 pages.
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

// Specify offset to alignment.
watermark.setOffsetX(100);
watermark.setOffsetY(200);

// Specify rotation.
watermark.setRotation(30);

// Specify watermark to background.
watermark.setIsBackground(true);

// Specify opacity.
watermark.setOpacity(0.6);

// Specify the scale to page (e.g. 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// Specify watermark for rendering to pdf.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_image_watermark.pdf", options);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
