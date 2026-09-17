---
title: Excel Camera in Aspose.Cells for C++
description: Learn how to use Excel Camera in Aspose.Cells for C++ to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
linktitle: Excel Camera
keywords: Aspose.Cells, C++, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera is a worksheet object that renders a live image of a cell range and floats on the drawing layer like an ordinary picture. Aspose.Cells supports two creation modes, a dynamic picture that auto-refreshes whenever the source data changes and a static picture that captures a one-time snapshot of a range. This article walks through both approaches so you can pick the one that fits your layout.

## What Is Excel Camera?
The Excel Camera is essentially a picture object anchored to a specific row and column on the worksheet's drawing layer. Unlike a regular inserted picture, the Camera is linked to a source range through an A1-style formula such as `"A1:F10"`. Whenever any cell inside that range changes, the Camera's image is refreshed automatically to reflect the new content. The Camera preserves the full formatting of the source area — borders, background colors, fonts, and number formats — so everything visible inside the cells appears inside the Camera's image as well. This makes the Camera especially useful for dashboards, summaries, side panels, and report layouts where you want a visible preview of a remote region without scrolling or repeating data. Two caveats apply: you must call `UpdateSelectedValue()` before saving the workbook, and the file will be exported to HTML or PDF, because those formats rely on the embedded image data rather than a live recalculation.

## Method 1 — Add a Dynamic Camera Picture
The dynamic Camera is the most common approach and is the closest match to Excel's built-in Camera tool. It works by adding a picture with no initial image content, then assigning it a `Formula` that references the source range. After the formula is assigned, calling `UpdateSelectedValue()` refreshes the embedded image data so it is in sync with the cells it mirrors. The Camera is not implemented through a dedicated class — it is built entirely on the standard `Picture` type.
The key APIs are:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — adds a picture anchored at the given row and column. Passing an empty `Vector<uint8_t>()` creates an empty picture that acts as the placeholder for a dynamic Camera. The method returns the index of the new picture.
- `worksheet.GetPictures().Get(int index)` — retrieves a specific `Picture` from the collection by index.
- `Picture.SetFormula(U16String value)` — sets the A1-style reference to the source range that the Camera mirrors, such as `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — refreshes the embedded image data from the cells referenced by `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` MUST be called before saving when the output is HTML or PDF; otherwise the exported file will not contain the picture data and the Camera will appear blank in the rendered output.
{{% /alert %}}

The following code creates a workbook, adds an empty picture anchored at row 10 column 6, links it to the source range `A1:F10` through the `Formula` property, refreshes the embedded image data, and saves the workbook.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Method 2 — Add a Static Camera Picture
The static Camera is essentially a one-time rendered preview of a cell range. Instead of maintaining a live link, you render the range to a `Vector<uint8_t>` byte buffer once, and pass that buffer directly to `Pictures.Add(row, col, data)`. The image content is then fixed at the moment of creation and does not auto-refresh when source cells change.
The key APIs are:
- `Cells.CreateRange(U16String address)` — builds a `Range` object from an A1-style address such as `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — renders the range to a `Vector<uint8_t>` byte buffer. Passing `nullptr` uses default rendering options; overloads exist for finer control over output.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — adds the picture anchored at the given row and column, this time passing the byte buffer produced by `Range.ToImage`.
The following code creates a workbook, builds a `Range` for `A1:F10`, renders it to image bytes through `Range.ToImage(nullptr)`, adds the picture anchored at row 10 column 6, and saves the workbook.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Static Camera: build Range, render to bytes, add as picture
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Choosing Between Dynamic and Static
- **Dynamic Camera:** updates on every recalculation, supports HTML and PDF export after `UpdateSelectedValue()`, and preserves the live-link behavior across the file's lifetime.
- **Static Camera:** a one-time render that never updates, useful when you want a fixed visual snapshot embedded at build time rather than a live mirror of the data.
Aspose.Cells supports both a dynamic, auto-refreshing Camera built on `Picture.Formula` plus `UpdateSelectedValue()` and a static, one-shot Camera built on `Range.ToImage` plus `Vector<uint8_t>`. Choose the dynamic approach when your output needs to stay in sync with the source cells, and choose the static approach when you only need a fixed visual snapshot at build time.

{{< app/cells/assistant language="cpp" >}}