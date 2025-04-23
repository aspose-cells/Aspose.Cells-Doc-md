---
title: إضافة علامة مائية إلى PDF مع Node.js عبر C++
linktitle: إضافة علامة مائية إلى ملف PDF
type: docs
weight: 9
url: /ar/nodejs-cpp/add-watermark-to-pdf/
description: تعلم كيفية إضافة علامة مائية نصية وصورة إلى PDF أثناء تحويل إكسل إلى PDF باستخدام Aspose.Cells for Node.js via C++.
---

 أثناء تحويل ملف إكسل إلى PDF، قد يكون لديك متطلبات لإضافة علامة مائية إلى ملف PDF. تُظهر الأمثلة التالية كيفية إضافة علامات مائية نصية وصورة إلى الملف أثناء التصدير.

## **إضافة علامة مائية نصية إلى PDF**

 يمكنك بسهولة إضافة علامة مائية نصية إلى ملف PDF عن طريق تحديد النص والخط المقابل. أيضًا، يمكنك ضبط المحاذاة، الإزاحة، الدوران، الشفافية، اللون الأمامي والخلفي، والتحجيم إلى الصفحة في [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/).

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

## **إضافة علامة مائية صورة إلى PDF**

 يمكنك إضافة علامة مائية صورة إلى ملف PDF فقط عن طريق تحديد بيانات الصورة. أيضًا، يمكنك ضبط المحاذاة، الإزاحة، الدوران، الشفافية، اللون الأمامي والخلفي، والتحجيم إلى الصفحة في [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/).

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

