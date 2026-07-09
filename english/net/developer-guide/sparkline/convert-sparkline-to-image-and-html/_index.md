---
title: Convert Sparkline to Image and HTML in Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
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

1. Create a new `Workbook` and obtain a reference to the first `Worksheet`.
2. Populate cells `A1` through `E1` with five sample numeric values (for example, daily sales or temperature readings).
3. Add three `SparklineGroup` objects to the worksheet by calling `worksheet.SparklineGroups.Add(...)`:
   - A `SparklineType.Line` group anchored at `F1`, with data range `A1:E1`.
   - A `SparklineType.Column` group anchored at `G1`, with data range `A1:E1`.
   - A `SparklineType.Stacked` (win/loss) group anchored at `H1`, with data range `A1:E1`.
4. Build an `ImageOrPrintOptions` instance and set its `ImageType` to `ImageType.Png` so each sparkline renders as a PNG picture.
5. For each of the three groups, render its single sparkline using `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convert the `MemoryStream` to a `byte[]`, and assign the array to `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, and `worksheet.Cells["H2"].EmbeddedImage` respectively.
6. Save the workbook as `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Populate sample data in cells A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Add a Line sparkline group anchored at F1 (column 5, row 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Add a Column sparkline group anchored at G1 (column 6, row 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configure image options for PNG output
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Convert the Line sparkline to image and embed it in cell F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Convert the Column sparkline to image and embed it in cell G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Convert the Win/Loss sparkline to image and embed it in cell H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Save the workbook to disk
workbook.Save("output_with_sparklines.xlsx");
```

The code above produces a workbook where each visual representation of a sparkline exists in two forms: the live, native sparkline anchored at row 1, and a static PNG picture embedded directly into a neighboring cell on row 2. Because the pictures live inside the file itself, the workbook remains a single self-contained artifact that can be emailed or archived without breaking the embedded image references.

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

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

The code above takes the sparkline-rich workbook from Workflow 1 and turns it into a portable HTML file. The sparkline groups are rendered as inline images inside the generated HTML table, so end users can view the trends in any modern browser without needing Excel installed. By setting `ExportActiveWorksheetOnly` to `true`, you avoid accidentally publishing hidden sheets or auxiliary data — only the worksheet currently visible to the user is exported.

{{% alert color="primary" %}}
The `HtmlSaveOptions` class offers additional properties for fine-tuning the output, such as `ExportHiddenWorksheet`, `ExportImagesAsBase64`, and `Encoding`. Adjust these as needed for your deployment target.
{{% /alert %}}

## **API Summary**

The workflows above rely on a small set of Aspose.Cells APIs working together.

- `SparklineGroup` and the collection accessor `worksheet.SparklineGroups` are used to declare the type (Line, Column, Stacked), the data range, and the anchor cell for each sparkline group. In this article each group is anchored to a single cell, so the group is reached through `worksheet.SparklineGroups[i]`.
- `Sparkline` and the indexer `group.Sparklines[0]` return the individual sparkline inside a group. Because every group in the example contains exactly one sparkline, no `foreach` loop is required.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` is the rendering method that writes a picture of the sparkline into a supplied `Stream`. The method returns `void`; you read the bytes from the stream after the call.
- `Cell.EmbeddedImage` is a `byte[]` property that stores a picture inside a single cell. It is available in **Aspose.Cells 26.5 and later** and is the recommended way to round-trip a sparkline rendered by `ToImage` back into the same workbook.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (a `bool`) restricts HTML export to the active worksheet. It is one of the most commonly used properties on `HtmlSaveOptions` when generating single-page reports.
- `ImageOrPrintOptions.ImageType` lives in the `Aspose.Cells.Drawing` namespace and selects the picture format (for example, `ImageType.Png`) used when rendering with `ToImage` and when printing worksheets to images.

## **Related Articles**

- [Creating Sparklines in Aspose.Cells for .NET](/net/creating-sparklines/)

{{< app/cells/assistant language="csharp" >}}