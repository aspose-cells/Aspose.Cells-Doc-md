---
title: Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions in Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines are miniature charts placed inside worksheet cells. Aspose.Cells lets you extract each sparkline as a standalone image (for embedding into another cell or an external report) and also export the entire sparkline-rich worksheet to HTML for browser-based distribution. The `cell.embedded_image` property used in this article is available in **Aspose.Cells 26.5 and later**.
{{% /alert %}}

## **Introduction**

Sparklines are a compact way to visualize trends directly inside a worksheet. While Excel users see them in place, many real-world scenarios require a sparkline to leave the cell — for example, to be embedded into a different cell as a static picture, attached to an automated email, or rendered as part of an HTML report published to the web.

Aspose.Cells supports both of these operations. The `sparkline.to_image` method renders an individual sparkline to a stream, and the resulting bytes can be assigned to `cell.embedded_image` so the picture is stored inside a single cell of the workbook. Separately, `HtmlSaveOptions` lets you convert the entire workbook — sparklines and all — into a self-contained HTML file. This article walks through both workflows end to end.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**

In this workflow you will build a worksheet that contains a small range of source values, attach three different sparkline groups (Line, Column, and Stacked/Win-Loss) to that range, render each group as a PNG, and write those PNG bytes into adjacent cells as embedded images. The final result is a single `.xlsx` file that contains both the live sparklines and their rendered picture counterparts.

### **Step-by-Step Instructions**

1. Define a working directory and ensure it exists on disk.
2. Create a new `Workbook` and obtain a reference to the first `Worksheet`.
3. Populate cells `A1` through `E1` with five sample numeric values (for example, daily sales or temperature readings).
4. Add three `SparklineGroup` objects to the worksheet by calling `worksheet.sparkline_groups.add(...)`:
   - A `SparklineType.LINE` group anchored at `F1`, with data range `A1:E1`.
   - A `SparklineType.COLUMN` group anchored at `G1`, with data range `A1:E1`.
   - A `SparklineType.STACKED` (win/loss) group anchored at `H1`, with data range `A1:E1`.
5. Build an `ImageOrPrintOptions` instance and set its `image_type` to `ImageType.PNG` so each sparkline is rendered as a transparent PNG.
6. For each of the three groups, render its single sparkline using `group.sparklines[0].to_image(memory_stream, image_options)`, convert the `BytesIO` stream to a `bytes` object, and assign the array to `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image`, and `worksheet.cells["H2"].embedded_image` respectively.
7. Save the workbook as `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Create a new workbook and access the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Populate sample data in cells A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Add a Line sparkline group anchored at F1 (column 5, row 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Add a Column sparkline group anchored at G1 (column 6, row 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Configure image options for PNG output
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Convert the Line sparkline to image and embed it in cell F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Convert the Column sparkline to image and embed it in cell G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Convert the Win/Loss sparkline to image and embed it in cell H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")
```

The code above produces a workbook where each visual representation of a sparkline is duplicated in two forms: the live, native sparkline anchored at row 1, and a static PNG picture embedded directly into a neighboring cell on row 2. Because the pictures live inside the file itself, the workbook remains a single self-contained artifact that can be emailed or archived without breaking the embedded image references. Render each sparkline group as a PNG, convert the `BytesIO` stream to a `bytes` object, and assign the bytes to the `embedded_image` property of the target cell — the assignment is what makes the picture part of the cell's stored contents.

{{% alert color="primary" %}}
Because each sparkline group is anchored to a single cell, you can address it through the indexer `group.sparklines[0]` instead of enumerating with a `for` loop. This keeps the rendering code short and matches the typical "one sparkline per anchor cell" pattern. Storing the picture bytes via `cell.embedded_image` requires Aspose.Cells 26.5 or later.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**

Once the workbook contains live sparklines (and optionally embedded picture counterparts), the entire worksheet can be published to the web by saving it as HTML. The `HtmlSaveOptions` class exposes the knobs you need to control this export; in this workflow you will reuse the `output_with_sparklines.xlsx` file produced by Workflow 1 and convert it to a clean, single-page HTML document.

### **Step-by-Step Instructions**

1. Ensure the `output_with_sparklines.xlsx` file produced by Workflow 1 is available on disk in your working directory.
2. Load that file into a new `Workbook` instance.
3. Instantiate `HtmlSaveOptions` and set its `export_active_worksheet_only` property to `True` so the resulting HTML file contains only the active worksheet rather than the entire workbook.
4. Call `workbook.save("sparklines.html", html_options)` to write the HTML output to disk.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

The code above takes the sparkline-rich workbook from Workflow 1 and turns it into a portable HTML file. Sparklines are preserved as inline SVG or PNG renderings inside the generated HTML, depending on the export mode, so end users can view the trends in any modern browser without needing Excel installed. By setting `export_active_worksheet_only` to `True`, you avoid accidentally publishing hidden sheets or auxiliary data — only the worksheet currently visible to the user is exported.

{{% alert color="primary" %}}
The `HtmlSaveOptions` class offers additional properties for fine-tuning the output, such as `export_hidden_worksheet`, `export_images_as_base64`, and `encoding`. Adjust these as needed for your deployment target.
{{% /alert %}}

## **API Summary**

The workflows above rely on a small set of Aspose.Cells APIs working together.

- `SparklineGroup` and the collection accessor `worksheet.sparkline_groups` are used to declare the type (Line, Column, Stacked), the data range, and the anchor cell for each sparkline group. In this article each group is anchored to a single cell, so the group is reached through `worksheet.sparkline_groups[i]`.
- `Sparkline` and the indexer `group.sparklines[0]` return the individual sparkline inside a group. Because every group in the example contains exactly one sparkline, no `for` loop is required.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` is the rendering method that writes a picture of the sparkline into a supplied stream. The method returns `None`; you read the bytes from the stream after the call.
- `cell.embedded_image` is a `bytes` property that stores a picture inside a single cell. It is available in **Aspose.Cells 26.5 and later** and is the recommended way to round-trip a sparkline rendered by `to_image` back into the same workbook.
- `html_save_options.export_active_worksheet_only` (a `bool`) restricts HTML export to the active worksheet. It is one of the most commonly used properties on `HtmlSaveOptions` when generating single-page reports.
- `image_or_print_options.image_type` lives in the `aspose.cells.drawing` namespace and selects the picture format (for example, `ImageType.PNG`) used when rendering with `to_image` and when printing worksheets to images.

## **Related Articles**

- [Sparklines in Aspose.Cells for Python via .NET](/cells/python-net/sparkline/)
- [Inserting an Image into a Cell](/cells/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}