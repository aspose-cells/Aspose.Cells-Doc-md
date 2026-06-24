---
title: Convert Sparkline to Image and HTML in Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines are miniature charts placed inside worksheet cells. Aspose.Cells lets you extract each sparkline as a standalone image (for embedding into another cell or an external report) and also export the entire sparkline-rich worksheet to HTML for browser-based distribution. The `Cell.EmbeddedImage` property used in this article is available in **Aspose.Cells 26.5 and later**.
{{% /alert %}}

## **Introduction**

Sparklines are a compact way to visualize trends directly inside a worksheet. While Excel users see them in place, many real-world scenarios require a sparkline to leave the cell — for example, to be embedded into a different cell as a static picture, attached to an automated email, or rendered as part of an HTML report published to the web.

Aspose.Cells supports both of these operations. The `Sparkline.ToImage` method renders an individual sparkline to a stream, and the resulting bytes can be assigned to `Cell.EmbeddedImage` so the picture is stored inside a single cell of the workbook. Separately, `HtmlSaveOptions` lets you convert the entire workbook — sparklines and all — into a self-contained HTML file. This article walks through both workflows end to end.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**

In this workflow you will build a worksheet that contains a small range of source values, attach three different sparkline groups (Line, Column, and Stacked/Win-Loss) to that range, render each group as a PNG, and write those PNG bytes into adjacent cells as embedded images. The final result is a single `.xlsx` file that contains both the live sparklines and their rendered picture counterparts.

### **Step-by-Step Instructions**

1. Define a working directory and ensure it exists on disk.
2. Create a new `Workbook` and obtain a reference to the first `Worksheet`.
3. Populate cells `A1` through `E1` with five sample numeric values (for example, daily sales or temperature readings).
4. Add three `SparklineGroup` objects to the worksheet by calling `worksheet.SparklineGroups.Add(...)`:
   - A `SparklineType.Line` group anchored at `F1`, with data range `A1:E1`.
   - A `SparklineType.Column` group anchored at `G1`, with data range `A1:E1`.
   - A `SparklineType.Stacked` (win/loss) group anchored at `H1`, with data range `A1:E1`.
5. Build an `ImageOrPrintOptions` instance and set its `ImageType` to `ImageType.Png` so each sparkline is rendered as a transparent PNG.
6. For each of the three groups, render its single sparkline using `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convert the `MemoryStream` to a `Vector<uint8_t>`, and assign the array to `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, and `worksheet.Cells["H2"].EmbeddedImage` respectively.
7. Save the workbook as `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

The code above produces a workbook where each visual representation of a sparkline is duplicated in two forms: the live, native sparkline anchored at row 1, and a static PNG picture embedded directly into a neighboring cell on row 2. Because the pictures live inside the file itself, the workbook remains a single self-contained artifact that can be emailed or archived without breaking the embedded image references. Render each sparkline group as a PNG, convert the `MemoryStream` to a `Vector<uint8_t>`, and assign the array to the `EmbeddedImage` property of the target cell — the assignment is what makes the picture part of the cell's stored contents.

{{% alert color="primary" %}}
Because each sparkline group is anchored to a single cell, you can address it through the indexer `group.Sparklines[0]` instead of enumerating with `foreach`. This keeps the rendering code short and matches the typical "one sparkline per anchor cell" pattern. Storing the picture bytes via `Cell.EmbeddedImage` requires Aspose.Cells 26.5 or later.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**

Once the workbook contains live sparklines (and optionally embedded picture counterparts), the entire worksheet can be published to the web by saving it as HTML. The `HtmlSaveOptions` class exposes the knobs you need to control this export; in this workflow you will reuse the `output_with_sparklines.xlsx` file produced by Workflow 1 and convert it to a clean, single-page HTML document.

### **Step-by-Step Instructions**

1. Ensure the `output_with_sparklines.xlsx` file produced by Workflow 1 is available on disk in your working directory.
2. Load that file into a new `Workbook` instance.
3. Instantiate `HtmlSaveOptions` and set its `ExportActiveWorksheetOnly` property to `true` so the resulting HTML file contains only the active worksheet rather than the entire workbook.
4. Call `workbook.Save("sparklines.html", htmlOptions)` to write the HTML output to disk.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

The code above takes the sparkline-rich workbook from Workflow 1 and turns it into a portable HTML file. Sparklines are preserved as inline SVG or PNG renderings inside the generated HTML, depending on the export mode, so end users can view the trends in any modern browser without needing Excel installed. By setting `ExportActiveWorksheetOnly` to `true`, you avoid accidentally publishing hidden sheets or auxiliary data — only the worksheet currently visible to the user is exported.

{{% alert color="primary" %}}
The `HtmlSaveOptions` class offers additional properties for fine-tuning the output, such as `ExportHiddenWorksheet`, `ExportImagesAsBase64`, and `Encoding`. Adjust these as needed for your deployment target.
{{% /alert %}}

## **API Summary**

The workflows above rely on a small set of Aspose.Cells APIs working together.

- `SparklineGroup` and the collection accessor `worksheet.SparklineGroups` are used to declare the type (Line, Column, Stacked), the data range, and the anchor cell for each sparkline group. In this article each group is anchored to a single cell, so the group is reached through `worksheet.SparklineGroups[i]`.
- `Sparkline` and the indexer `group.Sparklines[0]` return the individual sparkline inside a group. Because every group in the example contains exactly one sparkline, no `foreach` loop is required.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` is the rendering method that writes a picture of the sparkline into a supplied `Stream`. The method returns `void`; you read the bytes from the stream after the call.
- `Cell.EmbeddedImage` is a `Vector<uint8_t>` property that stores a picture inside a single cell. It is available in **Aspose.Cells 26.5 and later** and is the recommended way to round-trip a sparkline rendered by `ToImage` back into the same workbook.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (a `bool`) restricts HTML export to the active worksheet. It is one of the most commonly used properties on `HtmlSaveOptions` when generating single-page reports.
- `ImageOrPrintOptions.ImageType` lives in the `Aspose.Cells.Drawing` namespace and selects the picture format (for example, `ImageType.Png`) used when rendering with `ToImage` and when printing worksheets to images.

## **Related Articles**

- [Sparklines in Aspose.Cells for Aspose.Cells for C++](/cells/cpp/sparkline/)
- [Inserting an Image into a Cell](/cells/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}