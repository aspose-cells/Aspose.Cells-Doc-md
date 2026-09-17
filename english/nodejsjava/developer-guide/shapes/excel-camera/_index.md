---
title: Excel Camera in Aspose.Cells for Node.js via Java
description: Learn how to use Excel Camera in Aspose.Cells for Node.js via Java to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
linktitle: Excel Camera
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera is a worksheet object that renders a live image of a cell range and floats on the drawing layer like an ordinary picture. Aspose.Cells supports two creation modes, a dynamic picture that auto-refreshes whenever the source data changes and a static picture that captures a one-time snapshot of a range. This article walks through both approaches so you can pick the one that fits your layout.

## What Is Excel Camera?
The Excel Camera is essentially a picture object anchored to a specific row and column on the worksheet's drawing layer. Unlike a regular inserted picture, the Camera is linked to a source range through an A1-style formula such as `"A1:F10"`. Whenever any cell inside that range changes, the Camera's image is refreshed automatically to reflect the new content. The Camera preserves the full formatting of the source area — borders, background colors, fonts, and number formats — so everything visible inside the cells appears inside the Camera's image as well. This makes the Camera especially useful for dashboards, summaries, side panels, and report layouts where you want a visible preview of a remote region without scrolling or repeating data. Two caveats apply: you must call `updateSelectedValue()` before saving the workbook, and the file will be exported to HTML or PDF, because those formats rely on the embedded image data rather than a live recalculation.

## Method 1 — Add a Dynamic Camera Picture
The dynamic Camera is the most common approach and is the closest match to Excel's built-in Camera tool. It works by adding a picture with no initial image content, then assigning it a `Formula` that references the source range. After the formula is assigned, calling `updateSelectedValue()` refreshes the embedded image data so it is in sync with the cells it mirrors. The Camera is not implemented through a dedicated class — it is built entirely on the standard `Picture` type.
The key APIs are:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — adds a picture anchored at the given row and column. Passing `null` for the `stream` parameter creates an empty picture that acts as the placeholder for a dynamic Camera. The method returns the index of the new picture.
- `worksheet.getPictures().get(index)` — indexer access to retrieve a specific `Picture` from the collection.
- `Picture.Formula` — a string property (`getFormula()`/`setFormula()`) holding the A1-style reference to the source range that the Camera mirrors, such as `"A1:F10"`.
- `Picture.updateSelectedValue()` — a void method that refreshes the embedded image data from the cells referenced by `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` MUST be called before saving when the output is HTML or PDF; otherwise the exported file will not contain the picture data and the Camera will appear blank in the rendered output.
{{% /alert %}}

The following code creates a workbook, adds an empty picture anchored at row 10 column 6, links it to the source range `A1:F10` through the `Formula` property, refreshes the embedded image data, and saves the workbook.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
The static Camera is essentially a one-time rendered preview of a cell range. Instead of maintaining a live link, you render the range to image bytes once, wrap those bytes in a `ByteArrayInputStream`, and add them as a regular picture. The image content is then fixed at the moment of creation and does not auto-refresh when source cells change.
The key APIs are:
- `Cells.createRange(String address)` — builds a `Range` object from an A1-style address such as `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renders the range to image bytes. Passing `null` uses the default rendering options; overloads exist for finer control over output.
- `new ByteArrayInputStream(byte[] buffer)` — wraps the rendered image bytes in a `ByteArrayInputStream` that can be fed into `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — adds the picture anchored at the given row and column, this time passing the `ByteArrayInputStream` produced by the render.
The following code creates a workbook, builds a `Range` for `A1:F10`, renders it to image bytes through `range.toImage(null)`, wraps the bytes in a `ByteArrayInputStream`, adds the picture anchored at row 10 column 6, and saves the workbook.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **Dynamic Camera:** updates on every recalculation, supports HTML and PDF export after `updateSelectedValue()`, and preserves the live-link behavior across the file's lifetime.
- **Static Camera:** a one-time render that never updates, useful when you want a fixed visual snapshot embedded at build time rather than a live mirror of the data.
Aspose.Cells supports both a dynamic, auto-refreshing Camera built on `Picture.Formula` plus `updateSelectedValue()` and a static, one-shot Camera built on `Range.toImage` plus a `ByteArrayInputStream`. Choose the dynamic approach when your output needs to stay in sync with the source cells, and choose the static approach when you only need a fixed visual snapshot at build time.

{{< app/cells/assistant language="nodejs-java" >}}