---
title: Inserting an Image into a Cell
description: Aspose.Cells is a Python library for working with spreadsheet files. This article explains how to fit a picture exactly to a single cell, either by placing a floating picture over the cell or by embedding the image directly into the cell.
keywords: Aspose.Cells, Python library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells provides two distinct ways to associate an image with a single cell. A floating picture is a shape on the worksheet drawing layer that visually overlays a cell range, while an embedded image is stored inside the cell itself and scales automatically to the cell's display area. Choose the approach that best matches your layout requirements.

{{% /alert %}}

## **Introduction**

Fitting a picture exactly to a single cell is a common requirement when designing spreadsheets that act as visual reports, product catalogs, employee directories, dashboards, or inventory lists. Rather than stretching an image across many cells or placing it loosely on a worksheet, you may want a clean, cell-bound image that stays aligned with the cell that owns it.

Aspose.Cells supports this scenario in two complementary ways:

- **Approach 1 — Place a floating picture over a cell.** Add a `Picture` to the worksheet, set its `placement` to `MOVE_AND_SIZE`, and adjust its anchor cells (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) so the picture covers exactly one cell.
- **Approach 2 — Embed an image directly in a cell.** Assign image bytes to the cell's `embedded_image` property. The image automatically scales to fit the cell's display area and travels with the cell.

The rest of this article walks through both approaches, explains the relevant APIs, and shows how to use them in code.

## **Approach 1: Place a Picture Over a Cell**

A floating picture is a `Picture` object that lives on the worksheet drawing layer. Although it is not part of any single cell, it is anchored to a cell range. The picture's anchor cells — its upper-left and lower-right corners — determine its visual extent on the worksheet. By default, a freshly added picture spans several cells.

To make a floating picture cover **exactly one cell**, you need to:

1. Add the picture using `Worksheet.pictures.add(row, column, stream)`, which anchors the new picture to the given cell.
2. Set the four anchor properties so the picture's bounding rectangle coincides with the target cell.
3. Set `Picture.placement` to `PlacementType.MOVE_AND_SIZE` so the picture moves and resizes with the underlying cell when the user changes the column width or row height.

### **Anchoring the Picture to a Single Cell**

The picture's anchor is defined by four zero-based index properties:

- `Picture.upper_left_row` — the row index of the picture's top edge.
- `Picture.upper_left_column` — the column index of the picture's left edge.
- `Picture.lower_right_row` — the row index of the picture's bottom edge. To make the picture's bottom edge sit at the bottom of row `r`, set this to `r + 1`.
- `Picture.lower_right_column` — the column index of the picture's right edge. To make the picture's right edge sit at the right of column `c`, set this to `c + 1`.

For example, to fit the picture exactly into cell **C6** (row index `5`, column index `2`), set `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, and `lower_right_column = 3`.

{{% alert color="primary" %}}

Row and column indices in Aspose.Cells are **zero-based**. Cell C6 has row index 5 and column index 2. Off-by-one errors on the lower-right anchor are the most common source of pictures that appear to overlap into an adjacent cell.

{{% /alert %}}

### **Controlling Placement Behavior**

`Picture.placement` is an enum of type `PlacementType` that controls how the picture behaves when the user resizes the row or column beneath it. The recommended value for a single-cell picture is `PlacementType.MOVE_AND_SIZE`, which causes the picture to move and resize together with its underlying cell, preserving the exact fit.

### **Step-by-Step Instructions**

1. Create a new `Workbook` (or open an existing one).
2. Access the target `Worksheet` from `workbook.worksheets[0]`.
3. Open the image file from disk into a file stream (or a `BytesIO` object) using a `with` block so the stream is disposed properly.
4. Call `worksheet.pictures.add(5, 2, stream)` to add a picture anchored to cell C6. Capture the returned `Picture` reference.
5. Set the four anchor coordinates so the picture covers only cell C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Set `picture.placement = PlacementType.MOVE_AND_SIZE` to keep the picture aligned with C6 when the column or row is resized.
7. Optionally add sample text to surrounding cells to demonstrate that only cell C6 contains the picture.
8. Save the workbook to disk as an `.xlsx` file.

The following code demonstrates the complete approach.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Approach 2: Embed an Image Directly in a Cell**

Aspose.Cells also exposes a simpler mechanism for cell-bound images: the `Cell.embedded_image` property. Assigning image bytes to this property attaches the image to the cell itself, as if it were inline content.

### **How Embedded Images Work**

- The image is stored as part of the cell content rather than as a shape on the drawing layer.
- The image automatically scales to fit inside the cell's rendered boundaries. No anchor coordinates or placement settings are required.
- The cell remains a real cell with a real address that can be referenced by formulas, sorted as part of a row, or used in other cell-level operations.

This makes `Cell.embedded_image` the most concise option when your goal is simply "an image that lives inside this cell."

### **Step-by-Step Instructions**

1. Create a new `Workbook` (or open an existing one).
2. Access the target `Worksheet` from `workbook.worksheets[0]`.
3. Read the image file from disk into a `bytes` object (for example, by opening the file in binary mode and calling `.read()`).
4. Get a reference to the target cell — either through `worksheet.cells["C6"]` or `worksheet.cells[5, 2]`.
5. Assign the bytes object to the cell's `embedded_image` property.
6. Optionally adjust the row height and column width of the target row and column to give the embedded image a more prominent appearance.
7. Save the workbook to disk as an `.xlsx` file.

The following code demonstrates the complete approach.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Get the target cell C6
cell = worksheet.cells["C6"]

# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()

# Embed the image directly into the cell
cell.embedded_image = imageData

# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)

# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choosing the Right Approach**

Both approaches produce a picture that fits inside a single cell, but they differ in how the picture is stored and how it behaves:

- **Use a floating picture (Approach 1) when:**
  - You need finer control over placement, layering, or alignment with other drawing objects.
  - You want the picture to behave as a shape that can be selected, reordered, or grouped with other shapes.
  - You require legacy compatibility with code that already works with `pictures` collections.
  - You need to compute anchor coordinates dynamically based on worksheet layout.

- **Use an embedded image (Approach 2) when:**
  - You want the simplest possible insertion of an image into a cell.
  - The image should travel with the cell like any other cell content.
  - You do not need to manipulate the image as a shape.

{{% alert color="primary" %}}

Both approaches can coexist in the same workbook. You can place floating pictures over one set of cells and embed images directly into other cells, as the two mechanisms use different storage layers in the file.

{{% /alert %}}

## **Related Articles**

- [How to Insert Picture in Cell](/cells/python-net/how-to-place-image-to-cell/)
- [Add Image Hyperlinks](/cells/python-net/add-image-hyperlinks/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulate Position Size and Designer Chart](/cells/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}