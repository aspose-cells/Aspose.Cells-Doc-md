---
title: Convert Sparkline to Image and HTML in Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines are miniature charts placed inside worksheet cells. Aspose.Cells lets you extract each sparkline as a standalone image (for embedding into another cell or an external report) and also export the entire sparkline-rich worksheet to HTML for browser-based distribution. The `Cell.embedded_image` property used in this article is available in **Aspose.Cells 26.5 and later**.
{{% /alert %}}

## **Introduction**

Sparklines are a compact way to visualize trends directly inside a worksheet. While Excel users see them in place, many real-world scenarios require a sparkline to leave the cell — for example, to be embedded into a different cell as a static picture, attached to an automated email, or rendered as part of an HTML report published to the web.

Aspose.Cells supports both of these operations. The `Sparkline.to_image` method renders an individual sparkline to a stream, and the resulting bytes can be assigned to `Cell.embedded_image` so the picture is stored inside a single cell of the workbook. Separately, `HtmlSaveOptions` lets you convert the entire workbook — sparklines and all — into a self-contained HTML file. This article walks through both workflows end to end.

## **Workflow 1 — Render Sparklines to Images and Embed Them Into Cells**

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
6. For each of the three groups, render its single sparkline using `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, convert the `ByteArrayOutputStream` to a `byte[]` (or read its `to_byte_array()` into Python `bytes`), and assign the bytes to `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image`, and `worksheet.cells["H2"].embedded_image` respectively.
7. Save the workbook as `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Create a new workbook and access the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Add a Line sparkline group anchored at F1 (column 5, row 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Add a Column sparkline group anchored at G1 (column 6, row 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Configure image options for PNG output
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Convert the Line sparkline to image and embed it in cell F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Convert the Column sparkline to image and embed it in cell G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Convert the Win/Loss sparkline to image and embed it in cell H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

The code above produces a workbook where each visual representation of a sparkline is duplicated in two forms: the live, native sparkline anchored at row 1, and a static PNG picture embedded directly into a neighboring cell on row 2. Because the pictures live inside the file itself, the workbook remains a single self-contained artifact that can be emailed or archived without breaking the embedded image references. Render each sparkline group as a PNG, convert the `ByteArrayOutputStream` to a `byte[]` (or use `to_byte_array()` to obtain a Python `bytes` object), and assign the array to the `embedded_image` property of the target cell — the assignment is what makes the picture part of the cell's stored contents.

{{% alert color="primary" %}}
Because each sparkline group is anchored to a single cell, you can address it through the indexer `group.sparklines[0]` instead of enumerating with a `for` loop. This keeps the rendering code short and matches the typical "one sparkline per anchor cell" pattern. Storing the picture bytes via `Cell.embedded_image` requires Aspose.Cells 26.5 or later.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**

Once the workbook contains live sparklines (and optionally embedded picture counterparts), the entire worksheet can be published to the web by saving it as HTML. The `HtmlSaveOptions` class exposes the knobs you need to control this export; in this workflow you will reuse the `output_with_sparklines.xlsx` file produced by Workflow 1 and convert it to a clean, single-page HTML document.

### **Step-by-Step Instructions**

1. Ensure the `output_with_sparklines.xlsx` file produced by Workflow 1 is available on disk in your working directory.
2. Load that file into a new `Workbook` instance.
3. Instantiate `HtmlSaveOptions` and set its `export_active_worksheet_only` property to `True` so the resulting HTML file contains only the active worksheet rather than the entire workbook.
4. Call `workbook.save("sparklines.html", html_options)` to write the HTML output to disk.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

The code above takes the sparkline-rich workbook from Workflow 1 and turns it into a portable HTML file. Sparklines are preserved as inline SVG or PNG renderings inside the generated HTML, depending on the export mode, so end users can view the trends in any modern browser without needing Excel installed. By setting `export_active_worksheet_only` to `True`, you avoid accidentally publishing hidden sheets or auxiliary data — only the worksheet currently visible to the user is exported.

{{% alert color="primary" %}}
The `HtmlSaveOptions` class offers additional properties for fine-tuning the output, such as `export_hidden_worksheet`, `export_images_as_base64`, and `encoding`. Adjust these as needed for your deployment target.
{{% /alert %}}

## **API Summary**

The workflows above rely on a small set of Aspose.Cells APIs working together.

- `SparklineGroup` and the collection accessor `worksheet.sparkline_groups` are used to declare the type (Line, Column, Stacked), the data range, and the anchor cell for each sparkline group. In this article each group is anchored to a single cell, so the group is reached through `worksheet.sparkline_groups[i]`.
- `Sparkline` and the indexer `group.sparklines[0]` return the individual sparkline inside a group. Because every group in the example contains exactly one sparkline, no `for` loop is required.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` is the rendering method that writes a picture of the sparkline into a supplied `OutputStream` (such as a `ByteArrayOutputStream`). The method returns `void`; you read the bytes from the stream after the call.
- `Cell.embedded_image` is a `byte[]` property that stores a picture inside a single cell. It is available in **Aspose.Cells 26.5 and later** and is the recommended way to round-trip a sparkline rendered by `to_image` back into the same workbook.
- `HtmlSaveOptions.export_active_worksheet_only` (a `bool`) restricts HTML export to the active worksheet. It is one of the most commonly used properties on `HtmlSaveOptions` when generating single-page reports.
- `ImageOrPrintOptions.image_type` lives in the `com.aspose.cells.drawing` namespace and selects the picture format (for example, `ImageType.PNG`) used when rendering with `to_image` and when printing worksheets to images.

## **Related Articles**

- [Sparklines in Aspose.Cells for Aspose.Cells for Python via Java](/cells/python-java/sparkline/)
- [Inserting an Image into a Cell](/cells/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}