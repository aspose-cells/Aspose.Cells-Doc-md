---
title: Excel Camera in Aspose.Cells for Python via .NET
description: Learn how to use Excel Camera in Aspose.Cells for Python via .NET to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
linktitle: Excel Camera
keywords: Aspose.Cells, Python, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera is a worksheet object that renders a live image of a cell range and floats on the drawing layer like an ordinary picture. Aspose.Cells supports two creation modes, a dynamic picture that auto-refreshes whenever the source data changes and a static picture that captures a one-time snapshot of a range. This article walks through both approaches so you can pick the one that fits your layout.

## What Is Excel Camera?
The Excel Camera is essentially a picture object anchored to a specific row and column on the worksheet's drawing layer. Unlike a regular inserted picture, the Camera is linked to a source range through an A1-style formula such as `"A1:F10"`. Whenever any cell inside that range changes, the Camera's image is refreshed automatically to reflect the new content. The Camera preserves the full formatting of the source area — borders, background colors, fonts, and number formats — so everything visible inside the cells appears inside the Camera's image as well. This makes the Camera especially useful for dashboards, summaries, side panels, and report layouts where you want a visible preview of a remote region without scrolling or repeating data. Two caveats apply: you must call `update_selected_value()` before saving the workbook, and the file will be exported to HTML or PDF, because those formats rely on the embedded image data rather than a live recalculation.

## Method 1 — Add a Dynamic Camera Picture
The dynamic Camera is the most common approach and is the closest match to Excel's built-in Camera tool. It works by adding a picture with no initial image content, then assigning it a `formula` that references the source range. After the formula is assigned, calling `update_selected_value()` refreshes the embedded image data so it is in sync with the cells it mirrors. The Camera is not implemented through a dedicated class — it is built entirely on the standard `Picture` type.
The key APIs are:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — adds a picture anchored at the given row and column. Passing `None` for the `stream` parameter creates an empty picture that acts as the placeholder for a dynamic Camera. The method returns the index of the new picture.
- `worksheet.pictures[index]` — indexer access to retrieve a specific `Picture` from the collection.
- `picture.formula` — a string property (get/set) holding the A1-style reference to the source range that the Camera mirrors, such as `"A1:F10"`.
- `picture.update_selected_value()` — a void method that refreshes the embedded image data from the cells referenced by `formula`.

{{% alert color="primary" %}}
`update_selected_value()` MUST be called before saving when the output is HTML or PDF; otherwise the exported file will not contain the picture data and the Camera will appear blank in the rendered output.
{{% /alert %}}

The following code creates a workbook, adds an empty picture anchored at row 10 column 6, links it to the source range `A1:F10` through the `formula` property, refreshes the embedded image data, and saves the workbook.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Dynamic Camera: add an empty picture, link it via formula to A1:F10, then refresh
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Method 2 — Add a Static Camera Picture
The static Camera is essentially a one-time rendered preview of a cell range. Instead of maintaining a live link, you render the range to image bytes once, wrap those bytes in a `BytesIO`, and add them as a regular picture. The image content is then fixed at the moment of creation and does not auto-refresh when source cells change.
The key APIs are:
- `Cells.create_range(string address)` — builds a `Range` object from an A1-style address such as `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — renders the range to image bytes. Passing `None` uses the default rendering options; overloads exist for finer control over output.
- `BytesIO(byte[] buffer)` — wraps the rendered image bytes in a `BytesIO` that can be fed into `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — adds the picture anchored at the given row and column, this time passing the `BytesIO` produced by the render.
The following code creates a workbook, builds a `Range` for `A1:F10`, renders it to image bytes through `Range.to_image(null)`, wraps the bytes in a `BytesIO`, adds the picture anchored at row 10 column 6, and saves the workbook.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Static Camera: build Range, render to bytes, wrap in BytesIO, add as picture
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Choosing Between Dynamic and Static
- **Dynamic Camera:** updates on every recalculation, supports HTML and PDF export after `update_selected_value()`, and preserves the live-link behavior across the file's lifetime.
- **Static Camera:** a one-time render that never updates, useful when you want a fixed visual snapshot embedded at build time rather than a live mirror of the data.
Aspose.Cells supports both a dynamic, auto-refreshing Camera built on `picture.formula` plus `update_selected_value()` and a static, one-shot Camera built on `Range.to_image` plus a `BytesIO`. Choose the dynamic approach when your output needs to stay in sync with the source cells, and choose the static approach when you only need a fixed visual snapshot at build time.

{{< app/cells/assistant language="python-net" >}}